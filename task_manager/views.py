from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import SuccessMessageMixin


def index(request):
    return render(request, 'index.html', context={})


class CustomLoginView(LoginView, SuccessMessageMixin):
    success_message = _('You have successfully logged in.')


class CustomLogoutView(LogoutView, SuccessMessageMixin):
    success_message = _('You have successfully logged out.')
