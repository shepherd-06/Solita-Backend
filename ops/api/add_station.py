from django.http import JsonResponse
from ops.models import Station
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from ops.serializer import StationSerializer


# @method_decorator(csrf_exempt, name='dispatch')
class AddStation(APIView):

    def post(self, request):
        """_summary_
        API to add a new station on the list
        Args:
            request (_type_): _description_
        """
        data = request.data
        names = ["name_en", "name_fi", "name_sw"]
        flag = False

        for name in names:
            if name in data:
                flag = True

        if not flag:
            return JsonResponse({
                "message": "at least one station name is required",
                "options": names,
            }, status=400)

        serializer = StationSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return JsonResponse({
                "message": "{} station created".format(obj)
            }, status=201)
        else:
            return JsonResponse({
                "message": serializer.errors,
            }, status=400)
