""" Views for the base application """

from django.shortcuts import render

from allauth.socialaccount.models import SocialAccount


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')


def integrations_setup(request):
    try:
        github_account = request.user.socialaccount_set.get(provider='github')
    except SocialAccount.DoesNotExist:
        github_account = None

    return render(request, 'base/integrations_setup.html', {
        'github_account': github_account
    })

