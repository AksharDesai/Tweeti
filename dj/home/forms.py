from django import forms

from .models import Tweet,Comments


class Tweetform(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ("text", "image")
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write a tweeti...', 'class': 'tweeti-box'}),
        }
    



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']  # Only include the `text` field for user input
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Write a comment...', 'class': 'form-control'}),
        }


