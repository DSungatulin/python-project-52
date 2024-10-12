from django.contrib.auth.views import LoginView, LogoutView
from .mixins import LoginMessageMixin, LogoutMessageMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(LoginMessageMixin, LoginView):
    pass


class LogoutView(LogoutMessageMixin, LogoutView):
    pass
