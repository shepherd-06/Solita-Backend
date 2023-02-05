from django.urls import path

from ops.api.station import GetStation
from ops.api.single_station import SingleStationView
from ops.api.journey import GetJourney

urlpatterns = [
    path('station/', SingleStationView.as_view()),
    path('get_station/', GetStation.as_view()),
    path('get_journey/', GetJourney.as_view()),
]
