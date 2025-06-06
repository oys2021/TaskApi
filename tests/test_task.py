import pytest
from django.urls import reverse
from tasks.models import Task, Status 
from rest_framework.test import APIClient
from django.contrib.auth.models import User



@pytest.fixture
def user(db):
    return User.objects.create_user(username="sarfo",email="sarfo@gmail.com",password="admin123")

@pytest.fixture
def api_client(user):
    client=APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def status():
    return Status.objects.create(status_name="pending")

@pytest.fixture
def task(user,status):
    return Task.objects.create(
        title="first_title",
        description="first description",
        status=status,
        user=user,
        due_date="2025-07-07"
    )

@pytest.mark.django_db
def test_get_tasks(api_client,task):
    url=reverse("get-task")
    response=api_client.get(url)
    assert response.status_code == 200
    assert response.data["success"] is True

@pytest.mark.django_db
def test_create_task(api_client,user,status):
    url=reverse("create-task")
    data = {"title": "New Task", "description": "Test description", "status":status,"user":user,"due_date":"2025-07-07" }
    response=api_client.post(url,data)
    assert response.status_code == 201
    assert response.data["success"] is True
    assert response.data["data"]["title"] == "New Task"



@pytest.mark.django_db
def test_update_task(api_client,task):
    url=reverse("update-task", args=[task.id])
    data={
    "title": "Updated Title"
    }
    response=api_client.put(url,data)
    assert response.status_code == 200
    assert response.data["success"] is True
    assert response.data["data"]["title"] == "Updated Title"