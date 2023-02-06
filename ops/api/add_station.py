from django.views import View
from django.http import JsonResponse
from ops.models import Station
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# @method_decorator(csrf_exempt, name='dispatch')
class AddStation(View):

    def post(self, request, *args, **kwargs):
        """_summary_
        API to add a new station on the list
        Args:
            request (_type_): _description_
        """
        print(request)

        return JsonResponse({
            "hello": "World",
        })
