# Generated by Django 5.0.6 on 2024-05-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/default.jpg', upload_to='profile_pick'),
        ),
    ]
