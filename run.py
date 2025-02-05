import sys
from app import create_app
from config import app_config, app_active
import os

config = app_config[app_active]
config.APP = create_app()

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    os.system("flask db upgrade")
