import csv
from dateutil.parser import parse
from django.views import View
from django.http import JsonResponse
from ops.serializer import (ReturnSerializer,
                            DepartureSerializer,
                            JourneySerializer)
from ops.models import Station


class Rides(View):

    """
    This API has to be called after the Station API. Otherwise it will fail.
    SIMPLE!
    This will parse all the locally stored csv's (3) and insert their data
    after validation.

    If this API is run twice, it will insert duplicate data in the database.
    IN development phase, I am using this API, i might do something else 
    for one-time only thing after production deployment.
    """

    def get(self, request):
        filenames = [
            "2021-05.csv",
            "2021-06.csv",
            "2021-07.csv",
        ]
        TEN_SECONDS = 10000
        total = 0
        for filename in filenames:
            count = 1
            with open('static/{}'.format(filename), mode='r') as file:
                csvFile = csv.reader(file)
                # displaying the contents of the CSV file

                for lines in csvFile:
                    if count == 1:
                        # skip the first item, col data
                        pass
                    else:
                        departure_info = {
                            "departure_time": parse(lines[0]),
                            # this is a station obj
                            "departure_station_id": lines[2],
                            "departure_station_name": lines[3]
                        }

                        return_info = {
                            "return_time": parse(lines[1]),
                            "return_station_id": lines[4],
                            "return_station_name": lines[5],
                        }
                        if lines[6] != '':
                            try:
                                distance = float(lines[6])
                            except ValueError:
                                # 0 value will not pass the if check
                                distance = 0

                        if lines[7] != '':
                            try:
                                time = int(lines[7])
                            except ValueError:
                                # 0 value will not pass the if check
                                time = 0

                        if time >= TEN_SECONDS and distance >= 10:
                            # get departure station info
                            dep_flag = False
                            ret_flag = False
                            try:
                                departure_station = Station.objects.get(
                                    station_id=departure_info["departure_station_id"])
                                departure_info["departure_station_id"] = departure_station.id
                            except Station.DoesNotExist:
                                print("departure_station does not exist. {}-{}".format(
                                    departure_info["departure_station_id"],
                                    departure_info["departure_station_name"],
                                ))
                                dep_flag = True

                            # get return station info
                            try:
                                return_station = Station.objects.get(
                                    station_id=return_info["return_station_id"])
                                return_info["return_station_id"] = return_station.id
                            except Station.DoesNotExist:
                                print("return_station does not exist. {}-{}".format(
                                    return_info["return_station_id"],
                                    return_info["return_station_name"],
                                ))
                                ret_flag = True

                            if not dep_flag and not ret_flag:
                                # both has to be True
                                dep_serializer = DepartureSerializer(
                                    data=departure_info)
                                if dep_serializer.is_valid():
                                    # departure_object will be used to store journey info
                                    departure_object = dep_serializer.save()

                                    ret_serializer = ReturnSerializer(
                                        data=return_info)

                                    if ret_serializer.is_valid():
                                        # this object will be used to store journey info
                                        ret_object = ret_serializer.save()

                                        # Store Journey Object here
                                        data = {
                                            "departure_info": departure_object.id,
                                            "return_info": ret_object.id,
                                            "distance": distance,
                                            "duration": time,
                                        }

                                        jour_serializer = JourneySerializer(
                                            data=data)

                                        if jour_serializer.is_valid():
                                            obj = jour_serializer.save()
                                            print(
                                                "Inserted data! -> {}".format(obj))
                                            total += 1
                                        else:
                                            print(jour_serializer.errors)
                                    else:
                                        print(return_info["return_station_id"],
                                              return_info["return_station_name"],
                                              ret_serializer.errors)
                                else:
                                    print(departure_info["departure_station_id"],
                                          departure_info["departure_station_name"],
                                          dep_serializer.errors)
                    count += 1

        return JsonResponse({
            "message": "Journey Data insertion from CSV",
            "station": total,
            "status": 200,
        }, status=200)
