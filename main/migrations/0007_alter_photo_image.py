# Generated by Django 5.0.2 on 2024-07-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_photo_description_property_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(default='', upload_to='photos/'),
        ),
    ]
