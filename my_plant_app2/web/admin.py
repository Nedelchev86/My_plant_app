from django.contrib import admin

from my_plant_app2.web.models import Profile


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
