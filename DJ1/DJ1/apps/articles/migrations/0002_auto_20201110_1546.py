# Generated by Django 3.1.3 on 2020-11-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commment_text',
            new_name='comment_text',
        ),
    ]
