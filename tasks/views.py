from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  IsAuthenticated, AllowAny
from tasks.models import *
from tasks.serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from rest_framework.exceptions import ValidationError

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_task(request):
    user= request.user
    try:
        task=Task.objects.filter(user=user)
        serializer= TaskSerializer(task,many=True)
        return Response(
            {"success": True, "results": serializer.data},
            status=status.HTTP_200_OK
        )
    
    except ObjectDoesNotExist:
        return Response(
            {"success": False, "message": "User or tasks not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    except DatabaseError:
        return Response(
            {"success": False, "message": "A database error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        task = serializer.save(user=request.user)
        return Response(
            {"success": True, "data": TaskSerializer(task).data},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {"success": False, "message": "Invalid data", "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )
    
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_task(request,pk):
    try:
        task=Task.objects.get(pk=pk,user=request.user)
    
    except Task.DoesNotExist:
        return Response(
            {"success": False, "message": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer=TaskSerializer(task,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"success":True,"data":serializer.data},
            status=status.HTTP_200_OK
        )
    
    return Response(
        {"success": False, "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_statuses(request):
    statuses = Status.objects.all()
    serializer = StatusSerializer(statuses, many=True)
    return Response(serializer.data, status=200)
    
    

    
        

