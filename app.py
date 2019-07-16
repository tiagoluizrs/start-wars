# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, render_template, Response, json, abort
from pymongo import MongoClient
from functools import wraps
# config import
from config import app_config, app_active

# Controllers
from controller.Planet import Planet

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__)
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db = MongoClient(
        host=config.MONGO_HOST,
        port=config.MONGO_PORT, 
        username=config.MONGO_USERNAME, 
        password=config.MONGO_PASSWORD,
        authSource=config.MONGO_USERNAME,
        maxPoolSize=4
    )
    config.MONGO = db.starWars

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/api/planets/', methods=['GET'])
    @app.route('/api/planets/<string:value>/', methods=['GET'])
    def find_planets(value=None):
        planet = Planet()
        response = planet.find_(value)

        return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

    @app.route('/api/planets/', methods=['POST'])
    def insert_planet():
        planet = Planet()
        response = {
            'status': 200,
            'result': ''
        }

        if request.json['name'] is None or request.json['climate'] is None or request.json['terrain'] is None:
            response['result'] = 'Você precisa enviar seu objeto com os campos nome, climate e terrain'
        else:
            response = planet.insert_(request.json)

        return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

    @app.route('/api/planets/<string:_id>/', methods=['PUT'])
    def update_planet(_id):
        planet = Planet()
        response = {
            'status': 200,
            'result': ''
        }

        if request.json['name'] is None or request.json['climate'] is None or request.json['terrain'] is None:
            response['result'] = 'Você precisa enviar seu objeto com os campos nome, climate e terrain'
        else:
            response = planet.update_(_id, request.json)

        return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

    @app.route('/api/planets/<string:_id>/', methods=['DELETE'])
    def delete_planet(_id):
        planet = Planet()
        response = planet.delete_(_id)

        return Response(json.dumps(response['result'], ensure_ascii=False), mimetype='application/json'), response['status']

    return app