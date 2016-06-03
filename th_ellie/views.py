from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed

from django.core.cache import caches
import json
 


def save_to_cache(obj):
    # obj: {"title": title, "description": description}
    cache = caches["th_ellie"]
    if 'tasks' in cache:
        cached = cache.get('tasks')
        cached.append(obj)
        cache.set('tasks', cached)
    else:
        proj_name_list = []
        proj_name_list.append(obj)
        cache.set('tasks', proj_name_list)


# Create your views here.
def send_name_to_github(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        try:
            task = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest()

        if not isinstance(task, dict):
            return HttpResponseBadRequest()
        if "title" not in task.keys() or "description" not in task.keys():
            return HttpResponseBadRequest()
        if not isinstance(task["title"], str) or not isinstance(task["description"], str):
            return HttpResponseBadRequest()
        
        save_to_cache(json.loads(request.body.decode('utf-8')))

        return HttpResponse("Task  %s." % request.body.decode('utf-8'))
    else:
        return HttpResponseNotAllowed(["POST"])