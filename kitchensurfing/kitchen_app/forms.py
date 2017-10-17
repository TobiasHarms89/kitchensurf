from django import forms
from django.contrib.auth.models import User
from kitchen_app.models import UserProfileInfo, Events

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
