from django.urls import path

from . import views

urlpatterns = [
    path("hello/<slug:name>", views.hello),
    path("hi/<str:name>/<str:last_name>", views.hi),  # hi(name)
    path("", views.index),
]
