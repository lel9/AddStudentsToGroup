import codecs
import configparser
import traceback

from redminelib import *


def read_config(path):
    try:
        # загружаем настройки
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.readfp(codecs.open(path, "r", "utf8")) # читаем конфиг

        if 'Redmine' not in config:
            raise AttributeError('Redmine config not found')
        if 'redmine_host' not in config['Redmine']:
            raise AttributeError('redmine_host not found')
        if 'redmine_key' not in config['Redmine']:
            raise AttributeError('redmine_key not found')

    except AttributeError as ae:
        print('Config error: ')
        print(ae)
        return 1, None
    except Exception as e:
        traceback.print_exc()
        return 2, None
    return 0, config


def get_redmine(config):
    try:
        return 0, Redmine(config['Redmine']['redmine_host'],
                          key = config['Redmine']['redmine_key'])
    except Exception as e:
        traceback.print_exc()
        return 1, None