import factory

from django.contrib.auth import get_user_model


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """
    User factory

    This factory is used to create fake user instances for testing purposes.

    Attributes:
    -----------
    email : str
        The email of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    is_active : bool
        The activation status of the user.
    is_verified : bool
        The verification status of the user.
    is_superuser : bool
        The superuser status of the user.
    """
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = factory.Faker('pybool')
    is_verified = factory.Faker('pybool')
    is_superuser = factory.Faker('pybool')
