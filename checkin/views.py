""" Views for the checkin application """

from datetime import datetime

import pytz

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ball.models import UserProfile

from .models import CheckIn

@login_required
def home(request):
    """ Default view for the root """
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(
            user = request.user
        )

    checkins = CheckIn.objects.order_by('-time')[:10]

    current_time = datetime.now(profile.current_timezone).strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)

    return render(request, 'checkin/home.html', {
            'profile': profile,
            'checkins': checkins,
            'current_time': current_time
        })
