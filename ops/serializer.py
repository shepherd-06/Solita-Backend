from ops.models import Station
from rest_framework.serializers import ModelSerializer


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = ("station_id",
                  "name_fi",
                  "name_sw",
                  "name_en",
                  "address_fi",
                  "address_en",
                  "city_fi",
                  "city_sw",
                  "operator",
                  "capacity",
                  "coordinate_x",
                  "coordinate_y")
