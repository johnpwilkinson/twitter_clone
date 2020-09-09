"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from twitteruser import views as userviews
from tweet import views as tweetviews
from notification import views as notifviews
urlpatterns = [
    path('', userviews.index, name='home'),
    path('admin/', admin.site.urls),
    path('tweet/<slug:tweet_id>/', tweetviews.TweetDetailView.as_view(), name='tweet detail'),
    path('signup/', userviews.SignUpView.as_view(), name='signup'),
    path('user/<slug:user_name>/', userviews.UserDetailView.as_view(), name='user_detail'),
    path('users/', include('django.contrib.auth.urls')),
    path('tweet/', tweetviews.NewTweet.as_view(), name='tweet'),
    path('follow/<int:user_id>/', tweetviews.follow, name='follow'),
    path('notifications/', notifviews.notificationview, name='notifications'),
]
