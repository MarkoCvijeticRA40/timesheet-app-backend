# Generated by Django 5.0.2 on 2024-02-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0013_rename_user_task_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]