# Generated by Django 3.1.4 on 2021-01-31 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0024_auto_20210131_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='answer',
            order_with_respect_to='question',
        ),
    ]
