# Generated by Django 4.0 on 2021-12-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_available_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleimages',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]