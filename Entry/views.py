# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from Entry.models import *

import requests


def index(request):
    return HttpResponse("hello world")


def upload(request):
    json_work_req = None
    json_color_req = None1
    if settings.DEBUG:
        json_req = requests.get('http://dev.miguelbermudez.com/dev/artdata/test.json')
        json_color_req = requests.get('http://dev.miguelbermudez.com/dev/artdata/test_color.json')

    for line in json_req.iter_lines():
        if line:
            return HttpResponse(line, content_type="application/json")


    #return HttpResponse(json_color_req, content_type="application/json")
