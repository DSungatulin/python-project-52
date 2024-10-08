from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, 'index.html', context={})


class LoginView(LoginView):
    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('You have successfully logged in.')
        )
        return super().form_valid(form)


class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
