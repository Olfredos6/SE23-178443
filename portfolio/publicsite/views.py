import json
from datetime import date
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from . import models

EXPERIENCE_DATA_FILE = Path(
    settings.BASE_DIR / "publicsite" / "data" / "experience.json"
)


def index(request):
    # return HttpResponse("Index|A proopos")
    return render(request, "publicsite/about.html", {})


def experience(request):
    with open(EXPERIENCE_DATA_FILE, "r", encoding="utf, 8") as f:
        experience_data = json.loads(f.read())["experiences"]

    def process_experience(experience):
        experience["start_date"] = date.fromisoformat(
            "-".join(reversed(experience["start_date"].split("-")))
        )
        if experience["end_date"]:
            experience["end_date"] = date.fromisoformat(
                "-".join(reversed(experience["end_date"].split("-")))
            )
        return experience

    experience_data = list(map(lambda x: process_experience(x), experience_data))

    return render(
        request,
        "publicsite/experience.html",
        {"experience_data": experience_data, "count": len(experience_data)},
    )


def blog(request):
    posts = models.Post.objects.all()
    return render(request, "publicsite/blog.html", {"posts": posts})


def test_layout(request):
    return render(request, "publicsite/layout.html")
