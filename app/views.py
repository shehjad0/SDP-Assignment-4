from django.shortcuts import render
from task.models import TaskModel

# Create your views here.

def index(request):
    tasks = TaskModel.objects.all()
    return render(request, 'index.html', { 'tasks': tasks })