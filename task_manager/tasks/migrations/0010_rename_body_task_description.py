# Generated by Django 5.0.4 on 2024-05-14 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_task_body_alter_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='body',
            new_name='description',
        ),
    ]