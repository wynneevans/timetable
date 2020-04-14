from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("My name is Wynne")