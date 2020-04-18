from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail_page'),
    path('rooms', views.room_list, name="room_page"),
    path('teachers', views.teacher_list, name="teacher_page"),
    path('new_meeting', views.new_meeting, name='new_meeting_page'),
    path('add_room', views.new_room, name="add_room_page"),
    path('add_teacher', views.new_teacher, name='add_teacher_page'),
    path('lesson', views.LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/<pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('lesson/<pk>/update', views.LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/<pk>/delete', views.LessonDeleteView.as_view(), name='lesson-delete'),
    path('teacher', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/<pk>/update', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<pk>/delete', views.TeacherDeleteView.as_view(), name='teacher-delete'),
    path('room', views.RoomCreateView.as_view(), name='room-create'),
    path('room/<pk>', views.RoomDetailView.as_view(), name='room-detail'),
    path('room/<pk>/update', views.RoomUpdateView.as_view(), name='room-update'),
    path('room/<pk>/delete', views.RoomDeleteView.as_view(), name='room-delete')
]
