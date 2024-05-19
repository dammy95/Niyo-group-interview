import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    User model

    This model is used to represent a user.

    Attributes:
    -----------
    id : UUIDField
        The id of the user.
    created : DateTimeField
        The date and time the user was created.
    modified : DateTimeField
        The date and time the user was last modified.
    is_active : BooleanField
        The status of the user.
    is_verified : BooleanField
        The verification status of the user.
    is_superuser : BooleanField
        The superuser status of the user.
    is_staff : BooleanField
        The staff status of the user.
    email : EmailField
        The email of the user.
    first_name : CharField
        The first name of the user.
    last_name : CharField
        The last name of the user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
