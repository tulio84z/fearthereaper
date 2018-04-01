from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from authentication.models import User
from core.models import Objective


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(required=True, help_text='Inform your birthday')
    gender = forms.CharField(max_length=30, required=True, help_text='Inform your gender')
    nationality = forms.CharField(max_length=254, help_text='Inform your nationality')

    class Meta:
        model = User
        fields = ('username','email', 'birthday', 'gender', 'nationality', 'password1', 'password2', )

class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
        fields = ['objective_achieved', 'description']
