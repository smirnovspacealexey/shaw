# Generated by Django 3.2.4 on 2023-04-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_auto_20230416_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='delivery_menu',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='delivery_price',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='door_code',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='items',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='porch',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='sflat',
        ),
        migrations.RemoveField(
            model_name='deliveryhistory',
            name='sfloor',
        ),
    ]
