# Ramani Talks Orders Api

## About
This is an API to demo REST, HTTP

## Features
- Get all orders 
- Login a user

## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
## Requirements
Python 3.x.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone 
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, the run the app
   ```sh
    $ cd orders-api
    $ virtualenv venv
    $ source venv/bib/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | api/orders | True | Get all Orders
POST | api/login | True | Login a user



## Authors
[Bamuleseyo Gideon](https://github.com/lytes20)
