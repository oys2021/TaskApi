from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  IsAuthenticated, AllowAny
from authentication.serializers import *
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    data= request.data
    serializer=UserSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"success":True,"data":serializer.data},
            status=status.HTTP_201_CREATED
        )
        
    return Response(
        {"success":False,"message":"Invalid data", "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    try:
        user=User.objects.filter(username=request.user.username)
        serializer=UserProfileSerializer(user,many=True)
        return Response(
            {"success":True,"data":serializer.data},
            status=status.HTTP_200_OK
        )
    
    except ObjectDoesNotExist:
        return Response(
            {"success":False,"message":"user not found"},
            status=status.HTTP_404_NOT_FOUND
        )
        
    except DatabaseError:
        return Response(
            {"success": False, "message": "A database error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
