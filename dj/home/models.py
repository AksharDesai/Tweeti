from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tweeters",null=True,blank=True)
    text = models.TextField( max_length=100)
    image = models.ImageField( upload_to='photos/',null=True , blank=True)
    
    def __str__(self):
        return self.text

class Comments(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")  # Link comment to user
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="comments")  # Link comment to tweet
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)