# Generated by Django 3.1.3 on 2020-11-14 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_remove_task_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='subjects.subject'),
        ),
    ]
