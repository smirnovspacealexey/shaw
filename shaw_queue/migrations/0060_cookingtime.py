# Generated by Django 3.2.4 on 2022-11-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaw_queue', '0059_alter_deliveryorder_prefered_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField(verbose_name='минуты на готовку')),
                ('categories', models.ManyToManyField(to='shaw_queue.MenuCategory', verbose_name='Категории')),
                ('products', models.ManyToManyField(to='shaw_queue.Menu', verbose_name='Товары')),
            ],
        ),
    ]
