from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='task_todo'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
    path('complete/<int:id>/', mark_as_completed, name='complete'),
]
