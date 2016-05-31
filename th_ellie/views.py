from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def send_name_to_github(request, proj_name):
    
    return HttpResponse("Hello  %s." % proj_name)
    #return HttpResponse("You're looking at question %s." % question_id)
