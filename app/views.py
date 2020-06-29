from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from app.models import User
# Create your views here.
from .valid import user_check


def reg(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')
    if not username:
        return HttpResponse('not username')
    if not all((password,re_password)):
        return HttpResponse('no password')
    userisvalid,err_msg = user_check(username,password,re_password)
    if not userisvalid:
        return HttpResponse('%s'% err_msg)

    if User.objects.filter(username=username):
        return HttpResponse('active')
    auth = bool(password == re_password)
    if auth:
        return HttpResponse('zhuce')
    else:
        return HttpResponse('error')


def ceshi(request):
    pass
