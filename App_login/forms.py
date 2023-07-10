from django import  forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from .models import ProfileInfo, UserProfile


class SignUp(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField( label='password' , widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField( label='confirm password' , widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))

class ProfileInfoForm(forms.ModelForm): 
    class Meta:
        model = ProfileInfo
        fields = ['name','locality','city','mobile','zipcode','state']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'locality': forms.TextInput(attrs= {'class': 'form-control'}),
            'city': forms.TextInput(attrs= {'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs= {'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs= {'class': 'form-control'}),
            'state': forms.Select(attrs= {'class': 'form-control'}),

        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus': 'True','autocomplete':'current-password','class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
