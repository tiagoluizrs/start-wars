# -*- coding: utf-8 -*-
import sys
from app import create_app
from config import app_config, app_active

config = app_config[app_active]
config.APP = create_app()
app = config.APP

if __name__ == '__main__':
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys)