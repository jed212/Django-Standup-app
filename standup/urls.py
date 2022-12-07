from django.urls import path

from . import views

urlpatterns = [
    path('', views.Updates, name = 'Updates'),
]