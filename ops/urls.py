from django.urls import path

from ops.scripts.script_rides import ScriptRides
from ops.scripts.script_stations import ScriptStation

from ops.api.station import GetStation
from ops.api.single_station import SingleStationView
from ops.api.journey import GetJourney

urlpatterns = [
    path('station/', SingleStationView.as_view()),
    path('get_station/', GetStation.as_view()),
    path('get_journey/', GetJourney.as_view()),

    path('script/rides', ScriptRides.as_view()),
    path('script/station', ScriptStation.as_view()),
]
