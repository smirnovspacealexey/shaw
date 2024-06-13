# Generated by Django 3.2.4 on 2023-04-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default='30569379-1c26-49fa-b049-602beb30c6fe', max_length=200)),
                ('six_numbers', models.CharField(default='273849', max_length=200, verbose_name='код для курьера')),
            ],
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='assign_robot',
            field=models.BooleanField(default=False, help_text='Пытаться ли назначить заказ на ровер (шестиколесный робот)', verbose_name='assign_robot'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='auto_courier',
            field=models.BooleanField(default=False, help_text='курьер только на машине', verbose_name='auto_courier'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='currency',
            field=models.CharField(default='RUB', help_text='Валюта расчёта', max_length=200),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='currency_sign',
            field=models.CharField(default='₽', help_text='Знак валюты', max_length=200),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='emergency_contact_name',
            field=models.CharField(default='', help_text='Имя контактного лица', max_length=200, verbose_name='emergency_contact_name'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='emergency_contact_phone',
            field=models.CharField(default='', help_text='Телефон контактного лица', max_length=200, verbose_name='emergency_contact_phone'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='optional_return',
            field=models.BooleanField(default=False, help_text='Не требуется возврат товаров в случае отмены заказа. true - курьер оставляет товар себе, false - по умолчанию, требуется вернуть товар', verbose_name='optional_return'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='pro_courier',
            field=models.BooleanField(default=False, help_text='Опция "Профи" для тарифов "Экспресс" и "Курьер"', verbose_name='pro_courier'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='referral_source',
            field=models.CharField(default='', help_text='Источник заявки (можно передать наименование CMS, из которой создается запрос)', max_length=200, verbose_name='emergency_contact_phone'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='skip_act',
            field=models.BooleanField(default=False, help_text='Не показывать акт'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='skip_client_notify',
            field=models.BooleanField(default=False, help_text='Не отправлять отправителю/получателю смс-нотификации, когда к нему направится курьер.'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='skip_confirmation',
            field=models.BooleanField(default=False, help_text='Пропускать подтверждение через SMS в данной точке. False - подтверждение требуется', verbose_name='skip_confirmation'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='skip_door_to_door',
            field=models.BooleanField(default=False, help_text='Отказ от доставки до двери (выключить опцию "От двери до двери").'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='skip_emergency_notify',
            field=models.BooleanField(default=False, help_text='Не отправлять нотификации emergency контакту'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='taxi_class',
            field=models.CharField(choices=[('courier', 'courier'), ('express', 'express'), ('cargo', 'cargo')], default='courier', help_text='Класс такси. Возможные значения: courier, express, cargo', max_length=200, verbose_name='taxi_class'),
        ),
        migrations.AddField(
            model_name='yandexsettings',
            name='thermobag',
            field=models.BooleanField(default=True, help_text='курьер с термосумкой', verbose_name='thermobag'),
        ),
    ]