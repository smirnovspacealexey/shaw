# Generated by Django 3.2.4 on 2023-02-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw_queue', '0067_rename_datetime_cookingtimerordercontent_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercontent',
            name='qr',
            field=models.CharField(default='', max_length=500),
        ),
    ]
