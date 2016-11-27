from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Test

import datetime

# Create your views here.

def index(request):
    tests_name = [obj.name for obj in Test.objects.all()]
    return render(request, "index.html", {"list_test": tests_name})