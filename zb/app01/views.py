from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from app01.models import *
import time

# Create your views here.

# 登录
def login(request):
    if request.method == 'POST':
        print(11)
        user = request.POST.get("user")
        pwd = request.POST.get('pwd')
        if UserInfo.objects.filter(username=user):
            user_flag = authenticate(request,username= user,password= pwd)
            if user_flag is not None:
                auth.login(request,user_flag)
                return redirect('index')
            else:
                tips = '用户名或密码错误，请重新输入'
        else:
            tips = '用户名不存在,请注册'

    return render(request,'app01/login.html',locals())

# 注册
def register(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        phone = request.POST.get("phone")
        teacher_number = request.POST.get("teacher_id")
        user = UserInfo.objects.create_user\
            (username=user,password=pwd,first_name=name,phone=phone,teacher_id=teacher_number)

        return redirect('login')
    return render(request,'app01/regis.html')

# 主界面
@login_required
def index(request):
    t = time.localtime(time.time())
    now = (t.tm_year,t.tm_mon,t.tm_mday) # 取请求的时间
    now_user = request.user.username
    Obj = CheckInfo.objects.filter(time = '2021-6-16')
    print(Obj)
    for i in Obj:
        print(i.time,i.sid.name)
    return render(request,'app01/index.html',{'user_name':now_user})


# 退出登录
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def stu_management(request):
    now_user = request.user.username
    return render(request,'app01/stu_management.html',{'user_name':now_user})
# 添加学生函数
def stu_add(request):
    return render(request, 'app01/stu_add.html')

# 编辑学生函数
def stu_edit(request):
    return render(request, 'app01/stu_edit.html')