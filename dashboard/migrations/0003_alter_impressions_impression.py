# Generated by Django 4.1.7 on 2023-07-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_impressions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impressions',
            name='impression',
            field=models.TextField(max_length=1000000),
        ),
    ]
