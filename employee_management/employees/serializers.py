from rest_framework import serializers
from .models import DynamicForm, Employee

class DynamicFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicForm
        fields = '__all__'
        read_only_fields = ['created_by']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['created_at']
