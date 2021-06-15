from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# auth_user表扩展
class UserInfo(AbstractUser):
    """用户信息表"""
    teacher_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    buf = models.CharField(max_length=50,null=True)
    buf1 = models.CharField(max_length=50, null=True)


