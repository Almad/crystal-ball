# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ball', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubOrganisation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(to='ball.Company')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='company',
            field=models.ForeignKey(to='ball.Company', null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='parent_team',
            field=models.ForeignKey(null=True, to='ball.Team', blank=True),
        ),
    ]
