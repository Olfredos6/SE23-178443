import json
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

EXPERIENCE_DATA_FILE = Path(
    settings.BASE_DIR / "publicsite" / "data" / "experience.json"
)


def index(request):
    # return HttpResponse("Index|A proopos")
    return render(request, "publicsite/about.html", {})


def experience(request):
    with open(EXPERIENCE_DATA_FILE, "r", encoding="utf-8") as f:
        experience_data = json.loads(f.read())["experiences"]

    return render(
        request, "publicsite/experience.html", {"maman": experience_data, "manuel": 46}
    )


def blog(request):
    return render(request, "publicsite/blog.html")


def test_layout(request):
    return render(request, "publicsite/layout.html")
