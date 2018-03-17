#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import bottle
import os
from bottle import get, run, route, template, static_file, request, response
from os import environ

application = bottle.app()

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

@application.route('/', method=['GET'])
def home():
    return template('./public/ThanhDuyen.html')

if __name__ == "__main__":
 application.run(host='0.0.0.0', port=int(environ.get('PORT', 8000)))