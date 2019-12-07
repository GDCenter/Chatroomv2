from django.db import models
from user.models import UserProfile
# Create your models here.

class Group_chat(models.Model):
    id = models.IntegerField(primary_key=True,)
    roomname = models.CharField(verbose_name='聊天室名字',max_length=32,default=None)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_created=True)


# class User_chat(models.Model):
#
#     id = models.IntegerField(primary_key=True,auto_created=True)
#     img = models.ImageField(default=None)
#     content = models.CharField(verbose_name='内容', max_length=512)
#     file = models.FileField(default=None)
#     user_self = models.ForeignKey(UserProfile, on_delete=False, verbose_name='用户')
#     user_target = models.ForeignKey(UserProfile,on_delete=False,verbose_name='目标用户')
#     created_time = models.DateTimeField(auto_now_add=True)
#     modified_time = models.DateTimeField(auto_created=True)

class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(verbose_name='内容', max_length=512)
    file = models.FileField(default=None)
    img = models.ImageField(default=None)
    target_user = models.CharField(verbose_name='目标用户id',default=None,max_length=32)
    target_Pubroom = models.CharField(verbose_name='目标公共聊天室id',default=None,max_length=32)
    user_self_id = models.CharField(verbose_name='自身id',null=False,max_length=32)
    created_time = models.DateTimeField(auto_now_add=True,)

