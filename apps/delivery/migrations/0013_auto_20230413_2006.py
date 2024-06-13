# Generated by Django 3.2.4 on 2023-04-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0012_deliverydistance_deliverysettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverydistance',
            name='km',
        ),
        migrations.AddField(
            model_name='deliverydistance',
            name='meters',
            field=models.IntegerField(default=0, verbose_name='метров'),
        ),
    ]