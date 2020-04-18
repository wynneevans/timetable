from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from meetings.models import Meeting, Teacher, Lesson, Room

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "teachers": Teacher.objects.all(),
                   "lessons": Lesson.objects.all(),
                   "rooms": Room.objects.all()})

#def teacher(request):
#    return render(request, "website/welcome.html", {"teachers": Teacher.objects.all()})

#def date(request):
#    return HttpResponse("This page was served at " + str(datetime.now()))

#def about(request):
#    return HttpResponse("My name is Wynne")