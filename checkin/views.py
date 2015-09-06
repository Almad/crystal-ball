""" Views for the checkin application """

from datetime import datetime
import os

from ipware.ip import get_real_ip
import pytz
from tzwhere import tzwhere

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geoip import GeoIP

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

    saved_current_time = datetime.now(profile.current_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    ip = get_real_ip(request)
    if os.getenv('IP_OVERRIDE'):
        ip = os.getenv('IP_OVERRIDE')

    if ip is None:
        ip = current_location = None
        current_timezone = current_time = current_location = 'Unknown'
    else:
        geoip = GeoIP()
        tzw = tzwhere.tzwhere()
        location_info = geoip.city(ip)

        if location_info is None:
            ip = current_location = None
            current_timezone = current_time = current_location = 'Unknown'
        else:
            current_location = location_info['city']
            current_timezone = pytz.timezone(tzw.tzNameAt(*geoip.lat_lon(ip)))
            
            current_time = datetime.now(current_timezone).strftime("%Y-%m-%d %H:%M:%S")

    return render(request, 'checkin/home.html', {
            'profile': profile,
            'checkins': checkins,
            'saved_current_time': saved_current_time,
            'current_location': current_location,
            'current_timezone': current_timezone,
            'current_time': current_time,
        })
