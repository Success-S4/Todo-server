from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.core import serializers
from .models import *
import json


# Create your views here.
def signin(request):
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        email = body['email']
        pw = body['pw']
        user = authenticate(email=email, password=pw)
        if user is not None:
            login(request, user)
            status = 200
            is_successed = True
            message = "signin successed"
            user_json = serializers.serialize("json", [user])
        else:
            status = 404
            is_successed = False
            message = "signin failed"
            user_json = None
        
        return JsonResponse({
                'status': status,
                'success': is_successed,
                'message': message,
                'data': user_json
            })
    return 0


def signup(request):
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        username = body['username']
        email = body['email']
        pw = body['pw']
        pw_check = body['pw_check']
        if User.objects.filter(email=email).exists():
            status = 404
            is_successed = False
            message = "이미 존재하는 아이디 입니다. 다른 아이디를 입력해 주세요!"
            user_json = None
        else:
            if pw == pw_check:    
                user = User.objects.create_user(
                    username = username, 
                    email = email,
                    password = pw
                )
                user.save()
                status = 200
                is_successed = True
                message = "회원가입 성공! 로그인하여 입장해 주세요!"
                user_json = serializers.serialize("json", [user])
            else:
                status = 404
                is_successed = False
                message = "비밀번호와 비밀번호 확인이 일치하지 않습니다."
                user_json = None
                
        return JsonResponse({
                'status': status,
                'success': is_successed,
                'message': message,
                'data': user_json
            })
    return 0
