# Create your views here.
import json
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Entry.models import *
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
JSONSerializer = serializers.get_serializer("json")
json_serializer = JSONSerializer()

WORK_RETURN_NUMBER = 1000

def color(request):
    # all_dominant_colors = []
    page = request.GET.get('page')
    offset = int(page) * WORK_RETURN_NUMBER + 1 if page is not None else 0

    allworks = Work.objects.all().prefetch_related('dominantcolor')
    # allworks = Work.objects.all()
    # resultset = list(allworks[offset:offset+WORK_RETURN_NUMBER])
    # resultset = allworks[offset:offset+WORK_RETURN_NUMBER]
    resultset = list(allworks)
    # return HttpResponse(str(resultset))
    paginator = Paginator(resultset, WORK_RETURN_NUMBER)

    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        works = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        works = paginator.page(paginator.num_pages)

    context = {'works': works}
    return render(request, 'api/color.html', context)

# Create your views here.
def colorj(request):
    page = request.GET.get('page')
    paginator = Paginator(Work.objects.all(), 1000)

    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        works = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        works = paginator.page(paginator.num_pages)


    return HttpResponse(json_serializer.serialize(works.object_list), mimetype="application/json")