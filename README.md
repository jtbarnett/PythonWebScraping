# Python web scraping script deployed with Docker

Built with Python version 3.9.1 and Docker version 20.10.0.

## Purpose

This script searches the top movies on IMDB (http://www.imdb.com/chart/top) and recommends one to you.

## Build and Run

To build with Dockerfile run `docker build -t IMAGE-NAME .` in your terminal. To run the Docker Image run `docker run -t -i IMAGE-NAME` in your terminal and make sure to inclide `-t -i` to enable the terminal and make it interactive.