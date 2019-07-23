# Generated by Django 2.2.3 on 2019-07-15 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_request_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='phoneno',
            field=models.CharField(error_messages={'invalid': 'this field is required'}, max_length=14, validators=[django.core.validators.RegexValidator(regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')], verbose_name='Phone Number'),
        ),
    ]
