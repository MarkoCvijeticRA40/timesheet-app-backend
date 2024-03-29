# Generated by Django 5.0.1 on 2024-02-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_rename_postalcode_client_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='postal_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
