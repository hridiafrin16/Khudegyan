# Generated by Django 5.2 on 2025-04-30 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_by',
        ),
    ]
