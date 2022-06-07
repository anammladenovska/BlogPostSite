from django import forms
from .models import BlogPost, UserBlocked


class AddPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        exclude = ("user", )


class BlockForm(forms.ModelForm):

    class Meta:
        model = UserBlocked
        exclude = ("user_account", )