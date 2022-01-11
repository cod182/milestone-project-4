# Generated by Django 4.0 on 2022-01-09 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_alter_vehicleimages_image_alter_vehicleimages_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='gearbox',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('semi-automatic', 'Semi-Automatic')], max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicleimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles/'),
        ),
        migrations.AlterField(
            model_name='vehicleimages',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vehicleimages',
            name='vehicle_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle'),
        ),
    ]