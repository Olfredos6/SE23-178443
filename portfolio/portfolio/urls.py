from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-app/", include("hello_app.urls")),
    path("echo-app/", include("echo_app.urls")),
    # path("hello-app/hello/", hello_app.views.hello),
    # path("hello-app/hi/", hello_app.views.hi),
    # https://127.0.0.1:8000
    # hello-app/
    # hi
    # hello-app/hello/Manuel
    # hello/Manuel
    # hello-app/
    # hi/Manuel
]
