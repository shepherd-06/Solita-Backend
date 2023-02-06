from django.http import JsonResponse
from rest_framework.views import APIView
from ops.serializer import (DepartureSerializer,
                            JourneySerializer,
                            ReturnSerializer)
from ops.models import Station
from datetime import datetime


class AddJourney(APIView):

    REQUIRED_PARAMS = (
        "departure_time",
        "departure_station_id",
        "return_time",
        "return_station_id",
        "distance",
        "duration"
    )

    def post(self, request):
        data = request.data

        for item in self.REQUIRED_PARAMS:
            if item not in data:
                return JsonResponse({
                    "message": "required parameter: {} is missing.".format(item)
                }, status=400)
        try:
            departure_obj = Station.objects.get(
                station_id=data["departure_station_id"])
        except Station.DoesNotExist:
            return JsonResponse({
                "message": "Departure Station does not exist!"
            }, status=400)

        try:
            return_obj = Station.objects.get(
                station_id=data["return_station_id"])
        except Station.DoesNotExist:
            return JsonResponse({
                "message": "Return Station does not exist!"
            }, status=400)

        if departure_obj.id == return_obj.id:
            return JsonResponse({
                "message": "Departure and Return Station cannot be same!"
            }, status=400)

        if data["distance"] < 10:
            return JsonResponse({
                "message": "Journey distance cannot be less than 10 meter"
            }, status=400)

        if data["duration"] < 10:
            return JsonResponse({
                "message": "Journey duration cannot be less than 10 seconds"
            }, status=400)

        departure_time = datetime.fromtimestamp(data["departure_time"])
        return_time = datetime.fromtimestamp(data["return_time"])

        if return_time <= departure_time:
            return JsonResponse({
                "message": "Return time cannot be before the departure time"
            }, status=400)

        dep_serializer = DepartureSerializer(data={
            "departure_time": departure_time,
            "departure_station_id": departure_obj.id,
            "departure_station_name": departure_obj.name_fi,
        })

        dep_db_obj = None
        if dep_serializer.is_valid():
            dep_db_obj = dep_serializer.save()
        else:
            print(dep_serializer.errors)
            return JsonResponse({
                "message": "An error occurred while inserting departure station info",
            }, status=400)

        ret_serializer = ReturnSerializer(data={
            "return_time": return_time,
            "return_station_id": return_obj.id,
            "return_station_name": return_obj.name_fi,
        })

        ret_db_obj = None
        if ret_serializer.is_valid():
            ret_db_obj = ret_serializer.save()
        else:
            print(ret_serializer.errors)
            return JsonResponse({
                "message": "An error occurred while inserting return station info",
            }, status=400)

        journey_db_obj = None
        journey_serializer = JourneySerializer(data={
            "departure_info": dep_db_obj.id,
            "return_info": ret_db_obj.id,
            "distance": data["distance"],
            "duration": data["duration"],
        })

        if journey_serializer.is_valid():
            journey_db_obj = journey_serializer.save()
            return JsonResponse({
                "message": "successfully inserted a journey."
            }, status=201)
        else:
            print(journey_serializer.errors)
            return JsonResponse({
                "message": "an error occurred while inserting a new journey!"
            }, status=201)
