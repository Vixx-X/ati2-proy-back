# Generated by Django 4.0.1 on 2022-12-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_media_post_images_post_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_hour_end',
            field=models.TimeField(verbose_name='hour end'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_hour_start',
            field=models.TimeField(verbose_name='hour start'),
        ),
    ]
