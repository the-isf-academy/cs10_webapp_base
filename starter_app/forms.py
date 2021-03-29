from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'label',
            'notes',
            'due_date',
            'task_assigned_to'
            )

class CreateAccountForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = (
            'username',
            'password1',
            'password2'
            )

