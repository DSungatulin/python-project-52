from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from .models import User
from task_manager.mixins import AuthenticationMixin, AuthorizationMixin, DeleteProtectMixin
# Create your views here.


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_message = _('User is successfully registered')
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'


class UserUpdateView(AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users-detail')
    success_message = _('User Profile is successfully changed')
    success_url = reverse_lazy('users-detail')
    extra_context = {
        'title': _('Delete User'),
    }


class UserDeleteView(DeleteProtectMixin, AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users-detail')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users-detail')
    success_message = _('User successfully deleted')
    success_url = reverse_lazy('users-detail')
