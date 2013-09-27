from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from models import *

@csrf_exempt
def home(request):
    now = datetime.datetime.now()
    c = Context({'current_date': now})

    config = PurpleRobotConfigTemplate.objects.all()[0]
    c['config'] = config

    return render_to_response('home.html', c)
