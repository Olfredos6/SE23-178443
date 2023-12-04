from django.urls import path

from . import views

urlpatterns = [
    path("add/<int:a>/<int:b>", views.add),
    path("substract/<int:a>/<int:b>", views.substract),
    path("divide/<int:a>/<int:b>", views.divide),
    path("multiply/<int:a>/<int:b>", views.multiply),
    path("square/<int:value>", views.square),
]
