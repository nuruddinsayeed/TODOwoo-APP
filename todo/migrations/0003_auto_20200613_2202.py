# Generated by Django 3.0.7 on 2020-06-13 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200610_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='importent',
            new_name='important',
        ),
    ]
