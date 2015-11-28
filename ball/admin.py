from django.contrib import admin

from ball.models import (
    Company,
    Team,
    Member,
    Service,
    AllowedGoogleDomain,
)

admin.site.register(Company)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Service)
admin.site.register(AllowedGoogleDomain)
