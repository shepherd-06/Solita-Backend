from django.views import View
from django.http import JsonResponse
from ops.models import Station, DepartureInfo, ReturnInfo


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

        data = {
            "start_from": departure_count,
            "return_to": return_count
        }

        return JsonResponse({
            "data": data
        })
