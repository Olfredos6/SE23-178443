from django.urls import path

from . import views

urlpatterns = [path("<slug:text>", views.echo)]
