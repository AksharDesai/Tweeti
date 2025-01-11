from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    
    text = models.TextField( max_length=100)
    image = models.ImageField( upload_to='photos/',null=True , blank=True)
    
    def __str__(self):
        return self.text

