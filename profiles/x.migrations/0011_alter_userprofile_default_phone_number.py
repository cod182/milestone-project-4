# Generated by Django 4.0 on 2022-01-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_userprofile_default_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
