# Generated by Django 4.1.7 on 2023-02-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(choices=[(True, 'Zrobione'), (False, 'Niezrobione')], default=False),
        ),
    ]
