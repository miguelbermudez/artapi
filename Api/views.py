# Create your views here.

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Entry.models import *
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



def color(request):
    # all_dominant_colors = []
    page = request.GET.get('page')

    for w in Work.objects.all():
        dcolor = w.dominantcolor
        # all_dominant_colors.append(dcolor)

    #paginator = Paginator(all_dominant_colors, 50)
    paginator = Paginator(Work.objects.all(), 50)

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
