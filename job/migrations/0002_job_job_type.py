# Generated by Django 4.0.4 on 2022-05-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
