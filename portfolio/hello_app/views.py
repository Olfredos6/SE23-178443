from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def hello(request, name):
    return HttpResponse(f"Bonjour, {name}!")


def hi(request, name, last_name):
    print("~~~~>", dir(request))
    print("~~~~>", request.GET["search"])
    return HttpResponse(f"Salut, {name} {last_name}!")


def index(request):
    return HttpResponse(f"<h1>Bienvenue!</h2>")


def hello_json(request):
    return JsonResponse({"data": "Bonjour!"})


@csrf_exempt
def login(request):
    if request.method == "POST":  # [DELETE, POST, UPDATE]
        return HttpResponse("Fromulaire soumis")

    return HttpResponse(
        """<form action='/hello-app/login/' method='POST'>
            <input type='password' name='password' />
            <input type='submit' value='Ok'>
        </form>
        """
    )
