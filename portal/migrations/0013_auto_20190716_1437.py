# Generated by Django 2.2.3 on 2019-07-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_request_is_requesting_for_others'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('l0', 'level-1-SuperAdmin'), ('l2', 'level-2-Manager '), ('l3', 'level-3-Volunteers'), ('l4', 'level-4-Normal Users')], default='l4', max_length=15, verbose_name='Type of User'),
        ),
    ]