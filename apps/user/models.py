from django.db import models
from django.utils.timezone import now
# from common.validators import mobile_length_validator, mobile_validator, validate_not_empty
import hashlib

# from django_extensions.db.fields import AutoSlugField

import re
from django.core.exceptions import ValidationError


class User(models.Model):
    """
    This class represents a User of the website, it inherits from AbstractUser
    The variables are self-commented.
    """
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField('gender', max_length=1, choices=[('F', 'female'), ('M', 'male')], blank=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=10)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    friends = models.ManyToManyField("User", blank=True, null=True)
    created = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    # slug = AutoSlugField(populate_from=['email'], unique=True )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)  # Call the "real" save() method.
