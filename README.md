# Crystall Ball ![build status](https://circleci.com/gh/Almad/crystal-ball.svg?style=shield&circle-token=29702d6a0400c8207e970c20b5fb78510a039e74)

> Do you know where this is?

> Do I have a crystall ball or what?

-- Unknown Developers

## Installation

`docker-compose run web python manage.py syncdb`

After altering dependency chain (like adding a line to `requirements.txt`), run 

`docker-compose build web`


## Running

`django-compose up`

See browser at [http://localhost:8000](http://localhost:8000)

## Testing

`docker-compose run --rm --user "$(id -u):$(id -g)" web python3 manage.py test`
