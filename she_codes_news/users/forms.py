from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username','first_name', 'last_name', 'email', 'location', 'bio']
        

class UpdateprofileForm(forms.ModelForm):
        image = forms.URLField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
        bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

        class Meta:
            model = profile
            fields = ['image', 'bio']
            labels = {'bio': 'About'}


