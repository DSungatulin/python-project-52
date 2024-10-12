from django.contrib.auth.views import LoginView, LogoutView
from .mixins import LoginMessageMixin, LogoutMessageMixin
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})


class LoginView(LoginMessageMixin, LoginView):
    pass


class LogoutView(LogoutMessageMixin, LogoutView):
    pass
