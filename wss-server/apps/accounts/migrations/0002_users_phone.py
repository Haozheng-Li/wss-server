# Generated by Django 4.1.7 on 2023-04-01 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
