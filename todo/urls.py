from django.urls import path
from .views import TaskViewSets

urlpatterns = [
    path('', TaskViewSets.as_view({'get': 'list', 'post': 'create'}), name='task_list'),
    path('<int:pk>/', TaskViewSets.as_view({'get': 'retrieve',
                                               'put': 'update', 'delete': 'destroy'}), name='task_detail'),
]