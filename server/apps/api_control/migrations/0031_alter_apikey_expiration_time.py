# Generated by Django 4.1.4 on 2023-02-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_control', '0030_alter_apikey_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
