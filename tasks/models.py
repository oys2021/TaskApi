from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status_name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.status_name


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    status=models.ForeignKey(Status,on_delete=models.CASCADE)
    due_date=models.DateField()
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    