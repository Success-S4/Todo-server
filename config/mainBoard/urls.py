
from django.urls import path
from .views import *

urlpatterns = [
    path('', view_main, name="view_main"),
    path('get-category/', get_category, name="get_category"),
    path('update-category/<int:id>', update_category, name="update_category"),
    path('delete-category/<int:id>', delete_category, name="delete_category"),
    path('create-category/', create_category, name="create_category")
]