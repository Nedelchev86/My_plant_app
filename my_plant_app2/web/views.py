from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home-page.html")


def profile_create(request):
    pass

def profile_details(request):
    pass


def profile_edit(request):
    pass

def profile_delete(request):
    pass


def catalogue(request):
    pass

def create_plant(request):
    pass

def edit_plant(request, pk):
    pass

def delete_plant(request, pk):
    pass


def details_plant(request, pk):
    pass