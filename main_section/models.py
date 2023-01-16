from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    Subject = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)

