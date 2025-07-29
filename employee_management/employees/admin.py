from django.contrib import admin
from .models import DynamicForm, Employee
import json
from django.utils.safestring import mark_safe

@admin.register(DynamicForm)
class DynamicFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_by', 'display_schema']
    search_fields = ['name', 'created_by__username']
    list_filter = ['created_by']

    def display_schema(self, obj):
        pretty_json = json.dumps(obj.schema, indent=2)
        return mark_safe(f'<pre>{pretty_json}</pre>')
    display_schema.short_description = "Form Schema"
    readonly_fields = ['display_schema']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'form', 'created_at', 'display_data']
    list_filter = ['form', 'created_at']
    search_fields = ['form__name']

    def display_data(self, obj):
        pretty_json = json.dumps(obj.data, indent=2)
        return mark_safe(f'<pre>{pretty_json}</pre>')
    display_data.short_description = "Submitted Data"
    readonly_fields = ['display_data']

