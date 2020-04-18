from datetime import time
from django.db import models
from django.shortcuts import reverse


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} in room {self.room_number} on floor {self.floor_number}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.subject}"


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} by {self.teacher}"

    #def get_absolute_url(self):
    #    return reverse('welcome', kwargs={'pk': self.pk})


class Class(models.Model):
    name = models.CharField(max_length=100)
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


#class Timetable(models.Model):
#    name = models.CharField(max_length=100)
#    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
#    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

#    def __str__(self):
#        return f"{self.name}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
