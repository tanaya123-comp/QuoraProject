# Generated by Django 3.1.4 on 2021-01-31 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0023_auto_20210130_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['question']},
        ),
    ]