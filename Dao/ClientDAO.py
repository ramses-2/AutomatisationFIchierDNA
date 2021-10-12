from .DAO import Dao
from config import config
from mesModeles import Client
from Connexion import DatabaseConnexion


class AttestationDAO(Dao[Client]):
    __db = None

    def __init__(self):
        self.__db = DatabaseConnexion()

    def findAll(self, query, params):
        return self.__db.query(query, params).fetchall()
