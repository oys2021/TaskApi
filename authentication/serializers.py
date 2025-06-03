from authentication.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=["id","username","email","password"]
        
    def create(self,validated_data):
        user=User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
        
       
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email"]
        read_only_fields = ['id']