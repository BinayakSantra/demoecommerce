from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Subcategorie
import json


def get_subcategory(request):
    id = request.GET.get('id','')
    result = list(Subcategorie.objects.filter(category_id_id=int(id)).values('id', 'display_name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
