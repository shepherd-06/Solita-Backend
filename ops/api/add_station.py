from django.http import JsonResponse
from rest_framework.views import APIView
from ops.serializer import StationSerializer
from random import randint
from ops.models import Station


# @method_decorator(csrf_exempt, name='dispatch')
class AddStation(APIView):

    REQUIRED_PARAMS = ["coordinate_x", "coordinate_y"]
    # at least one of them has to be present
    OPTIONAL_PARAMS = ["name_en", "name_fi", "name_sw"]

    def post(self, request):
        """_summary_
        API to add a new station on the list
        Args:
            request (_type_): _description_
        """
        data = request.data
        names = ["name_en", "name_fi", "name_sw"]
        flag = False

        for name in names:
            if name in data:
                flag = True

        if not flag:
            return JsonResponse({
                "message": "at least one station name is required",
                "options": names,
            }, status=400)

        for item in self.REQUIRED_PARAMS:
            if item not in data:
                return JsonResponse({
                    "message": "Coordinates are required",
                }, status=400)
        
        while True:
            station_id = randint(10000000, 500000000)
            try:
                Station.objects.get(station_id=station_id)
            except Station.DoesNotExist:
                # found a unique station id from the random number.
                break
            
        data["station_id"] = station_id
        serializer = StationSerializer(data=data)
        if serializer.is_valid():
            station_obj = serializer.save()
            station_data = station_obj.__dict__
            station_data.pop('_state')
            station_data.pop('id')
            station_data["created_at"] = station_data["created_at"].timestamp()
            station_data["updated_at"] = station_data["updated_at"].timestamp()
            data = {
                "start_from": 0,
                "return_to": 0,
                "avg_departure_distance": 0,
                "avg_return_distance": 0,
                "popular_return": 0,
                "popular_departure": 0,
                "station": station_data,
            }
            return JsonResponse({
                "message": "{} station created".format(station_obj),
                "data": data
            }, status=201)
        else:
            return JsonResponse({
                "message": serializer.errors,
            }, status=400)
