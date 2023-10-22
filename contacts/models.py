from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.


class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=19)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
    
    
    
