from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import DynamicForm, Employee
from .serializers import DynamicFormSerializer, EmployeeSerializer
from rest_framework.filters import SearchFilter
from django.db.models import Q


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dynamic_form_list_create(request):
    if request.method == 'GET':
        forms = DynamicForm.objects.all()
        serializer = DynamicFormSerializer(forms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.user)
        serializer = DynamicFormSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dynamic_form_detail(request, pk):
    form = get_object_or_404(DynamicForm, pk=pk)

    if request.method == 'GET':
        serializer = DynamicFormSerializer(form)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employee_list_create(request):
    if request.method == 'GET':
        queryset = Employee.objects.all()

        # Optional: Filter using ?search=...
        search = request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(data__icontains=search)
            )

        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    emp = get_object_or_404(Employee, pk=pk)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        emp.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
