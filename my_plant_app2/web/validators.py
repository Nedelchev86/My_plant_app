from django.core.exceptions import ValidationError


def validate_firs_letter(value):
    print(value[0])
    if value[0].upper() != value[0]:
        raise ValidationError("Your name must start with a capital letter!")


def validate_only_letter(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Plant name should contain only letters!")