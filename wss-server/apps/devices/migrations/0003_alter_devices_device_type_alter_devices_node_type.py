# Generated by Django 4.1.4 on 2023-02-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_devices_device_type_devices_protocol_devices_sdk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_type',
            field=models.CharField(choices=[('raspberry_pi', 'Raspberry Pi')], default='Raspberry Pi', max_length=200),
        ),
        migrations.AlterField(
            model_name='devices',
            name='node_type',
            field=models.CharField(choices=[('motion_detect', 'MotionDetect'), ('gateway', 'Gateway')], default='motion detect', max_length=200),
        ),
    ]