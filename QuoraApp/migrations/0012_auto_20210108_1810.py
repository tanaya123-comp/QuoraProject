# Generated by Django 3.1.4 on 2021-01-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0011_auto_20210108_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='profiles/'),
        ),
    ]
