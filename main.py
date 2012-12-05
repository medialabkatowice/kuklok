#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from bottle import install, route, run, template, request, static_file


# -- routes
@route('/')
def index():
    return template('index', {'title': 'Miejski Kuklok', 'data': get_data()})


@route('/static/<path:path>')
def serve_files(path):
    return static_file(path , root='./static/')

def get_data():
    import yaml

    cur_path  = os.path.dirname(__file__)
    data_file = os.path.join(cur_path, 'data', 'sample_data.yaml')

    return yaml.load(open(data_file, 'rb').read())


# -- run the app
if __name__ == '__main__':

    run(host='localhost', port=8080)
