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
    recent = [e for e in sample_data() if e['week'] > current_week() - 3]
    categorized = {}
    for entity in recent:
        for cat in entity['categories']:
            tmpl = {
                u'category': cat,
                u'desc'    : u'Lorem ipsum',
                u'cur_week': 0,
                u'media'   : 0,
                u'city'    : 0
            }

            categorized.setdefault(cat, tmpl)
            categorized[cat][entity['type']] += 1

            if entity['week'] == current_week():
                categorized[cat]['cur_week'] += 1

    data = sorted(categorized.values(), key=lambda e: e['category'])

    maxi = sorted(categorized.values(), key=lambda e: e['cur_week']).pop()
    diff = sorted(categorized.values(), key=lambda e: abs(e['media'] - e['city'])).pop()

    return template('index', {'title': 'Miejski Kuklok', 'data': data, 'maxi': maxi, 'diff': diff})


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='./static/')


def sample_data():
    '''
    Get sample data stored in YAML files
    '''
    import yaml

    cur_path  = os.path.dirname(__file__)
    data_file = os.path.join(cur_path, 'data', 'sample_data.yaml')

    data = yaml.load(open(data_file, 'rb').read())

    return data


def current_week():
    '''
    Returns a current week from isocalendar
    '''
    isocal = dt.datetime.now().isocalendar()
    return isocal[1]


# -- run the app
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
