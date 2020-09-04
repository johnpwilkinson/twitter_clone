from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.models import Tweets
from notification.models import Notification
from django.db.models import Q

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
                form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    form = CustomUserCreationForm()
    return render(request, 'genericform.html', {'form': form})

@login_required(login_url='/users/login')
def index(request):
    tweeter = TwitterUser.objects.get(id=request.user.id)
    myfollowers = tweeter.followers.all()
    followingTweets = []
    mytweets = Tweets.objects.filter(tweeter=request.user)
    if mytweets:
        for myeach in mytweets:
                followingTweets.append(myeach)
    for each in myfollowers:
        ftweets = Tweets.objects.filter(tweeter=each)
        if len(ftweets) > 0:
            for feach in ftweets:
                followingTweets.append(feach)
    followingTweets = sorted(followingTweets, key=lambda x: x.submission_time)
    notif_count = Notification.objects.filter(atted_person=request.user.id, read=False).count()
    return render(request, 'home.html', {'feed': followingTweets, 'notifs': notif_count})

def user_detail_view(request, user_name):
    tweeter = TwitterUser.objects.filter(username=user_name).first()
    count = Tweets.objects.filter(tweeter=tweeter).count
    return render(request, 'tweeterdetail.html', {'tweeter': tweeter, 'count': count})
