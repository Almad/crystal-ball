from django.contrib import admin

from octoball.models import (
    Organisation,
    Team,
)

admin.site.register(Team)
admin.site.register(Organisation)
