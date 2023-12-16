
from django.contrib import admin
from django.urls import path, include

from my_plant_app2.web.views import index, profile_create, profile_details, profile_edit, profile_delete, catalogue

urlpatterns = [
 path("", index, name="home page"),
 path('profile/', include([
  path('create/', profile_create, name="create profile"),
  path('details/', profile_details, name="details profile"),
  path('edit/', profile_edit , name="edit profile"),
  path('delete/', profile_delete, name="delete profile"),
 ])),
 path("catalogue/", catalogue, name="catalogue"),

]

