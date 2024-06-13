# Generated by Django 3.2.4 on 2023-05-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbersettings',
            name='callback_token',
            field=models.CharField(blank=True, choices=[('0', 'общая'), ('1', 'упрощённая, доход'), ('2', 'упрощённая, доход минус расход'), ('3', 'единый налог на вменённый доход'), ('4', 'единый сельскохозяйственный налог'), ('5', 'патентная система налогообложения')], default='', max_length=50, null=True),
        ),
    ]
