import csv
from dateutil.parser import parse
from django.views import View
from django.http import JsonResponse
from ops.serializer import (ReturnSerializer,
                            DepartureSerializer,
                            JourneySerializer)
from ops.models import Station
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    with open('static/2021-05.csv', mode='r') as file:
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        count = 1
        print("takku suru!")
        for lines in csvFile:
            if count == 10:
                print("Break?")
                break
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
                distance = float(lines[6])
                time = int(lines[7])
                try:
                    departure_station = Station.objects.get(
                        station_id=departure_info["departure_station_id"])
                    departure_info["departure_station_id"] = departure_station.id
                except Station.DoesNotExist:
                    print("departure_station does not exist.")

                # get return station info
                try:
                    return_station = Station.objects.get(
                        station_id=return_info["return_station_id"])
                    return_info["return_station_id"] = return_station.id
                except Station.DoesNotExist:
                    print("return_station does not exist.")

                dep_serializer = DepartureSerializer(
                    data=departure_info)
                if dep_serializer.is_valid():

                    dep_object = dep_serializer.save()

                    ret_serializer = ReturnSerializer(
                        data=return_info)

                    if ret_serializer.is_valid():
                        ret_obj = ret_serializer.save()

                        # Store Journey Object here
                        data = {
                            "departure_info": dep_object.id,
                            "return_info": ret_obj.id,
                            "distance": distance,
                            "duration": time,
                        }

                        jour_serializer = JourneySerializer(
                            data=data)

                        if jour_serializer.is_valid():
                            jour_serializer.save()
                            print("Inserted 1 data!")
                        else:
                            print(jour_serializer.errors)
                    else:
                        print(ret_serializer.errors)
                else:
                    print(dep_serializer.errors)

            count += 1
    return HttpResponse(html)
