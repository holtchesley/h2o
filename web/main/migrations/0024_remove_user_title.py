# Generated by Django 2.2.9 on 2019-12-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20191219_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]