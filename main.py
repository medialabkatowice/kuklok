#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

import os
import datetime as dt
import simplejson as js
from bottle import request, redirect, route, run, template, static_file

HOW_OLD = 6


# -- routes
@route('/')
def index():
    '''
    Main page view
    '''
    return template('index', {'title': 'Miejski kuklok'})


@route('/all_stats')
def all_stats():
    '''
    Returns stats for all categories
    '''

    return js.dumps({'data': stats_for()})


@route('/selected_stats')
def selected_stats():
    '''
    Returns stats for selected categories
    '''
    categories = request.GET.get('categories', '').split(',')

    return js.dumps({'data': stats_for(categories)})


@route('/featured_stats')
def featured_stats():
    '''
    Returns only selected categories
    '''
    cur = db_cursor()

    # get recent stats for the most active category
    cur.execute('''SELECT category FROM weeks
                    WHERE week = %d
                    ORDER BY abs(media + city) DESC
                    LIMIT 1
                ''' % current_week())
    most_active = cur.fetchone()[0]

    # get recent stats for the most differing category
    cur.execute('''SELECT category FROM weeks
                    WHERE week = %d
                    ORDER BY abs(media - city) DESC
                    LIMIT 1
                ''' % current_week())
    most_differ = cur.fetchone()[0]

    # two separate calls to keep the order: active, differ
    data = stats_for([most_active]) + stats_for([most_differ])

    return js.dumps({'data': data})


@route('/<category:re:[A-Z].*>')
def single_category(category=None):
    '''
    Show page for selected category
    '''
    return template('category', {'title': 'Miejski kuklok :: %s' % category})


@route('/timeline/<category>')
def timeline(category=None):
    '''
    Get all the data from a certain category
    '''
    data = stats_for([category], latest=False)
    if not data:
        redirect('/')

    return js.dumps({'data': data})


@route('/details/<category>/<week_delta>')
def details(category, week_delta):
    '''
    Gets the details for a certain week
    '''
    week = current_week() - int(week_delta)
    query = '''SELECT date, title, author, source, url
                FROM articles
                WHERE categories LIKE '%%%s%%'
                    AND week = %d
                    AND type = '%s'
            '''

    cur = db_cursor()
    cur.execute(query % (category, week, 'media'))
    media = cur.fetchall()

    cur.execute(query % (category, week, 'city'))
    city = cur.fetchall()

    return {'media': media, 'city': city}


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='./static/')


def stats_for(cats=None, latest=True):
    '''
    Grabs stats from db for selected categories
    '''
    assert cats or latest

    categories = '(%s)' % ' OR '.join(["category='%s'" % e for e in cats])\
                 if cats else ''
    history    = 'week > %d' % (current_week() - HOW_OLD)\
                 if latest else ''
    where      = ' AND '.join([e for e in [categories, history] if e])

    query = '''SELECT category, media, city
                FROM weeks
                WHERE %s
                ORDER BY category, week DESC
            ''' % where

    cur = db_cursor()
    cur.execute(query)
    raw_data = cur.fetchall()

    aggregated = {}
    for entry in raw_data:
        category = entry[0]
        counts   = {
            'media': entry[1],
            'city' : entry[2]
        }

        tmpl = {
            'category': category,
            'weeks'   : []
        }
        aggregated.setdefault(category, tmpl)
        aggregated[category]['weeks'].append(counts)

    data = sorted(aggregated.values(), key=lambda e: e['category'])

    return data


def db_cursor():
    '''
    Connects to db and return connection with cursor
    '''
    import sqlite3

    cur_path = os.path.dirname(__file__)
    db_file  = os.path.join(cur_path, 'data', 'sample_data.db')

    con = sqlite3.connect(db_file)
    cur = con.cursor()

    return cur


def current_week():
    '''
    Returns a current week from isocalendar
    '''
    isocal = dt.datetime.now().isocalendar()
    return isocal[1]


# -- run the app
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
