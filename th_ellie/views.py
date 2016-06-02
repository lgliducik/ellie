from django.shortcuts import render
from django.http import HttpResponse

from django.core.cache import caches
 


# Create your views here.
def send_name_to_github(request, proj_name):
    if request.method == 'GET':
        cache = caches["th_ellie"]
        if 'tasks' in cache:
            cached = cache.get('tasks')
            cached.append(proj_name)
            cache.set('tasks', cached)
            print("1cache.get('tasks')", cache.get('tasks'))
        else:
            proj_name_list = []
            proj_name_list.append(proj_name)
            cache.set('tasks', proj_name_list)
            print("2cache.get('tasks')", cache.get('tasks'))
        
        #import pdb;pdb.set_trace()


    
    return HttpResponse("Hello  %s." % proj_name)
    #return HttpResponse("You're looking at question %s." % question_id)
