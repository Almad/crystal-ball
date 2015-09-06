from django.db import models
from django.contrib.sites.models import Site

class Company(models.Model):
    name = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)

class GithubTeam(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team)

class Member(models.Model):
    date_joined = models.DateField('Date the Member joined the Company')

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    github_repository = models.CharField(max_length=255)

class AllowedGoogleDomain(models.Model):
    """ For purpose of SSO login, which domains are allowed? """
    domain = models.CharField(max_length=255)
    site = models.ForeignKey(Site)

    def __str__(self):
        return self.domain
