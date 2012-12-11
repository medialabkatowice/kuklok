import collections
import sqlite3

con = sqlite3.connect('sample_data.db')
cur = con.cursor()

cur.execute('SELECT type, week, categories FROM articles')
data = cur.fetchall()

categorized = {}

for entity in data:
    e_type = entity[0]
    e_week = entity[1]

    for cat in entity[2].split(','):
        key  = '%s_%s' % (e_week, cat)
        tmpl = collections.OrderedDict({
            u'week'    : e_week,
            u'category': cat,
            u'media'   : 0,
            u'city'    : 0,
        })

        categorized.setdefault(key, tmpl)
        categorized[key][e_type] += 1


vals = [tuple(e.values()) for e in categorized.values()]


cur.executemany('INSERT INTO weeks VALUES(?,?,?,?)', vals)
con.commit()
con.close()
