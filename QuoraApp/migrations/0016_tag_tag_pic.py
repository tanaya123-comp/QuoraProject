# Generated by Django 3.1.4 on 2021-01-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0015_auto_20210109_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
