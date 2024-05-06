from django import forms


class PostForm(forms.Form):

    your_post = forms.CharField(label='', max_length=10)