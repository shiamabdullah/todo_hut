# Generated by Django 3.2.8 on 2021-10-29 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='slug',
        ),
    ]
