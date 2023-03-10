from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    # template_name = 'base/tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
  

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    # context_object_name = 'task'
    # success_url = reverse_lazy('tasks')
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self): 
        return reverse_lazy('tasks')



