# Generated by Django 4.1.4 on 2023-02-28 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_remove_devices_failed_conv_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devices',
            options={'ordering': ('-created_time',), 'verbose_name': 'devices', 'verbose_name_plural': 'devices'},
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.DecimalField(decimal_places=1, max_digits=5)),
                ('mem_rate', models.DecimalField(decimal_places=1, max_digits=5)),
                ('disk_rate', models.DecimalField(decimal_places=1, max_digits=5)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.devices')),
            ],
            options={
                'verbose_name': 'performance',
                'verbose_name_plural': 'performance',
                'ordering': ('-created_time',),
            },
        ),
    ]