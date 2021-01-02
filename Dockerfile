# Dockerfile (blueprint for building an Image), Image (template for running Containers), Container (the running process where we have our package project)
FROM python:3.9

ADD MovieFinder.py .

RUN pip install requests beautifulsoup4

CMD [ "python", "./MovieFinder.py" ]