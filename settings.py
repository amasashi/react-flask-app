import configparser
import os

conf = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), 'settings.ini')
conf.read(path, 'UTF-8')

secret_key = conf['app_key']['secret_key']
