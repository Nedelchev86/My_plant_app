from django.shortcuts import render, redirect

from my_plant_app2.web.forms import CreateProfile
from my_plant_app2.web.models import Profile


# Create your views here.

def index(request):
    profile = Profile.objects.first()

    context = {
        "profile": profile
    }
    return render(request, "home-page.html", context)


def profile_create(request):
    if request.method == "GET":
        form = CreateProfile()
    else:
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
    }
    return render(request, "profile/create-profile.html", context)

def profile_details(request):
    pass


def profile_edit(request):
    pass

def profile_delete(request):
    pass


def catalogue(request):
    return render(request, "common/catalogue.html")

def create_plant(request):
    pass

def edit_plant(request, pk):
    pass

def delete_plant(request, pk):
    pass


def details_plant(request, pk):
    pass