# -*- coding: UTF-8 -*-
from django import forms

from comments.models import Comments


class CommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'cols': '55', 'rows': '10', 'placeholder': 'Присоединяйтесь к обсуждению...',
        'spellcheck': 'true', 'maxlength': '2000'
        }))

    class Meta:
        model = Comments
        fields = ('body',)
