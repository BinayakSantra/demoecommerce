from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Subcategorie
import json

def get_subcategory(request):
    id = request.GET.get('id','')
    result = [u.__dict__ for u in Subcategorie.objects.filter(category_id_id=id)]
    return HttpResponse(json.dumps(result), content_type="application/json")
