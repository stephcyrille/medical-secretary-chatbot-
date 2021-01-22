# Generated by Django 2.2 on 2021-01-22 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBotRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=36, unique=True)),
                ('transId', models.CharField(default='', max_length=50)),
                ('operation', models.CharField(default='', max_length=12)),
                ('is_active', models.BooleanField(default=False)),
                ('change_credentials', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('lang', models.CharField(default='EN', max_length=12)),
                ('ussd_code', models.CharField(default='', max_length=4)),
                ('msisdn', models.CharField(default='', max_length=50)),
                ('expeditor_name', models.CharField(default='', max_length=200)),
                ('destinator_name', models.CharField(default='', max_length=200)),
                ('destination_number', models.CharField(default='', max_length=12)),
                ('transaction_code', models.CharField(default='', max_length=12)),
                ('bundle_code', models.CharField(blank=True, max_length=6, null=True)),
                ('bundle_category', models.CharField(blank=True, max_length=6, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=15, null=True)),
                ('contract_number', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_list', models.CharField(default='', max_length=250)),
                ('amount', models.IntegerField(default=0)),
                ('fees', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('destinator_full_name', models.CharField(default='', max_length=12)),
                ('airtime_transaction_code', models.CharField(default='', max_length=50)),
                ('airtime_response_code', models.CharField(default='', max_length=50)),
                ('airtime_balance', models.CharField(default='', max_length=50)),
                ('airtime_description', models.CharField(default='', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('menu_step_name', models.CharField(default='', max_length=50)),
                ('menu_step', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('start_session_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('end_session_time', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
    ]
