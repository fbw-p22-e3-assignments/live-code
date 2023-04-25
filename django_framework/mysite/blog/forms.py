from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)