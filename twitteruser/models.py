from django.contrib.auth.models import AbstractUser
from django.db import models
from twitterclone import settings




# Create your models here.
class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length= 50, null=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(blank=True, null=True)
    homepage = models.URLField(null=True)    
    following = models.ManyToManyField("self", related_name="followers", 
                                   symmetrical=False, null=True)
    

    def __str__(self):
        return self.username