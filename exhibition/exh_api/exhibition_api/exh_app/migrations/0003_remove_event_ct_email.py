# Generated by Django 3.2.6 on 2023-12-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exh_app', '0002_alter_event_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='ct_email',
        ),
    ]
