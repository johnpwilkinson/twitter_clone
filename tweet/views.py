from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import NewTweet
from .models import Tweets
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.shortcuts import get_object_or_404
import re
from django.views.generic import DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# @login_required(login_url='/users/login')
# def new_tweet(request):

#     if request.method == "POST":
#         form = NewTweet(request.POST)
#         if form.is_valid():
#                 data = form.cleaned_data
#                 new_tweet = Tweets.objects.create(
#                     tweet=data.get('tweet'),
#                     tweeter = request.user
#                 )
#                 if data.get('tweet').find('@'):
#                     pattern = re.compile(r'@')
#                     contents = data.get('tweet')
#                     matches = pattern.finditer(contents)
#                     for match in matches:
#                         index=match.span()
#                         atter = contents[index[1]::]
#                         atter_instance = TwitterUser.objects.filter(username=atter).first()
#                         Notification.objects.create(
#                             atted_person=atter_instance,
#                             the_tweet=new_tweet
#                         )
                
#                 return HttpResponseRedirect(reverse('home'))
               
#     form = NewTweet()
#     return render(request, 'genericform.html', {'form': form} )

class NewTweet(LoginRequiredMixin, View):
    form_class = NewTweet
    initial = {'key': 'value'}
    template_name = 'genericform.html'
    login_url = '/users/login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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
        return render(request, self.template_name, {'form': form})

# def tweet_detail(request, tweet_id):
#     tweet = Tweets.objects.filter(id=tweet_id).first()
#     return render(request, 'tweetdetail.html', {'tweet': tweet})

class TweetDetailView(ListView):
    model = Tweets
    template_name = 'tweetdetail.html'
    context_object_name = 'tweet'

    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get('tweet_id')
        return Tweets.objects.filter(id=tweet_id).first()

   

def follow(request, user_id):
    user_to_follow = TwitterUser.objects.filter(id=user_id).first()
    user_to_follow.following.add(request.user.id)
    return HttpResponseRedirect(reverse('home'))