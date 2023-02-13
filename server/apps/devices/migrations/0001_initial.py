# Generated by Django 4.1.6 on 2023-02-13 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200)),
                ('node_type', models.CharField(choices=[('motion detect', 'MotionDetect'), ('gateway', 'Gateway')], default='motion detect', max_length=200)),
                ('api_key', models.CharField(editable=False, max_length=150)),
                ('status', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active'), ('enable', 'Enable'), ('disable', 'Disable')], default='enable', max_length=50)),
                ('suc_conv_num', models.PositiveIntegerField(default=0)),
                ('failed_conv_num', models.PositiveIntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_login_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Devices',
                'verbose_name_plural': 'Devices',
                'ordering': ('-created_time',),
            },
        ),
    ]