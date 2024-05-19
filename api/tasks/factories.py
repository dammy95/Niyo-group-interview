import factory

from tasks.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    completed = factory.Faker('pybool')
    priority = factory.Faker('random_element', elements=['LOW', 'MEDIUM', 'HIGH'])
    due_date = factory.Faker('date_this_year', after_today=True)
    assigned_to = factory.SubFactory('users.factories.UserFactory')
