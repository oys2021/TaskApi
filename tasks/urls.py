from django.urls import path
from .views import create_task, get_task,update_task,list_statuses

urlpatterns = [
    path('tasks/', create_task, name='create-task'),  
    path('tasks/list/', get_task, name='get-task'),  
    path('tasks/<int:pk>/update/', update_task, name='update-task'),
    path('statuses/', list_statuses, name='list-statuses'),

]
