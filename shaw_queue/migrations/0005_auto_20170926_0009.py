# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-25 19:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw_queue', '0004_order_printed'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='guid_1c',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]