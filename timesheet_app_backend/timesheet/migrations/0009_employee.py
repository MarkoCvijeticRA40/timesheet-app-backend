# Generated by Django 5.0.1 on 2024-02-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0008_alter_project_id_alter_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hours_per_week', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=255)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Worker', 'Worker')], max_length=255)),
            ],
        ),
    ]
