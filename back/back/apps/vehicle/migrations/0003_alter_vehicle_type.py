# Generated by Django 4.0.1 on 2022-12-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_vehicle_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('CAR', 'Car'), ('SUV', 'SUV'), ('TRUCK', 'Truck')], max_length=8, null=True, verbose_name='type'),
        ),
    ]
