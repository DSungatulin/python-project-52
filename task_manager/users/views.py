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
    template_name = 'form.html'
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }


class UserUpdateView(AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'form.html'
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users-detail')
    success_message = _('User Profile is successfully changed')
    success_url = reverse_lazy('users-detail')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class UserDeleteView(DeleteProtectMixin, AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users-detail')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users-detail')
    success_message = _('User successfully deleted')
    success_url = reverse_lazy('users-detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['title'] = _('Delete')
        context['message'] = _('Are you sure that you want to delete ')
        context['button_text'] = _('Yes, delete')
        context['entity_name'] = user.get_full_name()
        return context
