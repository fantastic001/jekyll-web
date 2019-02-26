
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, label="Title")
    contents = forms.CharField(max_length=1024*64, widget=forms.Textarea, label="Contents")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=256)
