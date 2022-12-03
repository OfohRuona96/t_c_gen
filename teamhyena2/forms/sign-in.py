from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signinform(UserCreationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    

    class meta:
        model = User
        fields = ('username', 'password')

        def save(self, comit=True):
           # User = super(signupform, self).save(commit=False)
            User.username = self.cleaned_data['username']
            User.password = self.cleaned_data['password']

            if comit:
                User.save
            return User