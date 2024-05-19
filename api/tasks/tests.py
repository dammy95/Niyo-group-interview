import pytest

from django.urls import reverse

from tasks.models import Task
from tasks.factories import TaskFactory


@pytest.mark.django_db
def test_task_creation():
    """
    Test that a task can be created.
    """
    TaskFactory.create()
    assert Task.objects.count() == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    'user_client_fixture, task_count, status_code',
    [
        ('api_client', 0, 401),
        ('logged_in_user_client', 1, 201),
    ],
)
def test_can_create_task(request, user_client_fixture, task_count, status_code):
    """
    Test that a logged in user can create a task.
    """
    user_client = request.getfixturevalue(user_client_fixture)
    url = reverse('tasks:task-list')

    data = {
        'title': 'Test task',
        'description': 'Test task description',
        'completed': False,
        'priority': 'LOW',
        'due_date': '2022-12-12',
    }

    response = user_client.post(url, data=data)

    assert response.status_code == status_code
    assert Task.objects.count() == task_count


@pytest.mark.django_db
@pytest.mark.parametrize(
    'user_client_fixture, status_code',
    [
        ('api_client', 401),
        ('logged_in_user_client', 200),
    ],
)
def test_can_retrieve_task(request, logged_in_user_assigned_task, user_client_fixture, status_code):
    """
    Test that a user can retrieve a task.
    """
    user_client = request.getfixturevalue(user_client_fixture)

    url = reverse('tasks:task-detail', args=[str(logged_in_user_assigned_task.id)])

    response = user_client.get(url)

    assert response.status_code == status_code

    if response.status_code == 200:
        assert response.data.get('title') == logged_in_user_assigned_task.title


@pytest.mark.django_db
@pytest.mark.parametrize(
    'user_client_fixture, status_code',
    [
        ('api_client', 401),
        ('logged_in_user_client', 200),
    ],
)
def test_can_update_task(request, logged_in_user_assigned_task, user_client_fixture, status_code):
    """
    Test that a user can update a task.
    """
    user_client = request.getfixturevalue(user_client_fixture)

    url = reverse('tasks:task-detail', args=[str(logged_in_user_assigned_task.id)])

    data = {
        'title': 'Updated task',
        'description': 'Updated task description',
        'completed': True,
        'priority': 'HIGH',
        'due_date': '2022-12-12',
    }

    response = user_client.put(url, data=data)

    assert response.status_code == status_code

    if response.status_code == 200:
        assert response.data.get('title') == data.get('title')


@pytest.mark.django_db
@pytest.mark.parametrize(
    'user_client_fixture, task_count, status_code',
    [
        ('api_client', 1, 401),
        ('logged_in_user_client', 0, 204),
    ],
)
def test_can_delete_task(request, logged_in_user_assigned_task, user_client_fixture, task_count, status_code):
    """
    Test that a user can delete a task.
    """
    user_client = request.getfixturevalue(user_client_fixture)

    url = reverse('tasks:task-detail', args=[str(logged_in_user_assigned_task.id)])

    response = user_client.delete(url)

    assert response.status_code == status_code
    assert Task.objects.count() == task_count


@pytest.mark.django_db
@pytest.mark.parametrize(
    'user_client_fixture, task_count, status_code',
    [
        ('api_client', 0, 401),
        ('logged_in_user_client', 5, 200),
    ],
)
def test_can_list_tasks(request, registered_user, user_client_fixture, task_count, status_code):
    """
    Test that a user can list tasks.
    """
    user_client = request.getfixturevalue(user_client_fixture)

    for task in TaskFactory.create_batch(5):
        task.assigned_to = registered_user
        task.save()

    url = reverse('tasks:task-list')

    response = user_client.get(url)

    assert response.status_code == status_code

    if response.status_code == 200:
        assert len(response.data) == task_count
