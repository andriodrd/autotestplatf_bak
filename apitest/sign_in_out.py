# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 11:50
# @Author  : MingMing
# @Email   : yangmm@longrise.com.cn
# @File    : sign_in_out.py
# @Software: PyCharm


from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout

# 登录处理
def signin(request):
    if request.POST:
        # 从http post请求中获取用户名、密码参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 使用django auth 库里面的方法判断是否有该用户名和密码
        user = authenticate(username=username,password=password)
        # 如果找到用户，并且密码正确
        if user is not None:
            if user.is_active:
                # 如果存在该用户并且状态是激活的
                if user.is_superuser:
                    # 使用Django的login()函数进行登陆
                    login(request,user)
                    # 在session 中存入用户类型 数据库表django_session保存session_key,session_data,expire_data
                    request.session['user'] = username
                    return  JsonResponse({'ret':0})
                else:
                    return  JsonResponse({'ret':1,'msg':'请使用管理员账户登录'})
            else:
                return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})
        else:
            return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误！'})

def signout(request):
    login(request)
    return JsonResponse({'ret':'0'})