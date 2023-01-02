from django.core.validators import MinLengthValidator

from django.core import exceptions, validators
from django.db import models


def validate_if_starts_with_cap_letter(value):
    if not value[0].isupper():
        raise exceptions.ValidationError('Your name must start with a capital letter!')


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    MAX_LEN_USERNAME = 10

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(validators.MinLengthValidator(2), ),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=(validate_if_starts_with_cap_letter, ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=(validate_if_starts_with_cap_letter, ),
        null=False,
        blank=False,

    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):

    types_plant = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    type = models.CharField(
        max_length=14,
        choices=types_plant,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

