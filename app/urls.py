from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('room1/', views.room1, name='room1'),
    path('room2/', views.room2, name='room2'),
    path('room3/', views.room3, name='room3'),
    path('room4/', views.room4, name='room4'),
    path('room5/', views.room5, name='room5'),



]