# Generated by Django 5.0.1 on 2024-02-09 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_alter_client_address_alter_client_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.CharField(choices=[('Archive', 'Archive'), ('Active', 'Active'), ('Inactive', 'Inactive')], max_length=8)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheet.client')),
            ],
        ),
    ]
