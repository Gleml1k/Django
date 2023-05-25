from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(max_length=80)
    text = forms.Textarea()
    author = forms.CharField(max_length=40)

    class Meta:
        model = Post
        exclude = ['data']

