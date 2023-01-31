from django.urls import path

from ops.scripts.stations import Station

urlpatterns = [
    path('station', Station.as_view(), ),
]
