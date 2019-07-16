# -*- coding: utf-8 -*-
import ipdb
# config import
from config import app_config, app_active
from bson.objectid import ObjectId

config = app_config[app_active]

class PlanetModel(object):
    def __init__(self):
        self.planets = config.MONGO.planet

    def insert_(self, data):
        try:
            self.planets.insert_one(data)
        except Exception as e:
            print('[[insert_]] >> Um erro ocorreu ao tentar criar um planeta. Descrição: %s' % e)
            raise Exception

    def update_(self, _id, data):
        try:
            self.planets.update_one({"_id":ObjectId(_id)}, { "$set": data })
        except Exception as e:
            print('[[update_]] >> Um erro ocorreu ao tentar criar um planeta. Descrição: %s' % e)
            raise Exception

    def find_all_(self):
        try:
            res = self.planets.find()
        except Exception as e:
            print('[[find_all]] >> Um erro ocorreu ao tentar listar todos os planetas. Descrição: %s' % e)
            res = []
        finally:
            return res

    def find_by_field_(self, field, value, obj=False):
        try:
            if obj:
                res = self.planets.find({field: ObjectId(value)})
            else:
                res = self.planets.find({field: value})
        except Exception as e:
            print('[[find_by_field_]] >> Um erro ocorreu ao tentar listar um planeta. Descrição: %s' % e)
            res = []
        finally:
            return res

    def delete_(self, _id):
        try:
            self.planets.delete_one({'_id': ObjectId(_id)})
        except Exception as e:
            print('[[delete_]] >> Um erro ocorreu ao tentar deletar um planeta. Descrição: %s' % e)
            raise Exception
