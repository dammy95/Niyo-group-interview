import uuid

from django.db import models


class Task(models.Model):
    """
    Task model

    This model is used to represent a task.

    Attributes:
    -----------
    id : UUIDField
        The id of the task.
    created : DateTimeField
        The date and time the task was created.
    modified : DateTimeField
        The date and time the task was last modified.
    title : CharField
        The title of the task.
    description : TextField
        The description of the task.
    completed : BooleanField
        The completion status of the task.
    due_date : DateField
        The due date of the task.
    assigned_to : ForeignKey
        The user the task is assigned to.

    Methods:
    --------
    __str__()
        Returns the title of the task as a string.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='LOW')
    assigned_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)

    def __str__(self):
        return self.title
