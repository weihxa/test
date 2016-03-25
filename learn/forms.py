from django import forms

class registerform(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)