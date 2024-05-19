import pytest

from django.urls import reverse

from users.models import User
from users.factories import UserFactory


@pytest.mark.django_db
def test_user_creation():
    """
    Test that a user can be created.
    """
    UserFactory.create(email='test@niyogroup.com')
    assert User.objects.count() == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, first_name, last_name, password, confirm_password, user_created_count, status_code',
    [
        ('', '', '', '', '', 0, 400),
        ('', 'Litty', 'Vibes', 'password', 'password', 0, 400),
        ('litty@vibes.com', 'Litty', 'Vibes', 'password', 'different_password', 0, 400),
        ('litty@vibes.com', 'Litty', 'Vibes', 'test_password', 'test_password', 1, 201),
    ]
)
def test_can_register_user(
    email, first_name, last_name, password, confirm_password, user_created_count, status_code, api_client
):
    """
    Test that a user can register.
    """
    url = reverse('users:register')
    data = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'confirm_password': confirm_password,
    }

    response = api_client.post(url, data=data)

    assert response.status_code == status_code
    assert User.objects.count() == user_created_count


@pytest.mark.django_db
def test_registered_user_can_login(api_client, registered_user):
    """
    Test that a registered user can login.
    """
    url = reverse('users:token-obtain-pair')
    data = {
        'email': registered_user.email,
        'password': 'litty_password',
    }

    response = api_client.post(url, data=data)

    assert response.status_code == 200

    assert response.data.get('access')
    assert response.data.get('refresh')
