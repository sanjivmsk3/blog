from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from content.models import *

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ('user',)