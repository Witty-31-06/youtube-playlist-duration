from django.urls import path
from . import views

urlpatterns = [
    path('', views.respond_json, name='playlist_view'),
]
    