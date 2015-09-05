FROM django:python3
ENV PYTHONUNBUFFERED 1

# is there only because we are using Makefile for sphinx build
# might be worth removing
RUN apt-get update && apt-get install -y build-essential

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
