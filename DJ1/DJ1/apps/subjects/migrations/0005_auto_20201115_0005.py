# Generated by Django 3.1.3 on 2020-11-14 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_remove_it_expire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.TextField(verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField(verbose_name='Текст дз')),
                ('expire', models.DateTimeField(verbose_name='Дедлайн')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.DeleteModel(
            name='Communication',
        ),
        migrations.DeleteModel(
            name='ComputerPractice',
        ),
        migrations.DeleteModel(
            name='Economics',
        ),
        migrations.DeleteModel(
            name='IT',
        ),
        migrations.DeleteModel(
            name='Management',
        ),
        migrations.DeleteModel(
            name='Math',
        ),
    ]
