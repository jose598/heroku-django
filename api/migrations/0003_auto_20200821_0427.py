# Generated by Django 3.0.5 on 2020-08-21 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200821_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_editor',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_supervisor',
            new_name='is_superuser',
        ),
    ]
