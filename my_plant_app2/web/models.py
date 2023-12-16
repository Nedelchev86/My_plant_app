from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app2.web.validators import validate_firs_letter, validate_only_letter


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)],
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=20,
        validators=[validate_firs_letter],
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=20,
        validators=[validate_firs_letter],
        null=False,
        blank=False,
    )
    picture = models.URLField(null=True, blank=True)


class Plant(models.Model):
    CHOICES = (
        ("Outdoor", "Outdoor Plants"),
        ("Indoor", "Indoor Plants"),
    )

    type = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        choices=CHOICES
    )

    name = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
            validate_only_letter
        ],
    )

    image = models.URLField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)