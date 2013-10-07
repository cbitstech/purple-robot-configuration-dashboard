from django.template import Context
from django.shortcuts import render_to_response
from models import *
from forms import ConfigurationForm
from django.core.context_processors import csrf
from django.http import HttpResponse
import json

def get_config(request):
    robouser = RoboUser.objects.filter(id = int(request.POST['user_id']))[0]
    try:
        config = Configuration.objects.filter(user = robouser)[0]
        results = config.json
        nickname = config.config_name
        config_id = config.id
        return HttpResponse(json.dumps({"json":results, "name":nickname, "id":config_id}), content_type="application/json")
    except IndexError:
        return HttpResponse(json.dumps({}), content_type="application/json")

def save_config(request):
    try:
        config = Configuration.objects.get(id=int(request.POST['id']))
        config.json = request.POST['json']
        config.config_name = request.POST['config_name']
        config.user = RoboUser.objects.filter(id=int(request.POST['user_id']))[0]
        config.save()
        results = { 'result': 'success' }
        return HttpResponse(json.dumps(results, indent=2), content_type="application/json")
    except Configuration.DoesNotExist:
        config = Configuration()
        config.json = request.POST['json']
        config.config_name = request.POST['config_name']
        config.user = RoboUser.objects.filter(id=int(request.POST['user_id']))[0]
        config.save()
        results = { 'result': 'success' }
        return HttpResponse(json.dumps(results, indent=2), content_type="application/json")

def home(request):
    c = Context()
    users = RoboUser.objects.all()
    studies = Study.objects.all()
    config = PurpleRobotConfigTemplate.objects.all()[0]
    c['config'] = config
    c['studies'] = studies
    c['users'] = users

    return render_to_response('home.html', c)
