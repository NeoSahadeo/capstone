from django.forms import ModelForm
from django import forms
from .models import User, UserImage

class RegisterForm(ModelForm, forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password','image']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = 'Profile Image'

class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']
