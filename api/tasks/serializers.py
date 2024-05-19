from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Task serializer
    
    This serializer is used to serialize Task objects.
    
    Attributes:
    -----------
    id : int
        The id of the task.
    title : str
        The title of the task.
    description : str
        The description of the task.
    completed : bool
        The completion status of the task.
    priority : str
        The priority of the task.
    due_date : date
        The due date of the task.
    assigned_to : str
        The user the task is assigned to.
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'priority', 'due_date', 'assigned_to']
