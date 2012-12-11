# coding: utf-8
'''
Sample data generation script
'''

import codecs
import collections
import datetime as dt
import random
import sys
import yaml

import sqlite3
con = sqlite3.connect('sample_data.db')
cur = con.cursor()

def get_few(elements):
    '''
    Chooses a random number of random elements from list elemts
    '''
    random.shuffle(elements)
    stop = random.randint(1, len(elements) / 2)

    return ','.join(elements[:stop])


def random_date():
    '''
    Gets the random date from 1st of November 2012 till today
    '''
    start = dt.date(2012, 11, 1)
    end   = dt.datetime.now().date()

    secs = random.randint(0, int((end - start).total_seconds()))

    return start + dt.timedelta(seconds=secs)


sources = [
    {
        u'name': u'Gazeta Wyborcza',
        u'url' : u'http://gazeta.pl/%s',
        u'type': u'media'
    },
    {
        u'name': u'Dziennik Zachodzni',
        u'url' : u'http://dziennikzachodni.pl/%s',
        u'type': u'media'
    },
    {
        u'name': u'Szopienice INFO',
        u'url' : u'http://szopienice.info/%s',
        u'type': u'media'
    },
    {
        u'name': u'Biuletyn Informacji Publicznej UM',
        u'url' : u'http://bip.katowice.pl/%s',
        u'type': u'city'
    },
    {
        u'name': u'Portal Radnych',
        u'url' : u'http://katowice.eu/portalradnych/%s',
        u'type': u'city'
    }
]

tags = [u'Kraj', u'Opinie', u'Sondaże', u'Świat',
        u'Sport', u'Szkoła ', u'Praca', u'Polka']

authors = [u'Jan Kowalski', u'Anna Nowak', u'Franek Kimono',
           u'Kazek Nalazek', u'Jola Albert']

districts = [u'Bogucice', u'Brynów ', u'Dąb', u'Dąbrówka Mała',
             u'Giszowiec', u'Janów-Nikiszowiec', u'Kostuchna',
             u'Koszutka', u'Ligota-Panewniki', u'Murcki',
             u'os. Paderewskiego-Muchowiec', u'os. Tysiąclecia',
             u'os. Witosa', u'Piotrowice-Ochojec', u'Podlesie',
             u'Środmieście', u'Szopienice-Burowiec',
             u'Wełnowiec-Józefowiec', u'Załęska Hałda-Brynów',
             u'Załęże', u'Zarzecze', u'Zawodzie']

categories = [u'Edukacja', u'Infrastruktura', u'Zdrowie',
              u'Ekonomia', u'Transport', u'Kultura']

types = {
    u'media': [u'news', u'artykuł', u'wywiad'],
    u'city' : [u'news', u'interpelacja', u'uchwała']
}

try:
    HOW_MANY = int(sys.argv[1])
except IndexError:
    print u'python generate_sample_data.py <how_many>'
    exit(-1)

for i in range(HOW_MANY):
    source = random.choice(sources)
    date   = random_date()

    entity = (
        u'Tytuł %s' % i,                      # title        
        source['name'],                       # source      
        source['url'] % u'lorem',             # url         
        get_few(tags),                        # tags        
        date,                                 # date        
        date.isocalendar()[1],                # week        
        random.choice(authors),               # author      
        get_few(districts),                   # districts   
        source['type'],                       # type        
        random.choice(types[source['type']]), # content_type
        random.random(),                      # popularity  
        get_few(categories)                   # categories  
                                                                     
    )
                                     
    cur.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', entity)

con.commit()
con.close()

