
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import VpnModel


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Username' , widget=forms.TextInput(attrs={"class": 'form-control'}))
    password = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['username' , 'password']



# add vpn form 
class AddVpnForm(forms.ModelForm):

    class Meta:
        model = VpnModel
        fields = ['hostname' , 'countryshort' , 'username' , 'password' , 'config']

        labels = {
            'hostname':'Enter Host Name',
            'countryshort':'Enter Countryshort',
            'username':'Enter Username',
            'password':'Enter Password',
            'config':'Enter Configuration',

        }

        widgets = {
            'hostname': forms.TextInput(attrs={'class':'form-control'}),
            'countryshort':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'config':forms.Textarea(attrs={'class':'form-control'}),

        }

