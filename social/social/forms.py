from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from detailprofile.models import ProfileUser



class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords_Mismatch")


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileUser
        fields = ['first_name', 'last_name', 'designation', 'description', 'website', 'phone']


