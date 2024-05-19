import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from tasks.models import Task
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        'email': 'litty@vibes.com',
        'first_name': 'Litty',
        'last_name': 'Vibes',
        'password': 'litty_password',
        'confirm_password': 'litty_password',
    }


@pytest.fixture
def registered_user(api_client, user_data):

    url = reverse('users:register')

    data = user_data.copy()

    api_client.post(url, data=data)

    user = User.objects.get(email=user_data.get('email'))

    return user


@pytest.fixture
def logged_in_user_client(registered_user, user_data):
    client = APIClient()

    url = reverse('users:token-obtain-pair')

    data = {
        'email': registered_user.email,
        'password': user_data.get('password'),
    }

    response = client.post(url, data=data)

    token = response.data['access']

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    return client


@pytest.fixture
def logged_in_user_assigned_task(logged_in_user_client):
    url = reverse('tasks:task-list')

    data = {
        'title': 'Test task',
        'description': 'Test task description',
        'completed': False,
        'priority': 'LOW',
        'due_date': '2022-12-12',
    }

    response = logged_in_user_client.post(url, data=data)

    task = Task.objects.get(id=response.data.get('id'))

    return task
