from django.contrib import admin

from my_plant_app2.web.models import Profile, Plant


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Plant)
class AdminPlant(admin.ModelAdmin):
    pass
