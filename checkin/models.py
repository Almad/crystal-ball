from django.db import models
from django.contrib.sites.models import Site

from timezone_field import TimeZoneField

from ball.models import UserProfile

class CheckIn(models.Model):
    """ I represent check in made by user on some location """
    user_profile = models.OneToOneField(UserProfile)
    location = models.CharField(max_length=100, default='Prague')
    timezone = TimeZoneField(default='Europe/Prague')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s at %s on %s" % (self.user, self.location, self.time)

    def save(self):
        """
        Save myself as well as update my current timezone/location to the
        parent user profile
        """
        self.user_profile.current_location = self.location
        self.user_profile.current_timezone = self.timezone

        super(CheckIn, self).save(*args, **kwargs)
