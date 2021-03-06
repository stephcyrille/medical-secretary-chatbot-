# Generated by Django 2.2 on 2021-01-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_operations', '0004_chatbotrequest_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='bundle_category',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='bundle_code',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='change_credentials',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='contract_number',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='destination_number',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='destinator_full_name',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='destinator_name',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='expeditor_name',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='invoice_number',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='is_agent',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='is_user',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='level',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='msisdn',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='phone_list',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='transaction_code',
        ),
        migrations.RemoveField(
            model_name='chatbotrequest',
            name='ussd_code',
        ),
        migrations.AddField(
            model_name='chatbotrequest',
            name='ache_zone',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='chatbotrequest',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='chatbotrequest',
            name='medical_background',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='chatbotrequest',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='chatbotrequest',
            name='symptoms',
            field=models.CharField(default='', max_length=150),
        ),
    ]
