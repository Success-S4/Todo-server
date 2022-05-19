from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from .models import *
import json


# Create your views here.
def signin(request):
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        email = request.POST['email']
        pw = request.POST['pw']
        username = 
        user = authenticate(username=input_id, password=input_pw)
        if user is not None:
            login(request, user)

            return 0

        else:
            print("로그인 실패")
    return render(request, "signin.html")