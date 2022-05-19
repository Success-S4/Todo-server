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
    print("debug")
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
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '수신 성공!',
                'data': user_category_json
            })
    return 0


def update_category(request, id):
    if request.method == "POST":
        # category_id = request.POST['category_id']
        body =  json.loads(request.body.decode('utf-8'))
        update_category = get_object_or_404(Category,pk = id)
        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.save()
        update_category_json = [update_category]
        update_category_json = serializers.serialize("json", update_category_json)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '업데이트 성공!',
                'data': update_category_json
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


def create_todo(request, category_id):
    user = authenticate(username="admin", password="1234")
    login(request, user)
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        new_todo = Todo()
        new_todo.category = get_object_or_404(Category, pk = category_id)
        new_todo.content = body['content']
        new_todo.save()
        new_todo_json = [new_todo]
        new_todo_json = serializers.serialize("json", new_todo_json)
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '댓글 생성 성공!',
                'data': new_todo_json
            })
    return 0


def get_todo(request, category_id):
    if request.method == "GET":
        category_todo = Todo.objects.filter(category = category_id)
        category_todo_json = serializers.serialize("json", category_todo)
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 로드 성공!',
                'data': category_todo_json
            })
    return 0


def update_todo(request, todo_id):
    if request.method == "POST":
        body =  json.loads(request.body.decode('utf-8'))
        update_todo = get_object_or_404(Todo,pk = todo_id)
        update_todo.content = body['content']
        update_todo.is_completed = body['is_completed']
        update_todo.save()
        update_todo_json = [update_todo]
        update_todo_json = serializers.serialize("json", update_todo_json)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '댓글 업데이트 성공!',
                'data': update_todo_json
            })
    return 0


def delete_todo(request, todo_id):
    if request.method == "POST":
        delete_todo = get_object_or_404(Todo,pk = todo_id)
        delete_todo.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '댓글 삭제 성공!',
                'data': "delete_category_json"
            })
    return 0