from os import path
import json
import unittest
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from app import create_app
from config import app_config, app_active


class TestHomeView(unittest.TestCase):

    '''
      Como todos os 3 casos de teste fazem um get na home "/"
      da nossa aplicacao, definimos a funcao setUp. Ela e executada
      automaticamente sempre que o Pytest instancia a classe TestHomeView.
      A funcao setUp e semelhante a um metodo construtor.
    '''

    def setUp(self):
        config = app_config[app_active]
        config.APP = create_app()
        self.app = config.APP.test_client()

    # Teste de listagem de todos os planetas
    def test_get_planets(self):
        response = self.app.get('/api/planets/')

        # Verificando status 200
        self.assertEqual(200, response.status_code)

        # Verificando formato do retorno
        self.assertIn('application/json', response.content_type)

        # Verificando estrutura do json e os tipos de dados
        result = json.loads(response.data)
        for r in result:
            self.assertIn('climate', r)
            self.assertIn('films', r)
            self.assertIn('id', r)
            self.assertIn('name', r)
            self.assertIn('terrain', r)
            
            self.assertIsInstance(r['climate'], str)
            self.assertIsInstance(r['films'], int)
            self.assertIsInstance(r['id'], str)
            self.assertIsInstance(r['name'], str)
            self.assertIsInstance(r['terrain'], str)

    # Teste de listagem de planeta por id
    def test_get_planet_id(self):
        response = self.app.get('/api/planets/5d2b737cac633646254c68fb/')

        # Verificando status 200
        self.assertEqual(200, response.status_code)

        # Verificando formato do retorno
        self.assertIn('application/json', response.content_type)

        # Verificando estrutura do json e os tipos de dados
        result = json.loads(response.data)
        for r in result:
            self.assertIn('climate', r)
            self.assertIn('films', r)
            self.assertIn('id', r)
            self.assertIn('name', r)
            self.assertIn('terrain', r)
            
            self.assertIsInstance(r['climate'], str)
            self.assertIsInstance(r['films'], int)
            self.assertIsInstance(r['id'], str)
            self.assertIsInstance(r['name'], str)
            self.assertIsInstance(r['terrain'], str)

    # Teste de listagem de planeta por nome
    def test_get_planet_name(self):
        response = self.app.get('/api/planets/Teste 1/')

        # Verificando status 200
        self.assertEqual(200, response.status_code)

        # Verificando formato do retorno
        self.assertIn('application/json', response.content_type)

        # Verificando estrutura do json e os tipos de dados
        result = json.loads(response.data)
        for r in result:
            self.assertIn('climate', r)
            self.assertIn('films', r)
            self.assertIn('id', r)
            self.assertIn('name', r)
            self.assertIn('terrain', r)
            
            self.assertIsInstance(r['climate'], str)
            self.assertIsInstance(r['films'], int)
            self.assertIsInstance(r['id'], str)
            self.assertIsInstance(r['name'], str)
            self.assertIsInstance(r['terrain'], str)
    
    # Teste de criação de planeta
    def test_create_planet(self):
        response = self.app.post(
            '/api/planets/',
            data=json.dumps({
                "name":"Plutão", "climate":"temperate", "terrain":"grassy hills, swamp", "films":4
            }),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'"Planeta criado com sucesso!"', response.data)

    # Teste de edição de planeta
    def test_edit_planet(self):
        response = self.app.put(
            '/api/planets/5d3a483bf4e1f1645bddd2a9/',
            data=json.dumps({
                "climate":"tropical, temperate"
            }),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'"Planeta editado com sucesso!"', response.data)

    # Teste de remoção de planeta
    def test_delete_planet(self):
        response = self.app.delete(
            '/api/planets/5d3a483bf4e1f1645bddd2a9/',
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'"Planeta deletado com sucesso!"', response.data)
         