from django import forms

from my_plant_app2.web.models import Profile, Plant


class ProfileBase(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }



class CreateProfile(ProfileBase):
    class Meta:
        model = Profile
        exclude = ("picture",)


class EditProfile(ProfileBase):
    pass

class DeleteProfil(ProfileBase):
    def save(self, commit=True):
        self.instance.delete()


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

