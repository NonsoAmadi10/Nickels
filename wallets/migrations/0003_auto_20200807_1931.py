# Generated by Django 3.0.8 on 2020-08-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_auto_20200726_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_address',
            field=models.CharField(default='xz7FsOgAfq', max_length=10, unique=True),
        ),
    ]
