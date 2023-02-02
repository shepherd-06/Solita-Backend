from django.views import View
from django.http import JsonResponse
from ops.models import Station
from django.core.paginator import Paginator


class GetStation(View):

    """
    Send Station Data with pagination
    default item per page = 10 (hard coded)
    """

    def get(self, request):
        page_number = request.GET.get("page", 1)
        per_page = 10
        all_stations = Station.objects.all().order_by('station_id')

        paginator = Paginator(all_stations, per_page)
        page_obj = paginator.get_page(page_number)

        data = list()
        for item in page_obj.object_list:
            data.append({
                "id": item.station_id,
                "name_fi": item.name_fi,
                "name_sw": item.name_sw,
                "name_en": item.name_en,
                "address_fi": item.address_fi,
                "address_en": item.address_en,
                "city_fi": item.city_fi,
                "city_sw": item.city_sw,
                "operator": item.operator,
                "capacity": item.capacity,
                "coordinate": {
                    "x": item.coordinate_x,
                    "y": item.coordinate_y,
                },
            })
        return JsonResponse({
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": data
        })
