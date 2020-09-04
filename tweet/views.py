from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import NewTweet
from .models import Tweets
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
import re
# Create your views here.
@login_required(login_url='/users/login')
def new_tweet(request):

    if request.method == "POST":
        form = NewTweet(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                new_tweet = Tweets.objects.create(
                    tweet=data.get('tweet'),
                    tweeter = request.user
                )
                if data.get('tweet').find('@'):
                    pattern = re.compile(r'@')
                    contents = data.get('tweet')
                    matches = pattern.finditer(contents)
                    for match in matches:
                        index=match.span()
                        atter = contents[index[1]::]
                        atter_instance = TwitterUser.objects.filter(username=atter).first()
                        Notification.objects.create(
                            atted_person=atter_instance,
                            the_tweet=new_tweet
                        )
                
                return HttpResponseRedirect(reverse('home'))
               
    form = NewTweet()
    return render(request, 'genericform.html', {'form': form} )




def tweet_detail(request, tweet_id):
    tweet = Tweets.objects.filter(id=tweet_id).first()
    return render(request, 'tweetdetail.html', {'tweet': tweet})

def follow(request, user_id):
    user_to_follow = TwitterUser.objects.filter(id=user_id).first()
    user_to_follow.following.add(request.user.id)
    return HttpResponseRedirect(reverse('home'))