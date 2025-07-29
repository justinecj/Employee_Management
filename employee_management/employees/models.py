from django.db import models
from django.contrib.auth.models import User

class DynamicForm(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    schema = models.JSONField()  # Stores fields like [{label: 'Name', type: 'text'}, ...]

class Employee(models.Model):
    form = models.ForeignKey(DynamicForm, on_delete=models.CASCADE)
    data = models.JSONField()  # Stores actual values like {"Name": "John", "DOB": "1990-01-01"}
    created_at = models.DateTimeField(auto_now_add=True)
