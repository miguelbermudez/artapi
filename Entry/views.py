# Create your views here.
import json
import sys

from django.conf import settings
from django.http import HttpResponse
import requests

from Entry.models import *


#referenced fields
referenced_color_fields = ['palette', 'dominantcolor', 'searchbycolors', 'mostsaturated', ]
referenced_text_fields = ['references', 'exhibitionHistory', 'notes']
work_keys = ["id", "accessionNumber", "artist", "catalogueEntry", "catalogueRaisonne", "classification", "creditLine", "culture", "date", "description", "designer", "dimensions", "dynasty", "galleryLabel", "geography", "imageUrl", "imgfilename", "markings", "medium", "period", "provenance", "reign", "rightsReproduction", "title", "workid", "workurl"]

def index(request):
    return HttpResponse("hello world")


def upload(request):
    json_req = None
    if settings.DEBUG:
        #json_req = requests.get('https://s3.amazonaws.com/metlinkdb/test.json')
        json_req = requests.get('https://s3.amazonaws.com/metlinkdb/embeeapi_work.json')           #real file

    counter = 1
    titles = []
    for line in json_req.iter_lines():
        if line:
            work_dict = json.loads(line)
            #work dict copy for new work model creation
            w = work_dict.copy()

            #clean up keys
            for k in w.keys():
                if k not in work_keys:
                    w.pop(k, None)

            #new work, wm = work model
            wm = Work(**w)
            wm.save()

            #start looping through fields for colors
            #and other ref fields
            for field in work_dict.keys():
                value = work_dict[field]

                if field in referenced_color_fields:
                    #loop through value which is a list of work_colors
                    for wc in value:
                        c = {'red': wc['red'], 'green': wc['green'], 'blue': wc['blue'],
                             'intvalue': wc['intvalue'],'hexvalue': wc['hexvalue']}

                        #create new color
                        wc, created = WorkColor.objects.get_or_create(**c)
                        #created is set to true if a new obj was created, in that case, do we need save()?
                        wc.save()

                        #create color to work join
                        getattr(wm, field).add(wc)

                if field in referenced_text_fields:
                    ref_text_model = None
                    if field == "exhibitionHistory":
                        ref_text_model = ExhibitionHistory()
                    if field == "notes":
                        ref_text_model = Notes()
                    if field == "references":
                        ref_text_model = References()

                    #loop through value which is a list of text ref fields, ti = text item
                    for ti in value:
                        #create new entry for text ref field
                        setattr(ref_text_model, 'entry', ti)
                        setattr(ref_text_model, 'work', wm)
                        ref_text_model.save()

            titles.append("#%s Work: %s" % (counter, work_dict['title']))
            sys.stdout.write("#%s Work: %s         \r" % (counter, work_dict['title']))
            sys.stdout.flush()
            counter += 1

    return HttpResponse(json.dumps(titles), content_type="application/json")
