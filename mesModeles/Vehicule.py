


class Vehicule:
    def __init__(self,num_Immatriculation='',num_Chassi='',marque='',modele='',premier_Annee_De_Circulation='',categorie='',capacite_De_Charge='',puissance_Fiscale='',nbr_Porte='',remorque='',source_Energie='',numero_Carte_Grise):
        self._num_Immatriculation = num_Immatriculation
        self._num_Chassi = num_Chassi
        self._marque = marque
        self._modele = modele
        self._premier_Annee_De_Circulation = premier_Annee_De_Circulation
        self._categorie = categorie
        self._capacite_De_Charge = capacite_De_Charge
        self._puissance_Fiscale = puissance_Fiscale
        self._nbr_Porte = nbr_Porte
        self._remorque = remorque
        self._source_Energie = source_Energie
        self._numero_Carte_Grise = numero_Carte_Grise

    @property
    def num_Immatriculation(self) -> str:
        return self._num_Immatriculation

    @num_Immatriculation.setter
    def num_Immatriculation(self, num_Immatriculation) -> None:
        self._num_Immatriculation = num_Immatriculation


    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, marque) -> None:
        self._marque = marque

    @property
    def num_Chassi(self) -> str:
        return self._num_Chassi

    @num_Chassi.setter
    def num_Chassi(self, num_Chassi) -> None:
        self._num_Chassi = num_Chassi

    @property
    def modele(self) -> str:
        return self._modele

    @modele.setter
    def modele(self, modele) -> None:
        self._modele = modele

    @property
    def premier_Annee_De_Circulation(self) -> str:
        return self._premier_Annee_De_Circulation

    @premier_Annee_De_Circulation.setter
    def premier_Annee_De_Circulation(self, premier_Annee_De_Circulation) -> None:
        self._premier_Annee_De_Circulation = premier_Annee_De_Circulation

    @property
    def categorie(self) -> str:
        return self._categorie

    @categorie.setter
    def categorie(self, categorie) -> None:
        self._categorie = categorie

    @property
    def capacite_De_Charge(self) -> str:
        return self._capacite_De_Charge

    @capacite_De_Charge.setter
    def capacite_De_Charge(self, capacite_De_Charge) -> None:
        self._capacite_De_Charge = capacite_De_Charge

    @property
    def puissance_Fiscale(self) -> str:
        return self._puissance_Fiscale

    @puissance_Fiscale.setter
    def puissance_Fiscale(self, puissance_Fiscale) -> None:
        self._puissance_Fiscale = puissance_Fiscale

    @property
    def nbr_Porte(self) -> str:
        return self._nbr_Porte

    @nbr_Porte.setter
    def nbr_Porte(self, nbr_Porte) -> None:
        self._nbr_Porte = nbr_Porte

    @property
    def remorque(self) -> str:
        return self._remorque

    @remorque.setter
    def remorque(self, remorque) -> None:
        self._remorque = remorque


    def source_Energie(self) -> str:
        return self._source_Energie

    @source_Energie.setter
    def source_Energie(self, source_Energie) -> None:
        self._source_Energie = source_Energie

    @property
    def numero_Carte_Grise(self) -> str:
        return self._numero_Carte_Grise

    @numero_Carte_Grise.setter
    def numero_Carte_Grise(self, numero_Carte_Grise) -> None:
        self._numero_Carte_Grise = numero_Carte_Grise