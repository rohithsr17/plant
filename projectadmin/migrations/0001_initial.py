# Generated by Django 3.2.5 on 2021-08-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soil_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=30)),
            ],
        ),
    ]
