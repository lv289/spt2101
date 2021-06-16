from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/',views.index,name='index'),
    path('logout_view/',views.logout_view,name='out'),

    #------------#
    path('stu_management/',views.stu_management,name='stu'),
]