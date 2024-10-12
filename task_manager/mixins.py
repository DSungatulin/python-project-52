from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            _('You are not authorized! Please log in')
        )
        return redirect('login')


class ObjectPermissionMixin(UserPassesTestMixin):
    """
    Mixin to enforce object-level permissions based on a user attribute.

    Attributes:
        object_attr (str): The attribute of the object that should be compared
            to the user. Defaults to 'id'.
        success_url (str): The URL to redirect to if the permission check
            fails. Defaults to 'index'.
        permission_error_message (str): The error message to display if the
            permission check fails. Defaults to 'You do not have permission to
            perform this action.'.

    Methods:
        dispatch(request, *args, **kwargs):
            Override the default dispatch method to enforce the permission
            check. If the user does not have permission, add an error message
            and redirect to the success URL.

        add_flash_and_redirect(request):
            Add an error message to the messages framework and redirect to the
            success URL.
    """
    object_attr = 'id'
    success_url = 'index'
    permission_error_message = _(
        'You do not have permission to perform this action.'
    )

    def test_func(self):
        obj = self.get_object()
        obj_user_attr = getattr(obj, self.object_attr)
        user = self.request.user

        if isinstance(obj_user_attr, int):
            return obj_user_attr == user.id
        else:
            return getattr(obj_user_attr, 'id') == user.id

    def handle_no_permission(self):
        messages.add_message(
            self.request,
            messages.ERROR,
            self.permission_error_message
        )
        return redirect(self.success_url)


class ProtectedErrorHandlingMixin:
    success_url = 'index'
    protected_error_message = _(
        'Cannot delete this object because it is in use'
    )

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_error_message)
            return redirect(self.success_url)
