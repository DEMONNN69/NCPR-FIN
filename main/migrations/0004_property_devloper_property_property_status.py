# Generated by Django 5.0.2 on 2024-07-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_property_map_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='devloper',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_status',
            field=models.CharField(choices=[('readytomove', 'House'), ('underconstrution', 'Under Construction')], max_length=50, null=True),
        ),
    ]
