from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_update, name='edit_task'),
    path('delete/<int:pk>/', views.task_delete, name='delete_task'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('settings/', views.settings_page, name='settings'),
]
