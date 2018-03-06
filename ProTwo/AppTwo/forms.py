from django import forms
from django.core import validators
from AppTwo.models import Usertab,userprofileinfotab
from django.contrib.auth.models import User



class FormModel(forms.ModelForm):
    #First_name = forms.CharField()
    #Last_name = forms.CharField()
    #Email_id = forms.EmailField()
    class Meta():
        model = Usertab
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileinfoForm(forms.ModelForm):
    class Meta():
        model = userprofileinfotab
        fields = ('portfolio_site','profile_pic')
