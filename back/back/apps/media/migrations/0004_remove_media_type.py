# Generated by Django 4.0.1 on 2022-12-05 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_alter_media_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='type',
        ),
    ]