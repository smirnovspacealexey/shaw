# Generated by Django 3.2.4 on 2023-04-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SberSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('min_amount', models.IntegerField(default=500, verbose_name='минимальная сумма заказа')),
                ('max_amount', models.IntegerField(default=10000, verbose_name='максимальная сумма заказа')),
                ('tax_system', models.CharField(choices=[('0', 'общая'), ('1', 'упрощённая, доход'), ('2', 'упрощённая, доход минус расход'), ('3', 'единый налог на вменённый доход'), ('4', 'единый сельскохозяйственный налог'), ('5', 'патентная система налогообложения')], max_length=1)),
                ('in_test', models.BooleanField(default=False, verbose_name='тестовый режим')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'Настройки Сбера',
                'verbose_name_plural': 'Настройки Сбера',
            },
        ),
    ]
