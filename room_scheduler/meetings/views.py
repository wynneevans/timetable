from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.forms import modelform_factory
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .models import Meeting, Room, Teacher, Lesson
from .forms import MeetingForm, LessonForm #, TeacherForm, RoomForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room_list(request):
    return render(request, "meetings/room_list.html", {"rooms": Room.objects.all()})


def teacher_list(request):
    return render(request, "meetings/teacher_list.html", {"teachers": Teacher.objects.all()})


TeacherForm = modelform_factory(Teacher, exclude=[])
RoomForm = modelform_factory(Room, exclude=[])


def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else: # request.method == "GET"
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


def new_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else: # request.method == "GET"
        form = TeacherForm()
    return render(request, "meetings/new_teacher.html", {"form": form})


def new_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else: # request.method == "GET"
        form = RoomForm()
    return render(request, "meetings/new_room.html", {"form": form})


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'meetings/lesson.html'
    form = LessonForm()

    def post(self, request, *args, **kwargs):
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = self.get_object()
            form.instance.post = lesson
            form.save()
            return redirect(reverse("lesson-detail", kwargs={'pk': lesson.pk}))


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'meetings/lesson_create.html'
    form_class = LessonForm

    def form_valid(self, form):
        form.save()
        #return redirect(reverse("lesson-detail", kwargs={'pk': form.instance.pk}))
        return redirect(reverse("welcome"))


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'meetings/lesson_create.html'
    form_class = LessonForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse("welcome"))


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = "meetings/lesson_confirm_delete.html"
    success_url = '/'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'meetings/teacher.html'
    form = TeacherForm()

    def post(self, request, *args, **kwargs):
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = self.get_object()
            form.instance.post = teacher
            form.save()
            return redirect(reverse("teacher-detail", kwargs={'pk': teacher.pk}))


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'meetings/teacher_create.html'
    form_class = TeacherForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse("welcome"))


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'meetings/teacher_create.html'
    form_class = TeacherForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse("welcome"))


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "meetings/teacher_confirm_delete.html"
    success_url = '/'


class RoomDetailView(DetailView):
    model = Room
    template_name = 'meetings/room.html'
    form = RoomForm()

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = self.get_object()
            form.instance.post = room
            form.save()
            return redirect(reverse("room-detail", kwargs={'pk': room.pk}))


class RoomCreateView(CreateView):
    model = Room
    template_name = 'meetings/room_create.html'
    form_class = RoomForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse("welcome"))


class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'meetings/room_create.html'
    form_class = RoomForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse("welcome"))


class RoomDeleteView(DeleteView):
    model = Room
    template_name = "meetings/room_confirm_delete.html"
    success_url = '/'

