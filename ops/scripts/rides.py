import csv

from django.views import View
from django.http import JsonResponse
from ops.serializer import StationSerializer


class Rides(View):

    """
    This API has to be called after the Station API. Otherwise it will fail.
    SIMPLE!
    This will parse all the locally stored csv's (3) and insert their data
    after validation.

    If this API is run twice, it will insert duplicate data in the database.
    IN development phase, I am using this API, i might do something else 
    for one-time only thing after production deployment.
    """

    def get(self, request):
        pass
