# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here

validPlates = [
    (1, "图解电影"),
    (2, "剧情解析"),
    (3, "影评分析"),
    (4, "周边杂谈"),
    (5, "精彩瞬间"),
]

validSexes = [
    ("f", "女"),
    ("m", "男"),
]


class Profile(models.Model):
    auth_user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=validSexes, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class Movie(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    descrip = models.CharField(max_length=2000)
    img = models.ImageField()
    director = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    actress = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    time = models.IntegerField()

    def __unicode__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=40)
    content = models.CharField(max_length=800)
    poster = models.ForeignKey(User)
    time = models.DateTimeField(auto_now=True)
    num = models.IntegerField()
    movie = models.ForeignKey(Movie)
    plate = models.IntegerField(choices=validPlates)
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("postDetail", kwargs={"pk": self.id})


class Reply(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
