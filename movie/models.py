from __future__ import unicode_literals

from django.db import models

# Create your models here
class User(models.Model):
    name = models.CharField(max_length = 30,primary_key = True)
    password = models.CharField(max_length = 64)
    intro = models.CharField(max_length = 100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)

class Movie(models.Model):
    name = models.CharField(max_length = 40,primary_key = True)
    director = models.CharField(max_length = 30)
    actor = models.CharField(max_length = 30)
    actress = models.CharField(max_length = 30)
    type = models.CharField(max_length = 30)
    time = models.DateTimeField(auto_now = True)

class Post(models.Model):
    name = models.CharField(max_length = 40,primary_key = True)
    content = models.CharField(max_length = 800)
    poster = models.ForeignKey(User)
    time = models.DateTimeField(auto_now = True)
    num = models.IntegerField()
    movie = models.ForeignKey(Movie)
    plate = models.CharField(max_length = 30)

class Reply(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    content = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now = True)
