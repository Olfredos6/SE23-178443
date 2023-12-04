from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-app/", include("hello_app.urls")),
    path("echo-app/", include("echo_app.urls")),
    path("calc/", include("calculator.urls")),
]
