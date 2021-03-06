# Generated by Django 2.2.3 on 2019-07-23 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20190716_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteer_invitations',
            fields=[
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(choices=[('s1', 'Case Resolved'), ('s2', 'Case Assigned to a volunteer '), ('s3', 'Case under process'), ('s4', 'Case Open')], default='s4', max_length=15, verbose_name='Current Status')),
            ],
        ),
    ]
