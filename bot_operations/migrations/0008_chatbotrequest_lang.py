# Generated by Django 2.2 on 2021-01-30 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_operations', '0007_chatbotrequest_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotrequest',
            name='lang',
            field=models.CharField(default='FR', max_length=12),
        ),
    ]
