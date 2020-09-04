from django.contrib import admin
from .models import TwitterUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('age', 'bio', 'display_name', 'homepage', 'following')}),
)


class TwitterUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = TwitterUser
    list_display = ['username','display_name', 'age', 'bio', 'homepage']

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


    

    

admin.site.register(TwitterUser, TwitterUserAdmin)