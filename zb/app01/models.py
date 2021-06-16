from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# auth_user表扩展
class UserInfo(AbstractUser):
    """用户信息表"""
    teacher_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    buf = models.CharField(max_length=50, null=True)
    buf1 = models.CharField(max_length=50, null=True)


class StudentInfo(models.Model):
    sid = models.CharField(max_length=15, primary_key=True)
    cid = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    addr = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    in_school = models.CharField(max_length=30)
    wrong = models.CharField(max_length=30)
    buf1 = models.CharField(max_length=50, null=True)
    buf2 = models.CharField(max_length=50, null=True)
    buf3 = models.CharField(max_length=50, null=True)


class CheckInfo(models.Model):
    check_id = models.CharField(max_length=15, primary_key=True)
    sid = models.ForeignKey(to='StudentInfo',on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    buf1 = models.CharField(max_length=50, null=True)
    buf2 = models.CharField(max_length=50, null=True)