# properties/views.py
from django.http import JsonResponse
from .models import Property

def property_list(request):
    properties = Property.objects.all().values(
        "id", "title", "price", "location"
    )  # pick fields you want
    return JsonResponse(list(properties), safe=False)
