# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-12 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw_queue', '0038_auto_20200209_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_by_weight',
            field=models.BooleanField(default=False, verbose_name='На развес'),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='prefered_payment',
            field=models.CharField(choices=[('CSH', 'Наличные'), ('CLS', 'Безнал'), ('MXD', 'Смешанная')], default='CSH', max_length=3, verbose_name='Вид оплаты'),
        ),
    ]
