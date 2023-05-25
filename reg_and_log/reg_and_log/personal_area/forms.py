from django import forms
from .models import User1


class Register(forms.ModelForm):
    class Meta:
        model = User1
        exclude = ['data_reg']


class Auth(forms.ModelForm):

    class Meta:
        model = User1
        fields = ['username', 'password']