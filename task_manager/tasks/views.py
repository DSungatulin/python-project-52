from django.forms import BaseModelForm
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthenticationMixin, AuthorDeleteMixin
from .models import Task
from .forms import TaskForm
from task_manager.users.models import User
from django_filters.views import FilterView
from .filters import TaskFilter
# Create your views here.


class TaskListView(AuthenticationMixin, FilterView):

    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskDetailView(AuthenticationMixin, DetailView):

    model = Task
    template_name = 'tasks/task_detail.html'
    extra_context = {
        'title': _('Viewing a task'),
    }


class TaskCreateView(AuthenticationMixin, SuccessMessageMixin, CreateView):

    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')
    template_name = 'form.html'
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthenticationMixin, SuccessMessageMixin, UpdateView):

    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully updated')
    template_name = 'form.html'
    extra_context = {
        'title': _('Update Task'),
        'button_text': _('Update')
    }


class TaskDeleteView(AuthenticationMixin, AuthorDeleteMixin, SuccessMessageMixin, DeleteView):

    model = Task
    template_name = 'delete.html'
    author_message = _("You can't delete this task")
    author_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['title'] = _('Delete')
        context['message'] = _('Are you sure that you want to delete ')
        context['button_text'] = _('Yes, delete')
        context['entity_name'] = task.__str__()
        return context
