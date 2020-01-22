from django.shortcuts import render,redirect
from myweb.models import User

from myweb import views

# Create your views here.
#页面查询用户信息
def queryUsers(request):
    #到数据库查询用户信息
    us = User.objects.all()
    #将数据发给页面
    context = {"ls": us}
    return render(request, "users.html", context)


# 打开添加页面
def openAdd(request):
    return render(request, "userAdd.html")


# 保存数据
def saveUser(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    add = request.GET.get('add')
    stock = request.GET.get('stock')
    User.objects.create(username=username, password=password,add=add,stock=stock)
    return redirect("/myweb/queryUsers")

    # 打开修改页面
def openEdit(request):
    id = request.GET.get('id')
    # 到数据库查询用户信息
    m = User.objects.filter(id=id).first()
    # 将数据发给页面
    context = {"m": m}
    return render(request, "userEdit.html", context)

    # 更新数据
def updateUser(request):
    id = request.GET.get('id')
    username = request.GET.get('username')
    password = request.GET.get('password')
    add = request.GET.get('add')
    stock = request.GET.get('stock')
    User.objects.filter(id=id).update(username=username, password=password, add=add, stock=stock)

    return redirect("/myweb/queryUsers")

    # 删除数据
def deleteUser(request):
    id = request.GET.get('id')
    User.objects.filter(id=id).delete()
    return redirect("/myweb/queryUsers")

