from tasks.models import *
from rest_framework import serializers
from datetime import date


class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Status
        fields="__all__"
    

class TaskSerializer(serializers.ModelSerializer):
    status= serializers.SlugRelatedField(
        queryset=Status.objects.all(),
        slug_field="status_name"
    )
    
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    class Meta:
        model=Task 
        fields = [
            'id', 'user', 'title', 'description',
            'status', 'due_date', 'create_at'
        ]
        read_only_fields = ['create_at']
        
    def validate_due_date(self,value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
            
        