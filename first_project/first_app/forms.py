from django import forms
from django.contrib.auth.models import User
from first_app.models import Webpage, UserProfileInfo

class NewWebpageForm(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
