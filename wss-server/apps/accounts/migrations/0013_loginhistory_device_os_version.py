# Generated by Django 4.1.7 on 2023-04-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_loginhistory_login_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginhistory',
            name='device_os_version',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
