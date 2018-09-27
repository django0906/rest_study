from django import forms


class LoginForm(forms.Form):
    user_id = forms.CharField(label="ID", max_length=30)
    user_password = forms.CharField(label="Password", max_length=36)

