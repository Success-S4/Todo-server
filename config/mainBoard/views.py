from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import *
from django.http.response import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.
def view_main(request):
    return render(request, 'index.html')


def create_category(request):
    user = authenticate(username="admin", password="1234")
    login(request, user)
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        new_category = Category()
        new_category.user = request.user
        new_category.title = body['title']
        new_category.view_auth = body['view_auth']
        new_category.save()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '생성 성공!',
                'data': "create_category_json"
            })
    return 0
    
    
def get_category(request):
    user = authenticate(username="admin", password="1234")
    login(request, user)
    if request.method == "GET":
        uesr_category = Category.objects.filter(user = user)
        user_category_json = serializers.serialize("json", uesr_category)
        return JsonResponse(user_category_json, safe=False)
    return 0


def update_category(request, id):
    if request.method == "POST":
        # category_id = request.POST['category_id']
        body =  json.loads(request.body.decode('utf-8'))
        update_category = get_object_or_404(Category,pk = id)
        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.save()
        # update_category_json = serializers.serialize("json", update_category)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '업데이트 성공!',
                'data': "update_category_json"
            })
    return 0
    
    
def delete_category(request, id):
    if request.method == "POST":
        delete_category = get_object_or_404(Category, pk = id)
        delete_category.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': "delete_category_json"
            })
    return 0