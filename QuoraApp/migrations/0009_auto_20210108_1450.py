# Generated by Django 3.1.4 on 2021-01-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0008_auto_20210108_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
