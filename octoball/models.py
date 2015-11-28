from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=255)


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s from %s" % (self.name, self.team)
