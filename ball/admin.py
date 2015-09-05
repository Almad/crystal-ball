from django.contrib import admin

from ball.models import (
    Company,
    Team,
    GithubTeam,
    Member,
    Service,
)

admin.site.register(Company)
admin.site.register(Team)
admin.site.register(GithubTeam)
admin.site.register(Member)
admin.site.register(Service)
