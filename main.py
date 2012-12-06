#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

import os
import datetime as dt
from bottle import route, run, template, static_file


# -- routes
@route('/')
def index():
    '''
    Main page view
    '''
    return template('index', {'title': 'Miejski Kuklok', 'data': get_data()})


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='./static/')


def get_data():
    '''
    Get all the sample data stored in YAML files
    '''
    import yaml

    cur_path  = os.path.dirname(__file__)
    data_file = os.path.join(cur_path, 'data', 'sample_data.yaml')

    data = yaml.load(open(data_file, 'rb').read())
    current_week = dt.datetime.now().date().isocalendar()[1]
    data = [e for e in data if e['week'] > current_week - 3]

    categorized = {}
    for entity in data:
        for cat in entity['categories']:
            tmpl = {
                u'category': cat,
                u'media'   : 0,
                u'city'    : 0
            }

            categorized.setdefault(cat, tmpl)
            categorized[cat][entity['type']] += 1

    data = categorized.values()

    return data


# -- run the app
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
