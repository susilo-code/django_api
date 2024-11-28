from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_dense.models import Emp
from api_dense.serializers import EmpSerializer
from rest_framework import status



# Create your views here.

@api_view()
def view_dtl(request):
    return Response({'success': 409, 'message': 'api'})



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def view_emp(request):
    # GET method to retrieve all employees
    if request.method == 'GET':
        emp_obj = Emp.objects.all()
        serializer = EmpSerializer(emp_obj, many=True)
        return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

    # POST method to create a new person
    elif request.method == 'POST':
        serializer = EmpSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method to update a person (full update)
    elif request.method == 'PUT':
        emp_obj = Emp.objects.get(pk=request.data.get('id'))
        serializer = EmpSerializer(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH method to partially update a person
    elif request.method == 'PATCH':
        emp_obj = Emp.objects.get(pk=request.data.get('id'))
        serializer = EmpSerializer(emp_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a person
    elif request.method == 'DELETE':
        emp_obj = Emp.objects.get(pk=request.data.get('id'))
        emp_obj.delete()
        return Response({'msg': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)