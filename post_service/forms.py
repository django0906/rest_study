from django import forms


class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=20)
    password = forms.CharField(label="Password", max_length=32)