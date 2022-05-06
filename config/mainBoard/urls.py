
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view_main, name="view_main"),
    path('create-category/', create_category, name="create_category"),
    path('get-category/', get_category, name="get_category"),
    path('update-category/<int:id>', update_category, name="update_category"),
    path('delete-category/<int:id>', delete_category, name="delete_category"),
    path('create-todo/<int:category_id>', create_todo, name="create_todo"),
    path('get-todo/<int:category_id>', get_todo, name="get_todo"),
    
]