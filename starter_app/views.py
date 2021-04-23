from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#models
from .models import Task
from .forms import TaskForm, CreateAccountForm

from django.contrib.auth import login, authenticate


# Create your views here.
class IndexView(TemplateView):
    template_name = 'starter_app/indexView.html'

class CreateAccountView(TemplateView):
    template_name = 'starter_app/createAccountView.html'

class TaskDashboardView(LoginRequiredMixin, ListView):
    template_name = 'starter_app/dashboardView.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # filter out archieved tasks
        data = self.model.objects.all().filter(archive=False)

        # filter tasks for user
        tasks = data.filter(task_assigned_to=self.request.user.username)
        context['user_tasks'] = tasks.distinct().order_by('-due_date')

        return context

class TaskFormView(LoginRequiredMixin,TemplateView):
    template_name = 'starter_app/taskFormView.html'

class EditTaskView(LoginRequiredMixin,TemplateView):
    template_name = 'starter_app/updateTaskView.html'
