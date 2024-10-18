from django.db import models
from django.utils import timezone
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.label.models import Label


class TaskLabel(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)


class Task(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='tasks',
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='assigned_tasks',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='created_tasks'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
