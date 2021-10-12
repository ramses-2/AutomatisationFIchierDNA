



class Client:
    def __init__(self,code_Client='',nom='',prenom='',profession='',date_Naissance='',ville='',rue='',code_Postal='',telephone='',email='',num_Permis='',categorie_Permis='',date_De_Delivrance='',date_Expiration='',delivre_Par=''):
        self._code_Client = code_Client
        self._nom = nom
        self._prenom = prenom
        self._profession = profession
        self._date_Naissance = date_Naissance
        self._ville = ville
        self._rue = rue
        self._code_Postal = code_Postal
        self._telephone = telephone
        self._email = email
        self._num_Permis = num_Permis
        self._categorie_Permis = categorie_Permis
        self._date_De_Delivrance = date_De_Delivrance
        self._date_Expiration = date_Expiration
        self._delivre_Par = delivre_Par

    @property
    def numAttestation(self) -> str:
        return self._numAttestation

    @numAttestation.setter
    def numAttestation(self, numAttestation) -> None:
        self._numAttestation = numAttestation

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom) -> None:
        self._nom = nom

    @property
    def prenom(self) -> str:
        return self._prenom

    @prenom.setter
    def prenom(self, prenom) -> None:
        self._prenom = prenom

    @property
    def profession(self) -> str:
        return self._profession

    @profession.setter
    def profession(self, profession) -> None:
        self._profession = profession

    @property
    def date_Naissance(self) -> str:
        return self._date_Naissance

    @date_Naissance.setter
    def date_Naissance(self, date_Naissance) -> None:
        self._date_Naissance = date_Naissance

    @property
    def ville(self) -> str:
        return self._ville

    @ville.setter
    def ville(self, ville) -> None:
        self._ville = ville

    @property
    def rue(self) -> str:
        return self._rue

    @rue.setter
    def rue(self, rue) -> None:
        self._rue = rue

    @property
    def code_Postal(self) -> str:
        return self._code_Postal

    @code_Postal.setter
    def code_Postal(self, code_Postal) -> None:
        self._code_Postal = code_Postal

    @property
    def telephone(self) -> str:
        return self._telephone

    @telephone.setter
    def telephone(self, telephone) -> None:
        self._telephone = telephone

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        self._email = email

    @property
    def num_Permis(self) -> str:
        return self._num_Permis

    @num_Permis.setter
    def num_Permis(self, num_Permis) -> None:
        self._num_Permis = num_Permis

    @property
    def categorie_Permis(self) -> str:
        return self._categorie_Permis

    @categorie_Permis.setter
    def categorie_Permis(self, categorie_Permis) -> None:
        self._categorie_Permis = categorie_Permis

    @property
    def date_De_Delivrance(self) -> str:
        return self._date_De_Delivrance

    @date_De_Delivrance.setter
    def date_De_Delivrance(self, date_De_Delivrance) -> None:
        self._date_De_Delivrance = date_De_Delivrance

    @property
    def date_Expiration(self) -> str:
        return self._date_Expiration

    @date_Expiration.setter
    def date_Expiration(self, date_Expiration) -> None:
        self._date_Expiration = date_Expiration

    @property
    def delivre_Par(self) -> str:
        return self._delivre_Par

    @delivre_Par.setter
    def delivre_Par(self, delivre_Par) -> None:
        self._delivre_Par = delivre_Par