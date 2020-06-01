#!/usr/bin/env python

import json
from os import getenv
from bottle import route, run, response

APP_HOST = getenv('APP_HOST', '0.0.0.0')
APP_PORT = getenv('APP_PORT', '8000')


@route('/hello')
@route('/hello/<name>')
def index(name='guest'):
    response.content_type = 'application/json'

    return json.dumps({
        'name': name,
        'greeting': f'Hello {name}!'
    })


if __name__ == '__main__':
    run(host=APP_HOST, port=APP_PORT)