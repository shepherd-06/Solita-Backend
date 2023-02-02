from django.views import View
from django.http import JsonResponse
from ops.models import Journey
from django.core.paginator import Paginator
from datetime import timedelta


class GetJourney(View):

    """
    return all journey, hard coded pagination
    per page item: 20 or (10)
    """

    def get(self, request):
        page_number = request.GET.get("page", 1)
        per_page = 20
        all_journey = Journey.objects.all()\
            .order_by('departure_info__departure_time')

        paginator = Paginator(all_journey, per_page)
        page_obj = paginator.get_page(page_number)

        data = list()
        for item in page_obj.object_list:
            data.append({
                "departure_time": item.departure_info.departure_time.strftime('%s'),
                "departure_station": item.departure_info.departure_station_name,
                "return_time": item.return_info.return_time.strftime('%s'),
                "return_station": item.return_info.return_station_name,
                "distance": item.distance / 1000.0,
                "duration": timedelta(seconds=item.duration),
            })

        return JsonResponse({
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": data
        })
