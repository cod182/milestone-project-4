# Generated by Django 4.0 on 2021-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='engine_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(),
        ),
    ]