from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@gmail.com'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'e.g., Jhon'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'e.g., Kerry'}))
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
