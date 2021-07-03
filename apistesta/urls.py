from django.contrib.auth.models import User
from django.urls import path
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns = [
    path("", views.apiOverview, name="Api Overview"),
    path('api-token-auth/', authviews.obtain_auth_token),
    path("task-list/", views.taskList, name="Task List"),
    path("subtask-list/", views.subTaskList, name="SubTask List"),
    path("task-create/", views.taskCreate, name="Task Create"),
    path("subtask-create/", views.subTaskCreate, name="SubTask Create"),
    path("task-delete/", views.taskDelete, name="Task Delete"),
    path("subtask-delete/", views.subTaskDelete, name="SubTask Delete")
]
    