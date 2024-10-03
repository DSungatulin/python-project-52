## Hexlet tests and Codeclimate badges:
[![Actions Status](https://github.com/DSungatulin/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DSungatulin/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3a02112663653215e48f/maintainability)](https://codeclimate.com/github/DSungatulin/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3a02112663653215e48f/test_coverage)](https://codeclimate.com/github/DSungatulin/python-project-52/test_coverage)

# About Service
Task Manager is a flexible web application for creating and tracking tasks. 
The service requires user registration and authorization. The functionality allows you to create and view tasks yourself, assign an executor from existing users, add various statuses /labels for tasks.

[![Live domen](https://python-project-52-mhbm.onrender.com)]
![](docs/images/home_page.jpg)

## Dependencies
- _python = "^3.10"_
- _poetry = "^version 1.6.1"_

## Instructions for the deployment
Environment variables for application deployment:
- SECRET_KEY(django application key)
- DATABASE_URL(postgresql url)
- DEBUG(For deploy = Flase, for dev = True)
- ROLLBAR_ACCESS_TOKEN(Roll bar token for real-time error tracking on the service rollbar.com)
- Documentation for deployment on the service render.com: https://docs.render.com/deploy-django

## Install & Start
```bash
git clone git@github.com:DSungatulin/python-project-52.git
cd python-project-52/
# install poetry
make install
# start server locally
make dev
```