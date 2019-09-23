from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'required': 'true',
            'placeholder': 'Username:',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'required': 'true',
            'placeholder': 'Password:',
        }
    ))