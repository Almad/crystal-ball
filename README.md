# Crystall Ball ![build status](https://circleci.com/gh/Almad/crystal-ball.svg?style=shield&circle-token=29702d6a0400c8207e970c20b5fb78510a039e74)

> Do you know where this is?

> Do I have a crystall ball or what?

-- Unknown Developers

## Big Fat Warning

This is not production ready #totes

Especially beware of:

* `django-allauth` is storing access tokens unecrypted. Given `crystal-ball` needs _very_ high privileges for its magic, **this puts all your GitHub data at risk!**

## Installation

`cp crystal_ball/settings/local-dist.py crystal_ball/settings/local.py`

Look into local settings.

`docker-compose run web python manage.py syncdb`

After altering dependency chain (like adding a line to `requirements.txt`), run 

`docker-compose build web`

## Running

`django-compose up`

See browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Initial set up

**to be automated...**

1. Head to [Google Developer Console](https://console.developers.google.com), create a new project for your installation or development, go to "API Manager" -> "Credentials" -> Add Credentials on that project, select "OAuth 2.0 Client ID", "Web Application" and use `http://127.0.0.1:8000/accounts/google/login/callback/` for "Authorized redirect URIs".

1. Go to [your django admin](http://127.0.0.1:8000/admin/) and login with credentials you've entered during `syncdb` step

	1. Go to "Sites", click on existing "example.com" site and change the domain name to `127.0.0.1:8000` (or wherever you are running)

	1. Go to "Social applications" and add a new application with Google as a provider, credentials you've received from Google Developer Console and connected with the site from previous step

## Development

After altering dependency chain (like adding a line to `requirements.txt`), run 

`docker-compose build web`


After modifying `models.py`:

`docker-compose run --rm --user "$(id -u):$(id -g)" web python manage.py makemigrations`
`docker-compose run --rm --user "$(id -u):$(id -g)" web python manage.py migrate`

## Testing

`docker-compose run --rm --user "$(id -u):$(id -g)" web python3 manage.py test`

If you want to test with different IP addresses at runtime, add line like

`IP_OVERRIDE=8.8.8.8`

to file called `.env` that is in the root of the repository, and add `env_file: .env` to your `docker-compose.yml` (if you have better way how to propagate environment variables downstream, please let me know).

## Attribution

This product includes GeoLite data created by MaxMind, available from 
[MaxMind](http://www.maxmind.com).
