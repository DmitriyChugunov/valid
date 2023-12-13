from django import forms


class reg_form(forms.Form):
    name = forms.CharField(min_length=4)
    email = forms.EmailField()
    password = forms.CharField(min_length=8)


class login_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8)
