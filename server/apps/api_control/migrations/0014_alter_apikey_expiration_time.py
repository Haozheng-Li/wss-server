# Generated by Django 4.1.6 on 2023-02-13 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_control', '0013_alter_apikey_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='expiration_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 12, 1, 35, 9, 253974, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
