from django.shortcuts import render, redirect

from my_plant_app2.web.forms import CreateProfile, CreatePlant, EditPlant, DeletePlant, EditProfile, DeleteProfil
from my_plant_app2.web.models import Profile, Plant


# Create your views here.

def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    else:
        return None


def index(request):
    profile = get_profile()

    context = {
        "profile": profile,
        "do_not_show": True,
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
        "do_not_show": True,
    }
    return render(request, "profile/create-profile.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    plants = len(Plant.objects.all())

    context = {
        "profile": profile,
        "plants": plants
    }

    return render(request, "profile/profile-details.html", context)

def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = EditProfile(instance=profile)

    else:
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("details profile")
    context = {
        "form": form,
    }

    return render(request, "profile/edit-profile.html", context)


def profile_delete(request):

    profile = Profile.objects.first()
    if request.method == "GET":
        form = DeleteProfil(instance=profile)
    else:
        form = DeleteProfil(instance=profile)
        form.save()
        return redirect("home page")

    context = {
        "form": form,

    }

    return render(request, "profile/delete-profile.html", context)


def catalogue(request):
    plants = Plant.objects.all()
    profile = Profile.objects.first()
    context = {
        "plants": plants,
        "profile": profile
    }
    return render(request, "common/catalogue.html", context)


def create_plant(request):
    if request.method == "GET":
        form = CreatePlant()
    else:
        form = CreatePlant(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form
    }
    return render(request, "plant/create-plant.html", context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == "GET":
        form = EditPlant(instance=plant)
    else:
        form = EditPlant(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
        "plant": plant
    }

    return render(request, "plant/edit-plant.html", context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == "GET":
        form = DeletePlant(instance=plant)
    else:
        form = DeletePlant(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        "form": form,
        "plant": plant
    }

    return render(request, "plant/delete-plant.html", context)


def details_plant(request, pk):
    plant = Plant.objects.get(pk=pk)

    context = {
        "plant": plant
    }

    return render(request, "plant/plant-details.html", context)