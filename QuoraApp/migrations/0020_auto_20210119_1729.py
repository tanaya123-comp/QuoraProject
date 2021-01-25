# Generated by Django 3.1.5 on 2021-01-19 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraApp', '0019_auto_20210119_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QuoraApp.answer'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='votedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QuoraApp.member'),
        ),
    ]