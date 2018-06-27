from django.shortcuts import render, redirect
from mychace.models import User
from django.http import HttpResponse


def registe(req):
    if req.method == "POST":
        users = User.objects.all()
        if users:
            users.name = req.POST.get('username')
            users.password = req.POST.get('password')
            users.email = req.POST.get('email')
            users.phone = req.POST.get('email')
            User.objects.create(username='name', password='password', email='email',phone='phone')
            User.save()

            return '注册成功'

    return render(req, 'login.html')


def login(req):
    if req.method == "POST":
        users = User.objects.all()
        user = User.objects.filter(users.username == 'name', users.password == 'password')
        if user:
            user.name = req.POST.get('username')
            user.password = req.POST.get('password')
            return redirect(req, 'index.html')
        else:
            return HttpResponse('密码或口令错误')

    else:
        return render(req, 'login.html')
