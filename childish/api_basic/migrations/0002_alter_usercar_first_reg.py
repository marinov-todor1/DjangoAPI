# Generated by Django 4.0 on 2022-04-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercar',
            name='first_reg',
            field=models.DateField(),
        ),
    ]