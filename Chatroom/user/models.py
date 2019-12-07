from django.db import models

# Create your models here.
class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField('用户名',max_length=11,)
    nickname = models.CharField('昵称',max_length=30)
    password = models.CharField('密码',max_length=40)
    avatar = models.ImageField('头像',max_length=100)



    class Meta:
        db_table='user'