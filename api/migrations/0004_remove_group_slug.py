# Generated by Django 3.1.2 on 2020-10-18 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]