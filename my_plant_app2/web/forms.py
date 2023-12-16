from django import forms

from my_plant_app2.web.models import Profile, Plant


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("picture",)
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"

class CreatePlant(PlantBaseForm):
    pass


class EditPlant(PlantBaseForm):
    pass