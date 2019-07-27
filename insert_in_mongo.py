from pymongo import MongoClient
import requests
from pprint import pprint

cliente = MongoClient(host='127.0.0.1',
                     port=27017, 
                     username='usuario', 
                     password='senha',
                    authSource="admin")

banco = cliente.starWars
album = banco.planet

log = ''

for i in range(1, 8):
    url = 'https://swapi.co/api/planets/?page=%s' % i
    r = requests.get(url)
    results = r.json()['results']
    for r in results:
        name = None
        climate = None
        terrain = None
        movies = None

        if 'name' in r:
            name = r['name']

        if 'climate' in r:
            climate = r['climate']

        if 'terrain' in r:
            terrain = r['terrain']

        if 'films' in r:
            films = len(r['films'])

        try:
            album.insert_one({
                'name': name,
                'climate': climate,
                'terrain': terrain,
                'films': films
            })
        except Exception as e:
            print('Um erro ocorreu no planeta %s %s' % (name, e))
            log += 'Um erro ocorreu no planeta %s %s \n' % (name, e)

file = open("log.txt", "w+")
file.write(log)
file.close()