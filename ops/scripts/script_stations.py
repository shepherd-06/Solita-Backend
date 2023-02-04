import csv

from django.views import View
from django.http import JsonResponse
from ops.serializer import StationSerializer


class ScriptStation (View):

    """
    This is a simple API
    If it ran the first time, it will try to insert all the data 
    from helsinki_station_list.csv file in the database.

    If it ran after initialization, it won't throw any error; but it won't
    insert either.

    This is a very expensive operation. It will try to insert every station details 
    in the database table.
    """

    def get(self, request):
        with open('static/helsinki_station_list.csv', mode='r') as file:
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            station = 0
            count = 1
            for lines in csvFile:
                if count == 1:
                    # skip the first item
                    pass
                else:
                    data = {
                        "station_id": lines[1],
                        "name_fi": lines[2],
                        "name_sw": lines[3],
                        "name_en": lines[4],
                        "address_fi": lines[5],
                        "address_en": lines[6],
                        "city_fi": lines[7],
                        "city_sw": lines[8],
                        "operator": lines[9],
                        "capacity": lines[10],
                        "coordinate_x": lines[11],
                        "coordinate_y": lines[12]
                    }
                    serializer = StationSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        station += 1
                    else:
                        print(serializer.errors)
                count += 1

        return JsonResponse({
            "message": "Data insertion from CSV",
            "station": station,
            "status": 200,
        }, status=200)
