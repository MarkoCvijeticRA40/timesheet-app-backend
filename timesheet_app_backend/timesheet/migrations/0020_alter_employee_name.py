# Generated by Django 5.0.1 on 2024-02-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0019_alter_employee_hours_per_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
