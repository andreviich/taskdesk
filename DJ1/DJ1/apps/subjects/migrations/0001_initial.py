# Generated by Django 3.1.3 on 2020-11-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField(verbose_name='Текст дз')),
                ('expire', models.DateTimeField(verbose_name='Дедлайн')),
            ],
            options={
                'verbose_name': 'Домашнее задание по математике',
                'verbose_name_plural': 'Домашние задания по математике',
            },
        ),
    ]
