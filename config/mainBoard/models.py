from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    view_auth = models.IntegerField()
    
    
class Todo(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length = 50)
    is_completed = models.BooleanField()
    pup_date = models.DateTimeField(auto_now_add=True)