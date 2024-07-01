from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from .models import Label
# Create your tests here.


class SetUpTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='Dominic', last_name='Toretto',
            username='Real_driver',
        )
        self.user.set_password('F@mily_is_everith1ng')
        self.user.save()

        self.user2 = User.objects.create(
            first_name='Brian', last_name='O\'Conner',
            username='I_choose_Supra',
        )
        self.user2.set_password('Orange_supra1')
        self.user2.save()

        self.status = Status.objects.create(name='status')
        self.status.save()

        self.label = Label.objects.create(name='IMPORTANT')
        self.label.save()

        self.task = Task.objects.create(
            name='Work hard',
            description='The only way to win',
            status=Status.objects.get(pk=self.status.pk),
            executor=User.objects.get(pk=self.user.pk),
            author=self.user
        )
        self.client.login(
            username='Real_driver', password='F@mily_is_everith1ng',
        )


class LabelCreateTest(SetUpTestCase):
    def test_label_create_view(self):
        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_label_create_success(self):
        response = self.client.post(reverse_lazy('label_create'), {
            'name': 'oracle_db',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_detail'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully created',
            'Метка успешно создана',
        ])


class LabelUpdateTest(SetUpTestCase):
    def test_label_update_view(self):
        response = self.client.get(reverse_lazy('label_update', kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_label_update_success(self):
        response = self.client.post(reverse_lazy('label_update', kwargs={'pk': self.label.pk}), {
            'name': 'NOT IMPORTANT',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_detail'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully updated',
            'Метка успешно обновлена'
        ])


class LabelDeleteTest(SetUpTestCase):
    def test_label_delete_view(self):
        response = self.client.get(reverse_lazy('label_delete', kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='delete.html')

    def test_label_delete_success(self):
        response = self.client.post(reverse_lazy('label_delete', kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_detail'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully deleted',
            'Метка успешно удалена'
        ])
