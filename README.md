# Flask REST API App

## About:
This is Flask restful application which exposes player.csv file to rest api. 

## Project Structure:
* flask_api directory - contains the following files: ``app.py`` - the main file which run the app, ``requirements.txt`` - pre requisites packages, ``player.csv`` - the database of the application, ``README.md`` - about.
  * ``src`` package - contains the resources and configuration.
    * ``resorces`` package - contains the api resources
    * ``config`` package - contains the configuration classes of the app
  * ``tests`` package - contains unit testing.

## Endpoints:
* endpoint: ``http://127.0.0.1/player/<playerID>``, method: ``GET``, expected response (if found player): json which contain player attributes
* endpoint: ``http://127.0.0.1/players``, method: ``GET``, expected response: list of all the players

## Setup:

### Setup Locally:
1. Install Python
2. Run ``pip install -r requirements.txt``
3. For test locally from the flask_api dir run: ``python -m unittest -v tests/test_api.py``
4. For run the from the flask_api dir run: ``python ./app.py``

### Setup using Docker:
1. Install Docker
2. For create the environment use: ``docker compose up``
3. For clean up the environment use: ``docker compose down``


## Deployment:
I deployed it to ec2 and create for this project full AWS environment using ``ansible`` as deployment tool. 
I used another repo as deployment [repo](https://github.com/shaharkozi/ansible) and elaborated more there on how I deployed it to AWS.

## Assumptions:
1. In the instructions write duplicate endpoint, the same one for players and player. I made assumption which it by mistake and split it.
2. I made assumption that file can change during runtime, so I did 2 actions: 
   1) Read the csv file in each request.
   2) Mount the csv file when using docker.

