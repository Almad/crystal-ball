from django.db import models

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
