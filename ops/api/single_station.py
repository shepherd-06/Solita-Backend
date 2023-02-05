from django.views import View
from django.http import JsonResponse
from ops.models import Station, DepartureInfo, ReturnInfo, Journey
from django.db.models import Sum


class SingleStationView(View):

    """
    single station view.
    will return
    - total number of journey from this station
    - total number of journey returning to this station
    """

    def get(self, request):
        station_id = request.GET.get("station_id", None)
        if station_id is None:
            return JsonResponse({
                "message": "Missing parameter {station_id}."
            }, status=400)
        try:
            station_obj = Station.objects.get(station_id=station_id)
        except Station.DoesNotExist:
            return JsonResponse({
                "message": "Invalid request!"
            }, status=404)

        departure_count = DepartureInfo.objects.filter(
            departure_station_id=station_obj.id).count()
        return_count = ReturnInfo.objects.filter(
            return_station_id=station_obj.id).count()

        total_departure_distance = Journey.objects.filter(
            departure_info__departure_station_id=station_obj.id)\
            .aggregate(total=Sum('distance'))["total"]
        average_departure_distance = total_departure_distance / departure_count

        total_return_distance = Journey.objects.filter(
            return_info__return_station_id=station_obj.id)\
            .aggregate(total=Sum('distance'))["total"]
        average_return_distance = total_return_distance / return_count

        all_return_station = Journey.objects.filter(
            departure_info__departure_station_id=station_obj.id)\
            .values_list('return_info__return_station_name', flat=True)

        all_return_dict = {}
        for station_name in all_return_station:
            if station_name in all_return_dict:
                all_return_dict[station_name] += 1
            else:
                all_return_dict[station_name] = 1

        all_return_dict = sorted(
            all_return_dict.items(), key=lambda x: x[1], reverse=True)[:5]
        popular_return = [item[0] for item in all_return_dict]

        all_departure_station = Journey.objects.filter(
            return_info__return_station_id=station_obj.id)\
            .values_list('departure_info__departure_station_name', flat=True)

        all_depar_dict = {}
        for station_name in all_departure_station:
            if station_name in all_depar_dict:
                all_depar_dict[station_name] += 1
            else:
                all_depar_dict[station_name] = 1

        all_depar_dict = sorted(
            all_depar_dict.items(), key=lambda x: x[1], reverse=True)[:5]
        popular_depart = [item[0] for item in all_depar_dict]

        station_data = station_obj.__dict__
        station_data.pop('_state')
        station_data.pop('id')
        station_data["created_at"] = station_data["created_at"].timestamp()
        station_data["updated_at"] = station_data["updated_at"].timestamp()

        data = {
            "start_from": departure_count,
            "return_to": return_count,
            "avg_departure_distance": average_departure_distance,
            "avg_return_distance": average_return_distance,
            "popular_return": popular_return,
            "popular_departure": popular_depart,
            "station": station_data,
        }

        return JsonResponse({
            "data": data
        })
