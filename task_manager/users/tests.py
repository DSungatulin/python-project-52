import unittest
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from .models import User
from django.contrib.messages import get_messages

# Create your tests here.

class MyTestSuite(unittest.TestSuite):
    def __init__(self):
        super(MyTestSuite, self).__init__()
        self.addTest(SetUpTestCase('test_set_up'))
        self.addTest(UsersListTest('users_list_test'))
        self.addTest(UpdateUserTest('update_user_test_success'))
        self.addTest(DeleteUserTest('delete_user_test_success'))


class SetUpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Ivan', last_name='Ivanov',
            username='Sample'
        )
        self.user.set_password('797c5f34e00145b')
        self.user.save()

        self.client.login(
            username='Sample', password='797c5f34e00145b',
        )


class UsersListTest(TestCase):
    def test_index(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        c = Client()
        response = c.post('/users/create/', {
            'first_name': 'Semyon',
            'last_name': 'Semyonov',
            'username': 'Sema123',
            'password1': 'b6e5359809ec5953837df0ba346a26fd',
            'password2': 'b6e5359809ec5953837df0ba346a26fd',
        })
        self.assertEqual(response.status_code, 302)

    def test_login_user(self):
        c = Client()
        response = c.post('/login/', {
            'username': 'Sema123',
            'password': 'b6e5359809ec5953837df0ba346a26fd',
        })
        self.assertEqual(response.status_code, 200)


class UpdateUserTest(SetUpTestCase):
     def test_user_update_success(self):
        response = self.client.post(
            reverse_lazy('user-update', kwargs={'pk': self.user.pk}),
            {'first_name': 'Ivan', 'last_name': 'Ivanov',
             'username': 'Sample_for_docs', 'password1': '797c5f34e00145b',
             'password2': '797c5f34e00145b'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users-detail'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'User is successfully updated',
            'Профиль пользователя успешно изменен',
        ])


class DeleteUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='John', last_name='Wick',
            username='DJovanovich'
        )
        self.user.set_password('Ditya_Belarusi')
        self.user.save()

        self.client.login(
            username='DJovanovich', password='Ditya_Belarusi',
        )

    def test_user_delete_success(self):
        response = self.client.post(
            reverse_lazy('user-delete', kwargs={'pk': self.user.pk}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users-detail'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'User successfully deleted',
            'Пользователь успешно удален',
        ])


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(MyTestSuite())