from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Index|A proopos")
    return render(request, "publicsite/about.html")


def experience(request):
    return render(request, "publicsite/experience.html")


def blog(request):
    return render(request, "publicsite/blog.html")
