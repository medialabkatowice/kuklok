# coding: utf-8
'''
Sample data generation script
'''

import codecs
import datetime as dt
import random
import sys
import yaml


def get_few(elements):
    '''
    Chooses a random number of random elements from list elemts
    '''
    random.shuffle(elements)
    stop = random.randint(0, len(elements) / 2)

    return elements[:stop]


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
    how_many = int(sys.argv[1])
except IndexError:
    print u'python generate_sample_data.py <how_many>'
    exit(-1)

data = []
for i in range(how_many):
    source = random.choice(sources)
    date   = random_date()

    tmp = {
        u'id'           : i,
        u'title'        : u'Tytuł %s' % i,
        u'text'         : u'Lorem ipsum bla bla bla',
        u'source'       : source['name'],
        u'url'          : source['url'] % u'lorem',
        u'tags'         : get_few(tags),
        u'date'         : date,
        u'week'         : date.isocalendar()[1],
        u'author'       : random.choice(authors),
        u'districts'    : get_few(districts),
        u'type'         : source['type'],
        u'content_type' : random.choice(types[source['type']]),
        u'popularity'   : random.random(),
        u'categories'   : get_few(categories)
    }

    data.append(tmp)

output_file = codecs.open(u'sample_data.yaml', u'wb', u'utf-8')
output_file.write(yaml.dump(data))
output_file.close()
