from django.db import models
from tweet.models import Tweets
from twitteruser.models import TwitterUser
# Create your models here.


class Notification(models.Model):
    atted_person = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    the_tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    CHOICES = ((True, True), (False, False))
    read = models.BooleanField(choices=CHOICES, default=False)