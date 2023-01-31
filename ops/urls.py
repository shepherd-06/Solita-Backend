from django.urls import path

from ops.scripts.stations import Station
from ops.scripts.rides import Rides
from ops.views import index

urlpatterns = [
    path('station', Station.as_view()),
    path('journey', Rides.as_view()),
    path('', index, name="index"),
]
