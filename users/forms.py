from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserUpdateForm(forms.ModelForm):
    #   email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'address', 'p_number']
        labels = {'p_number': 'Mobile Number', 'email': 'Email Address'}


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'p_number', 'password1', 'password2']
        labels = {'p_number': 'Mobile Number', 'email': 'Email Address'}
