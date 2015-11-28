from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from timezone_field import TimeZoneField

from octoball.models import (
    Organisation,
    Team as GithubTeam
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    current_location = models.CharField(max_length=100, default='Prague')
    current_timezone = TimeZoneField(default='Europe/Prague')


class Company(models.Model):
    """ Name of the top-level company """
    name = models.CharField(max_length=255)
    github_organisation = models.ForeignKey(Organisation, null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    """ Team within the company. May be recursive. """
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, null=True)
    parent_team = models.ForeignKey("self", blank=True, null=True)
    github_team = models.ForeignKey(GithubTeam, blank=True, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    date_joined = models.DateField('Date the Member joined the Company')

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    github_repository = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AllowedGoogleDomain(models.Model):
    """ For purpose of SSO login, which domains are allowed? """
    domain = models.CharField(max_length=255)
    site = models.ForeignKey(Site)

    def __str__(self):
        return self.domain
