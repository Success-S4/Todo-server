from site import USER_BASE
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
        
        new_category_json={}
        new_category_json["category_id"] = new_category.id
        new_category_json["user"] = new_category.user.email
        new_category_json["title"] = new_category.title
        new_category_json["view_auth"] = new_category.view_auth
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '생성 성공!',
                'data': new_category_json
            })
    return 0
    
def detail_category(request, id):
    if request.method == "GET":
        detail_category = get_object_or_404(Category,pk = id)
        detail_category_json={}
        detail_category_json["category_id"] = detail_category.id
        detail_category_json["user"] = detail_category.user.email
        detail_category_json["title"] = detail_category.title
        detail_category_json["view_auth"] = detail_category.view_auth
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'detail_category 수신 성공!',
                'data': detail_category_json
            })
    return 0

def get_category(request):
    user = authenticate(username="admin", password="1234")
    login(request, user)
    if request.method == "GET":
        uesr_category = Category.objects.filter(user = user)
        # user_category_json = serializers.serialize("json", uesr_category)
        user_category_json=[]
        for category in uesr_category:
            new_set={}
            new_set["category_id"] = category.id
            new_set["user"] = category.user.email
            new_set["title"] = category.title
            new_set["view_auth"] = category.view_auth
            user_category_json.append(new_set)
                
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category 수신 성공!',
                'data': user_category_json
            })
    return 0


def update_category(request, id):
    if request.method == "PATCH":
        body =  json.loads(request.body.decode('utf-8'))
        update_category = get_object_or_404(Category,pk = id)
        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.save()
        # update_category_json = [update_category]
        # update_category_json = serializers.serialize("json", update_category_json)
        
        update_category_json={}
        update_category_json["category_id"] = update_category.id
        update_category_json["user"] = update_category.user.email
        update_category_json["title"] = update_category.title
        update_category_json["view_auth"] = update_category.view_auth
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '업데이트 성공!',
                'data': update_category_json
            })
    return 0
    
    
def delete_category(request, id):
    if request.method == "DELETE":
        delete_category = get_object_or_404(Category, pk = id)
        delete_category.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': None
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
        # new_todo_json = serializers.serialize("json", [new_todo])
        new_todo_json={}
        new_todo_json["todo_id"] = new_todo.id
        new_todo_json["content"] = new_todo.content
        new_todo_json["is_completed"] = new_todo.is_completed
        new_todo_json["pup_date"] = new_todo.pup_date
        
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
        # category_todo_json = serializers.serialize("json", category_todo)
        
        category_todo_json=[]
        for todo in category_todo:
            new_set={}
            new_set["todo_id"] = todo.id
            new_set["content"] = todo.content
            new_set["is_completed"] = todo.is_completed
            new_set["pup_date"] = todo.pup_date
            category_todo_json.append(new_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 로드 성공!',
                'data': category_todo_json
            })
    return 0


def update_todo(request, todo_id):
    if request.method == "PATCH":
        body =  json.loads(request.body.decode('utf-8'))
        update_todo = get_object_or_404(Todo,pk = todo_id)
        update_todo.content = body['content']
        update_todo.is_completed = body['is_completed']
        update_todo.save()
        
        # update_todo_json = serializers.serialize("json", [update_todo])
        
        update_todo_json={}
        update_todo_json["todo_id"] = update_todo.id
        update_todo_json["content"] = update_todo.content
        update_todo_json["is_completed"] = update_todo.is_completed
        update_todo_json["pup_date"] = update_todo.pup_date
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'Todo 업데이트 성공!',
                'data': update_todo_json
            })
    return 0


def delete_todo(request, todo_id):
    if request.method == "DELETE":
        delete_todo = get_object_or_404(Todo,pk = todo_id)
        delete_todo.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '댓글 삭제 성공!',
                'data': "delete_category_json"
            })
    return 0