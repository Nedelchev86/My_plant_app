
from django.contrib import admin
from django.urls import path, include

from my_plant_app2.web.views import index, profile_create, profile_details, profile_edit, profile_delete, catalogue, \
    create_plant, details_plant, edit_plant, delete_plant

urlpatterns = [
    path("", index, name="home page"),
    path('profile/', include([
        path('create/', profile_create, name="create profile"),
        path('details/', profile_details, name="details profile"),
        path('edit/', profile_edit , name="edit profile"),
        path('delete/', profile_delete, name="delete profile"),
        ])),
    path('catalogue/', catalogue, name="catalogue"),
    path('create/', create_plant, name="create plant"),
    path('details/<int:pk>/', details_plant, name="details plant"),
    path('edit/<int:pk>/', edit_plant, name="edit plant"),
    path('delete/<int:pk>/', delete_plant, name="delete plant"),

]
