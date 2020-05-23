from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.CharField(max_length=300, widget=forms.Textarea)