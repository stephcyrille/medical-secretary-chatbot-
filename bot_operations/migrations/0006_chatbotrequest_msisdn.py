# Generated by Django 2.2 on 2021-01-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_operations', '0005_auto_20210130_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotrequest',
            name='msisdn',
            field=models.CharField(default='', max_length=50),
        ),
    ]
