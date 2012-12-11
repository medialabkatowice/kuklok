#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

import os
import datetime as dt
from bottle import route, run, template, static_file

HOW_OLD = 3


# -- routes
@route('/')
def index():
    '''
    Main page view
    '''
    cur = connect_to_db()

    # get recent stats for the most active category
    cur.execute('''SELECT category FROM weeks
                    WHERE week = %d
                    ORDER BY abs(media + city) DESC
                    LIMIT 1
                ''' % current_week())
    most_active = cur.fetchone()[0]

    cur.execute('''SELECT * FROM weeks
                    WHERE week > %d AND category = '%s'
                    ORDER BY week DESC
                ''' % (current_week() - HOW_OLD, most_active))
    recent_active = cur.fetchall()

    # get recent stats for the most differing category
    cur.execute('''SELECT category FROM weeks
                    WHERE week = %d
                    ORDER BY abs(media - city) DESC
                    LIMIT 1
                ''' % current_week())
    most_differ = cur.fetchone()[0]

    cur.execute('''SELECT * FROM weeks
                    WHERE week > %d AND category = '%s'
                    ORDER BY week DESC
                ''' % (current_week() - HOW_OLD, most_differ))
    recent_differ = cur.fetchall()

    return template('index', {'title': 'Miejski Kuklok',
                              'active': recent_active,
                              'differ': recent_differ})


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='./static/')


def connect_to_db():
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
