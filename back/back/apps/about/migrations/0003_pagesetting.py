# Generated by Django 4.0.1 on 2022-12-02 20:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_contactme_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='page email')),
                ('image_limit', models.IntegerField(default=10, verbose_name='image limit')),
                ('video_limit', models.IntegerField(default=5, verbose_name='video limit')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='phone number')),
                ('local_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='local phone number')),
            ],
            options={
                'verbose_name': 'page setting',
                'verbose_name_plural': 'page settings',
                'db_table': 'page_setting',
            },
        ),
    ]
