# Classe de connexion à la base de données.
from datetime import datetime

import psycopg2
from config import config


class DatabaseConnexion:
    __connection = None
    __cursor = None

    def __init__(self):
        __db_config = config.config['postgresql']
        self.__connection = psycopg2.connect(
            user=__db_config['user'],
            password=__db_config['password'],
            host=__db_config['host'],
            port=__db_config['port'],
            database=__db_config['database']
        )
        self.__cursor = self.__connection.cursor()

    def CloseConnexion(self):
        #self.__cursor.quit()
        self.__connection.close()

    def getConnection(self):
        return self.__connection

    def getCursor(self):
        return self.__cursor
