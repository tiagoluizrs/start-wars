# Projeto star wars

## Requisitos
- Python 3.x
- Python-pip atualizado
- Banco de dados Mongodb

## Instalando os itens necessários para o Python


1. Instale o python em seu ubuntu
```console
sudo apt-get install python3
```

2. Agora instale o pip em seu Ubuntu
```console
sudo apt install python3-pip
```

3. Instale o Virtualenv para podermos criar um ambiente virtual para o projeto
```console
sudo pip install virtualenv
```

4. Agora Crie o virtualenv do projeto
```console
virtualenv -p python3 venv
```

5. Ative o virtualenv para poder instalar as bibliotecas nele.
```console
source venv/bin/activate
```

6. Instale as bibliotecas registradas no requirements.txt
```console
pip install -r requirements.txt
```

## Instalando o mongodb

1. Atualize a lista de pacotes do seu ubuntu
```console
sudo apt update
```

2. Agora instale o mongodb 
```console
sudo apt install -y mongodb
```

3. Para verificar o status do mongodb rode:
```console
sudo systemctl status mongodb
```

4. Para iniciar o mongodb rode:
```console
sudo systemctl start mongodb
```

5. Para parar o mongodb rode:
```console
sudo systemctl stop mongodb
```

5. Para reiniciar o mongodb rode:
```console
sudo systemctl restart mongodb
```

## Importando os planetas para o mongodb

Após ter instalado o mongodb você deverá criar um database chamado starWars contendo uma collection chamada `planet`.

Após fazer isso, rode o arquivo `insert_in_mongo.py`. Não esqueça de alterar os dados de autenticação no arquivo para o usuário e senha do seu mongodb.

Rodando isso, você importará todos os planetas que existem na api `https://swapi.co/`

Se preferir pegue o arquivo backup no repositório chamado `starWars_mongo_bkp.tar.gz` e suba-o para seu banco de dados usando o comando `mongorestore`. Para saber mais visite a documentação do [mongodb](https://docs.mongodb.com/manual/reference/program/mongorestore/). 

## Rodando o projeto

1. Pegue o arquivo `config-basic.py` e duplique-o criando o arquivo `config.py`, isso foi feito para que se preservem dados de banco de dados, senhas e outros itens pessoais da máquina de cada desenvolvedor do projeto.

2. Agora que o projeto possui um arquivo `config.py` crie uma SECRET com pelo menos 64bits e altere os dados de banco do mongodb que estão no arquivo. Para cada ambiente as credenciais poderão ser diferentes. Os ambientes são production, testing e development.

3. Ative a variável de ambiente seguindo o exemplo abaixo:
```console
export FLASK_ENV=development
```

4. No arquivo app.py selecione se usará o modelo de conexão ao mongo com usuário e senha ou sem usuário e senha:

```python
# Se seu banco possuir usuário e senha use este modelo
db = MongoClient(
    host=config.MONGO_HOST,
    port=config.MONGO_PORT, 
    username=config.MONGO_USERNAME, 
    password=config.MONGO_PASSWORD,
    authSource=config.MONGO_USERNAME,
    maxPoolSize=4
)

# Se não houver usuário e senha use este
# db = MongoClient(
#     host=config.MONGO_HOST,
#     port=config.MONGO_PORT, 
#     maxPoolSize=4
# )
```

> Você também pode usar `testing` ou `production` dependendo da finalidade em que o projeto rodará.

5. Agora rode o comando à seguir para que a API funcione corretamente:
```console
python wsgi.py
```

Pronto, sua API está funcionando:
```console
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://localhost:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 142-380-668
```

## Realizando testes Unitários

1. Para realizar testes unitários basta rodar o comando à seguir:
```console
py.test --cov=app
```

> Na pasta tests existe um arquivo chamado `test_planet.py`, caso deseje criar outros testes, basta criar um arquivo nesta pasta com o prefixo test_ e um nome para completar o arquivo e a extensão .py, por exemplo `test_persist.py`. A opção --cov=app irá exibir a porcentagem de código de nossa API que está coberto pelos testes unitários que foram criados.

Algo assim será visto no terminal:
```console
----------- coverage: platform linux, python 3.7.3-final-0 -----------
Name     Stmts   Miss  Cover
----------------------------
app.py      43      2    95%
```