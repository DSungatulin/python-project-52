from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Status
from .forms import StatusForm

# Create your views here.


class ListOfStatusesView(ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    login_url = reverse_lazy('/login/')
    success_message = _('Status successfully added')
    success_url = reverse_lazy('statuses-detail')
    template_name = 'statuses/create.html'


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    login_url = reverse_lazy('/login/')
    success_message = _('Status successfully changed')
    success_url = reverse_lazy('statuses-detail')
    template_name = 'statuses/update.html'


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    login_url = reverse_lazy('/login/')
    success_message = _('Status successfully deleted')
    success_url = reverse_lazy('statuses-detail')
    template_name = 'statuses/delete.html'
    extra_context = {
        'title': _('Delete Status'),
    }

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.error(self.request, _("Cannot delete this status because it is referenced by one or more tasks."))
        return redirect(self.success_url)
