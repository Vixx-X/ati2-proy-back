# Generated by Django 4.0.1 on 2022-10-02 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otp_email', '0004_throttling'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDevice',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('otp_email.emaildevice',),
        ),
    ]
