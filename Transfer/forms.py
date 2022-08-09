from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [
            "first_name", "last_name", "email", "username", "pin"
        ]

        widget = {
            'pin': forms.PasswordInput(),
        }


# There is no need for this line of code 

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=20)
#     pin = forms.CharField(max_length=20, widget=forms.PasswordInput)