# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 12:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('descrip', models.CharField(max_length=2000)),
                ('img', models.ImageField(upload_to=b'')),
                ('director', models.CharField(max_length=30)),
                ('actor', models.CharField(max_length=30)),
                ('actress', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=800)),
                ('time', models.DateTimeField(auto_now=True)),
                ('num', models.IntegerField()),
                ('plate', models.IntegerField(choices=[(1, b'\xe5\x9b\xbe\xe8\xa7\xa3\xe7\x94\xb5\xe5\xbd\xb1'), (2, b'\xe5\x89\xa7\xe6\x83\x85\xe8\xa7\xa3\xe6\x9e\x90'), (3, b'\xe5\xbd\xb1\xe8\xaf\x84\xe5\x88\x86\xe6\x9e\x90'), (4, b'\xe5\x91\xa8\xe8\xbe\xb9\xe6\x9d\x82\xe8\xb0\x88'), (5, b'\xe7\xb2\xbe\xe5\xbd\xa9\xe7\x9e\xac\xe9\x97\xb4')])),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('intro', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
