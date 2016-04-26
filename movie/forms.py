# -*- coding: utf-8 -*-

from django import forms
from models import validPlates, Post, Reply


class MoviePosterForm(forms.Form):
    movie = forms.CharField(label="电影", required=False)
    plate = forms.ChoiceField(label="板块", choices=validPlates)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name", "content", "num", "movie", "plate", "image"]
        widgets = {
            'content': forms.Textarea(),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(),
        }
