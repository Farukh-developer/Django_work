# Generated by Django 5.0.6 on 2024-05-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(null=True, upload_to='country_images/'),
        ),
    ]
