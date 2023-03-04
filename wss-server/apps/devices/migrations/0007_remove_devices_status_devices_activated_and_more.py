# Generated by Django 4.1.4 on 2023-02-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_alter_devices_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='status',
        ),
        migrations.AddField(
            model_name='devices',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='devices',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='devices',
            name='enable',
            field=models.BooleanField(default=False),
        ),
    ]