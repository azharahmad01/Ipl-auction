from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Owner,Player
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('team_name',)
        
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('base_price',)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
