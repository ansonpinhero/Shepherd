# Generated by Django 2.2.3 on 2019-07-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20190716_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_requesting_for_others',
            field=models.BooleanField(default=False, verbose_name='Requesting for others'),
        ),
    ]
