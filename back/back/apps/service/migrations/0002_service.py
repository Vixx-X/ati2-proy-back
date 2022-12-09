# Generated by Django 4.0.1 on 2022-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'db_table': 'services',
                'ordering': ('name',),
            },
        ),
    ]