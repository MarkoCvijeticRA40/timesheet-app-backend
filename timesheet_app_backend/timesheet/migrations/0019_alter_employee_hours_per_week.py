# Generated by Django 5.0.2 on 2024-02-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0018_alter_employee_email_alter_employee_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hours_per_week',
            field=models.IntegerField(default=0),
        ),
    ]