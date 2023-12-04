from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login),
    path("hello/<slug:name>", views.hello),
    path("hello-json", views.hello_json),
    path("hi/<str:name>/<str:last_name>", views.hi),  # hi(name)
    path("", views.index),
]
