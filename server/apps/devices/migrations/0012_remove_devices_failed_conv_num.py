# Generated by Django 4.1.4 on 2023-02-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_rename_device_key_devices_api_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='failed_conv_num',
        ),
    ]