from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("experience/", views.experience),
    path("blog/", views.blog),
]
