from django.http import HttpResponse


def echo(request, text):
    return HttpResponse(text)
