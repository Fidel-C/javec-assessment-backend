from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

# Create your models here.


class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)