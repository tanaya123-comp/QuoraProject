# Generated by Django 3.1.4 on 2021-01-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0009_auto_20210108_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profiles/default_profile.png', null=True, upload_to='profiles/'),
        ),
    ]
