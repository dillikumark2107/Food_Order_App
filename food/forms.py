from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Food


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove Django's default help messages
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'category']