# -*- coding: utf-8 -*-
from datetime import datetime

from model.Planet import PlanetModel

class Planet(object):
    def __init__(self):
        self.planet = PlanetModel()

    def find_(self, value):
        result = []
        status = 200
        try:
            if value is not None:
                res = self.planet.find_by_field_('name', value)
                for r in res:
                    result.append({
                        'id': str(r['_id']),
                        'name': r['name'],
                        'climate': r['climate'],
                        'terrain': r['terrain'],
                        'films': r['films']
                    })
                
                if not len(result):
                    res = self.planet.find_by_field_('_id', value, obj=True)
                    for r in res:
                        result.append({
                            'id': str(r['_id']),
                            'name': r['name'],
                            'climate': r['climate'],
                            'terrain': r['terrain'],
                            'films': r['films']
                        })
            else:
                res = self.planet.find_all_()
                for r in res:
                    result.append({
                        'id': str(r['_id']),
                        'name': r['name'],
                        'climate': r['climate'],
                        'terrain': r['terrain'],
                        'films': r['films']
                    })
                
        except Exception as e:
            result = []
            status = 500
        finally:
            return {
                'status': status,
                'result': result
            }

    def insert_(self, obj_json):
        films = 0

        if 'films' in obj_json:
            films = obj_json['films']

        data = {
            'name': obj_json['name'],
            'climate': obj_json['climate'],
            'terrain': obj_json['terrain'],
            'films': films
        }   

        status = 200
        try:
            self.planet.insert_(data)
            result = 'Planeta criado com sucesso!'
        except Exception as e:
            status = 500
            result = 'Erro ao criar planeta.'
        finally:
            return {
                'result': result,
                'status': status
            }

    def update_(self, _id, obj_json):
        status = 200
        try:
            self.planet.update_(_id, obj_json)
            result = 'Planeta editado com sucesso!'
        except Exception as e:
            status = 500
            result = 'Erro ao editar planeta.'
        finally:
            return {
                'result': result,
                'status': status
            }

    def delete_(self, _id):
        status = 200
        try:
            self.planet.delete_(_id)
            result = 'Planeta deletado com sucesso!'
        except Exception as e:
            status = 500
            result = 'Erro ao deletar planeta.'
        finally:
            return {
                'result': result,
                'status': status
            }