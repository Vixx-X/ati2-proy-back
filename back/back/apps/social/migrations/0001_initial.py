# Generated by Django 4.0.1 on 2022-10-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Social name')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'db_table': 'socials',
                'ordering': ('name',),
            },
        ),
    ]