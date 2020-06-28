import re
from django.shortcuts import render,HttpResponse,redirect


def user_valid(username,password,re_password):
    if re.match(r'^[A-Za-z_@.]{6,10}$',username):
        if re.match(r'^(?![0-9]+$)(?![a-z]+$)(?![A-Z]+$)(?!([^(0-9a-zA-Z)])+$).{6,10}$',password) :
            if re.match(r'^(?![0-9]+$)(?![a-z]+$)(?![A-Z]+$)(?!([^(0-9a-zA-Z)])+$).{6,20}$',re_password):
                return (True,'格式正确')
            else:
                return (False,'重复输入密码格式错误')
        else:
            return (False,'密码格式错误')
    else:
        return (False,'用户格式错误')


user_check = user_valid