from django.urls import path

from ops.api.station import GetStation
from ops.api.single_station import SingleStationView
from ops.api.journey import GetJourney
from ops.api.add_station import AddStation

urlpatterns = [
    path('station/', SingleStationView.as_view()),
    path('get_station/', GetStation.as_view()),
    path('add_station/', AddStation.as_view()),

    path('get_journey/', GetJourney.as_view()),
]
