from django import forms
from .models import Comment

class CommentForm(forms.ModelsForm):
    class Meta:
        model = CommentForm
        fields = '__all__'
