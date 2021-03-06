from django.shortcuts import render, get_object_or_404
from .models import Meeting


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "Meetings/detail.html", { "meeting": meeting})
