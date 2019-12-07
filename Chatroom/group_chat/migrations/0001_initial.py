# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-12-06 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=512, verbose_name='内容')),
                ('file', models.FileField(default=None, upload_to='')),
                ('img', models.ImageField(default=None, upload_to='')),
                ('target_user', models.CharField(default=None, max_length=32, verbose_name='目标用户id')),
                ('target_Pubroom', models.CharField(default=None, max_length=32, verbose_name='目标公共聊天室id')),
                ('user_self_id', models.CharField(max_length=32, verbose_name='自身id')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_chat',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('roomname', models.CharField(default=None, max_length=32, verbose_name='聊天室名字')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
