from ops.models import Station, DepartureInfo, ReturnInfo, Journey
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


class DepartureSerializer(ModelSerializer):

    class Meta:
        model = DepartureInfo
        fields = "__all__"


class ReturnSerializer(ModelSerializer):

    class Meta:
        model = ReturnInfo
        fields = "__all__"


class JourneySerializer(ModelSerializer):

    class Meta:
        model = Journey
        fields = "__all__"
