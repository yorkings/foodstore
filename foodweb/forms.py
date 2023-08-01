from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name =forms.CharField(max_length=100)
    last_name =forms.CharField(max_length=100) 
    gender1=[('male',"MALE"),('female',"Female")]
    gender= forms.ChoiceField(choices=gender1,required=True)
    class Meta:
        model =User
        fields= ['username','first_name','last_name','email','password1','password2']
class LoginForm(forms.Form) : 
    username=forms.CharField(max_length=50) 
    password=forms.CharField(max_length=50)   