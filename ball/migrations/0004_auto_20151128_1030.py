# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octoball', '0001_initial'),
        ('ball', '0003_auto_20151127_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githuborganisation',
            name='company',
        ),
        migrations.RemoveField(
            model_name='githubteam',
            name='team',
        ),
        migrations.AddField(
            model_name='company',
            name='github_organisation',
            field=models.ForeignKey(to='octoball.Organisation', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='github_team',
            field=models.ForeignKey(to='octoball.Team', null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='GithubOrganisation',
        ),
        migrations.DeleteModel(
            name='GithubTeam',
        ),
    ]
