# Generated by Django 3.2.5 on 2021-08-31 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_disease_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='plant_disease',
            field=models.CharField(default='', max_length=30),
        ),
    ]
