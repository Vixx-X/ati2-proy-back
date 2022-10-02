# Generated by Django 4.0.1 on 2022-10-02 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Official name')),
            ],
            options={
                'verbose_name': 'Continent',
                'verbose_name_plural': 'Continents',
                'db_table': 'continents',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_3166_1_a2', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='ISO 3166-1 alpha-2')),
                ('iso_3166_1_a3', models.CharField(blank=True, max_length=3, verbose_name='ISO 3166-1 alpha-3')),
                ('iso_3166_1_numeric', models.CharField(blank=True, max_length=3, verbose_name='ISO 3166-1 numeric')),
                ('printable_name', models.CharField(db_index=True, max_length=128, verbose_name='Country name')),
                ('name', models.CharField(max_length=128, verbose_name='Official name')),
                ('display_order', models.PositiveSmallIntegerField(db_index=True, default=0, help_text='Higher the number, higher the country in the list.', verbose_name='Display order')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='address.continent', verbose_name='Continent')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
                'ordering': ('-display_order', 'printable_name'),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Official name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='address.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'db_table': 'states',
                'ordering': ('name',),
                'unique_together': {('name', 'country')},
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Official name')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='address.state', verbose_name='State')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'cities',
                'ordering': ('name',),
                'unique_together': {('name', 'state')},
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=255, verbose_name='First line of address')),
                ('line2', models.CharField(blank=True, max_length=255, verbose_name='Second line of address')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'addresses',
            },
        ),
    ]
