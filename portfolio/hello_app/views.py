from django.http import HttpResponse


def hello(request, name):
    return HttpResponse(f"Bonjour, {name}!")


def hi(request, name, last_name):
    print("~~~~>", request)
    print("~~~~>", name)
    return HttpResponse(f"Salut, {name} {last_name}!")


def index(request):
    return HttpResponse(f"<h1>Bienvenue!</h2>")
