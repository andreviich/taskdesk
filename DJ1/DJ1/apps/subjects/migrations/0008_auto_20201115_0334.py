# Generated by Django 3.1.3 on 2020-11-15 00:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0007_auto_20201115_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expire',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дедлайн'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
        ),
    ]
