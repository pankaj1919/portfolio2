# Generated by Django 3.0.5 on 2020-05-12 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_email_confirmed'),
        ('home', '0002_home_third'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
    ]
