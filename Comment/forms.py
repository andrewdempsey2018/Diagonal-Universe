from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=30,
    widget=forms.Textarea(attrs={"rows":1, "cols":5}))

    text = forms.CharField(max_length=300,
    widget=forms.Textarea(attrs={"rows":3, "cols":5}))