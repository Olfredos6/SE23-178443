from django.http import HttpResponse


def add(request, a, b):
    return HttpResponse(f"Result: \n{a}+{b}={a+b}")


def substract(request, a, b):
    return HttpResponse(f"Result: \n{a}-{b}={a-b}")


def divide(request, a, b):
    return HttpResponse(f"Result: \n{a}/{b}={a/b}")


def multiply(request, a, b):
    return HttpResponse(f"Result: \n{a}x{b}={a*b}")


def square(request, value):
    return HttpResponse(f"Result: \n{value}-{value}={value*value}")
