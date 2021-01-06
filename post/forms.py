from django import forms
from .models import Post 

class AddPostForm(forms.Form):
    postText = forms.CharField()

class PostForm(forms.ModelForm): 

    class Meta:
        model = Post
        fields = "__all__"