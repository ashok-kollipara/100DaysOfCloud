# Day-24 : Part-1 - First Steps towards making a Resume API w/ Flask

## Introduction

- This project is part of Journey to understand and make a API two ways as mentioned in ![last post](../023/README.md)
    - to have a better understanding of the backend of API with 
        - databases
        - caching
        - rate limiting
        - authorization

- Final version is to establish a End to end version with CI/CD as per ![cloud resume challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) but in classic architecture on EC2 / ECS as python app

## Prerequisite

I find that a beginner level exposure to below topics will be ideal, although there is documentation always at hand for these topic

- Python
    - Decorators
    - Classes

- HTTP Methods
- NoSQL databases
    - MongoDB
    - Redis

## Use Case

- Showcase resume as API with demonstration of technical skills necessary to implement them both in classical and serverless architecture

## Cloud Research

I have gone through the below topics for reference 

- ![Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/)
- ![SaaS learnings - Interesting read](https://12factor.net/)
- ![Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- ![Flask Limiter Documentation](https://flask-limiter.readthedocs.io/en/stable/)
- ![Redis with Python](https://docs.redis.com/latest/rs/references/client_references/client_python/)

## Hands On - Today

- Setting up EC2 with MongoDB and Redis

- Add rate limiting to API

- Establising, populating and retrieving data from MongoDB atlas sandbox

**Code current stage**

![Check out the specific repo](https://github.com/ashok-kollipara/quick-resume-api)

```python
import flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pymongo
import details

app = flask.Flask(__name__)

limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=['50 per hour', '100 per day'],
        storage_uri="memory://"
        )

# TODO authentication token based

# TODO link to database

# TODO link to redis cache

# TODO updates methods for different actions routes are below

@app.route('/', methods=['GET'])
def home():
    return details.resume

@app.route('/bio', methods=['GET'])
@limiter.limit("15/minute;1/second")
def bio():
    return details.resume['basics']

@app.route('/skills', methods=['GET'])
@limiter.limit('5/minute')
def skills():
    return details.resume['skills']

@app.route('/social', methods=['GET'])
def social():
    return details.resume['profiles']

@app.route('/projects', methods=['GET'])
def projects():
    return details.resume['projects']

@app.route('/work', methods=['GET'])
def work_exp():
    return details.resume['work']

@app.route('/awards', methods=['GET'])
def awards():
    return details.resume['awards']

@app.route('/certs', methods=['GET'])
def certs():
    return details.resume['certificates']

if __name__ == '__main__':
    app.run(
            host='127.0.0.1',
            port=43210,
            debug=True
            )

```

## Next Steps

- Move backend completely to MongoDB and make user data script for EC2 + AMI snapshot

## Social Proof

- Will post on **Discord** channels - 100daysofCloud & LearntoCloud
