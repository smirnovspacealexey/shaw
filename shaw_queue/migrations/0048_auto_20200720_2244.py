# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-07-20 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shaw_queue', '0047_auto_20200614_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_title', models.CharField(default='', max_length=200, verbose_name='Название для покупателя')),
            ],
        ),
        migrations.CreateModel(
            name='MacroProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_title', models.CharField(default='', max_length=200, verbose_name='Название для покупателя')),
            ],
        ),
        migrations.CreateModel(
            name='OrderContentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.OrderContent', verbose_name='Товар из заказа')),
                ('content_item_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_item_option', to='shaw_queue.OrderContent', verbose_name='Доп к товару из заказа')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_title', models.CharField(default='', max_length=200, verbose_name='Название для покупателя')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_title', models.CharField(default='', max_length=200, verbose_name='Название для покупателя')),
                ('content_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.ContentOption', verbose_name='Вариант содержимого')),
                ('macro_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.MacroProduct', verbose_name='Макротовар')),
            ],
        ),
        migrations.CreateModel(
            name='SizeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_title', models.CharField(default='', max_length=200, verbose_name='Название для покупателя')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='img/icons', verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.Menu', verbose_name='Товар из меню 1С'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.SizeOption', verbose_name='Вариант размера'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.Menu', verbose_name='Товар из меню 1С'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shaw_queue.ProductVariant', verbose_name='Вариант товара'),
        ),
    ]
