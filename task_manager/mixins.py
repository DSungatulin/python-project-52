from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            _('You are not authorized! Please log in')
        )
        return redirect('login')


class ProtectedCheckMixin:
    success_url = 'index'
    protected_error_message = _(
        'Cannot delete this object because it is in use'
    )

    def has_related_objects(self, obj):
        for related_object in obj._meta.related_objects:
            accessor_name = related_object.get_accessor_name()
            related_manager = getattr(obj, accessor_name)
            if related_manager.exists():
                return True
        return False

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.has_related_objects(obj):
            messages.error(request, self.protected_error_message)
            return redirect(self.success_url)

        return super().post(request, *args, **kwargs)


class LoginMessageMixin:
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('You have successfully logged in.'))
        return super().form_valid(form)


class LogoutMessageMixin:
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


class UserChangeOwnDataMixin(UserPassesTestMixin):
    object_attr = 'id'

    def test_func(self):
        obj = self.get_object()
        obj_user_attr = getattr(obj, self.object_attr)
        user = self.request.user

        if isinstance(obj_user_attr, int):
            if obj_user_attr != getattr(user, 'id'):
                return False
        else:
            if getattr(obj_user_attr, 'id') != getattr(user, 'id'):
                return False

        return True

    def handle_no_permission(self):
        if hasattr(self, 'model') and self.model == get_user_model():
            redirect_url = 'users'
        else:
            redirect_url = 'tasks'
        messages.add_message(
            self.request,
            messages.ERROR,
            _('You do not have permission to change another user')
            if redirect_url == 'users'
            else _('Only its author can delete a task')
        )
        return redirect(redirect_url)
