# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ball', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='Prague', max_length=100)),
                ('timezone', timezone_field.fields.TimeZoneField(default='Europe/Prague')),
                ('time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.OneToOneField(to='ball.UserProfile')),
            ],
        ),
    ]
