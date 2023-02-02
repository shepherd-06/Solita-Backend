from django.urls import path

from ops.scripts.stations import Station
from ops.scripts.rides import Rides
from ops.views import index

from ops.api.station import GetStation
from ops.api.single_station import SingleStationView

urlpatterns = [
    path('station/', SingleStationView.as_view()),
    path('get_station/', GetStation.as_view()),
    path('', index, name="index"),
]
