# Generated by Django 3.1.4 on 2021-01-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0007_auto_20210107_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
