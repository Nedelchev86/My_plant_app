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


class DeletePlant(PlantBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super(DeletePlant, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
            
    def save(self, commit=True):
        if commit:
            self.instance.delete()

