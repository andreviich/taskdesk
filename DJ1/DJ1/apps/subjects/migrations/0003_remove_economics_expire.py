# Generated by Django 3.1.3 on 2020-11-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_communication_computerpractice_economics_it_management'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economics',
            name='expire',
        ),
    ]
