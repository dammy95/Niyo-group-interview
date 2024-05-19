from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Task viewset

    This viewset is used to perform CRUD operations on Task objects.

    Attributes:
    -----------
    queryset : QuerySet
        The queryset of Task objects.
    serializer_class : TaskSerializer
        The serializer class used to serialize Task objects.
    permission_classes : list
        The list of permission classes used to check if the user has permission to perform the operation.
    
    Methods:
    --------
    get_queryset(self)
        Returns the queryset of Task objects filtered by the user.
    perform_create(self, serializer)
        Assigns the task to the user who created it.
    perform_update(self, serializer)
        Assigns the task to the user who updated it.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

    def perform_update(self, serializer):
        serializer.save(assigned_to=self.request.user)
