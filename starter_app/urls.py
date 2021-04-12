from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.CreateAccountView.as_view(), name='register'),

    path('dashboard/', views.TaskDashboardView.as_view(), name='dashboard'),

    path('newtask/', views.TaskFormView.as_view(), name='new-task'),
    path('updatetask/<int:pk>/', views.EditTaskView.as_view(), name='update-task'),
]
