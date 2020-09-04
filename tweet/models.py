from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweets(models.Model):

    tweet = models.CharField(max_length=140)
    tweeter = models.ForeignKey(TwitterUser,related_name='ticket_owner', on_delete=models.CASCADE)
    submission_time = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return self.tweet