from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'team']
        labels = {
            'username': _('Username'),
            'email': _('Email Address'),
            'role': _('Role'),
            'team': _('Team')
        }
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'email': 'Required. Enter a valid email address.',
            'role': 'Select the role for the user.',
            'team': 'Select the team for the user.'
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'team']