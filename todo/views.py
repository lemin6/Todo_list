from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TaskFilter
from rest_framework.filters import SearchFilter


class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['completed']
    permission_classes = [permissions.IsAuthenticated]

    # 1 IsAuthenticated
    # 2 IsAuthenticatedOrReadOnly
    # 3 AllowAny
    # 4 IsAdminUser







