from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail_page'),
    path('rooms', views.room_list, name="room_page"),
    path('new', views.new, name='new')
]