from django.db import models
from task_manager.user.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(
        Status,
        related_name='tasks',
        on_delete=models.PROTECT,
        verbose_name=_('Status'))
    executor = models.ForeignKey(
        User,
        related_name='assigned_tasks',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Executor'))
    labels = models.ManyToManyField(
        Label,
        through='TaskLabel',
        related_name='task_labels',
        blank=True,
        verbose_name=_('Labels'))
    author = models.ForeignKey(
        User,
        related_name='created_tasks',
        on_delete=models.PROTECT,
        verbose_name=_('Author'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('Task')

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('task', 'label')
