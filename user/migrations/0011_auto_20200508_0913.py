# Generated by Django 3.0.5 on 2020-05-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image2',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Upload Client Image'),
        ),
    ]
