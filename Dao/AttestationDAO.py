from DAO import Dao
from config import config
from mesModeles import Attestation
from Connexion import DatabaseConnexion


class AttestationDAO(Dao[Attestation]):
    __db = None

    def findAll(self, query, params, attestations=None):
        myConnect = DatabaseConnexion.DatabaseConnexion()
        dbConnexion = myConnect.getConnection()
        curseur = myConnect.getCursor()
        curseur.execute(query, params)
        i = 0
        for attestation in curseur.fetchall():
            attestations[i] = Attestation(attestation)
            i = i + 1

        myConnect.CloseConnexion()

        return attestations
