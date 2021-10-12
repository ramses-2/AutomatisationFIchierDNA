

class Attestation:
    requeteAttestation = ' select stc.name as numAttestation,so.name as numPolice,date_part(\'year\',(stc.write_date::date)) as date_delivrance,so.date_effet as date_debut,so.fin_garantie as date_Fin,' \
                         'CASE' \
                         '     WHEN tc.id =1 THEN \'Jaune\'   ELSE \'Brune\' ' \
                         'END AS couleur,' \
                         'CASE ' \
                         'WHEN stc.state= \'1\' THEN \'Numéro libre\' ' \
                         'WHEN stc.state = \'2\'::text THEN \'Numéro utilisé\' ' \
                         'ELSE \'Numéro défectueux\' ' \
                         ' END AS status, ' \
                         'CASE ' \
                         'WHEN ea.zone_circ= \'1\' THEN \'Zone I\'' \
                         'WHEN ea.zone_circ = \'2\'::text THEN \'Zone II\'' \
                         'ELSE \'Zone III\'' \
                         ' END AS zone_Circulation,' \
                         'ea.immat as num_Immatriculation,' \
                         'rp.ref as code_Client,' \
                         'Null::text as code Assureur,' \
                         'Null::text as bon_De_Livraison,' \
                         'so.policy_id,ea.policy_id' \
                         'from stock_carte_line stc' \
                         'left join  eltech_eau ea on stc.id=ea.num_carte_id' \
                         'left join sale_order so on so.policy_id=ea.policy_id' \
                         'left join type_carte tc on tc.id=stc.type_carte_id' \
                         'left join res_partner rp on rp.id=ea.partner_id' \
                         'where tc.id<>3 and stc.write_date =?'

    def __init__(self, numAttestation='', numPolice='', date_delivrance='', date_debut='', date_Fin='', couleur='', status='', zone_Circulation='', num_Immatriculation='', code_Client='', code_Assureur='', bon_De_Livraison=''):
        self._numAttestation = numAttestation
        self._numPolice = numPolice
        self._date_delivrance = date_delivrance
        self._date_debut = date_debut
        self._date_Fin = date_Fin
        self._couleur = couleur
        self._status = status
        self._zone_Circulation = zone_Circulation
        self._num_Immatriculation = num_Immatriculation
        self._code_Client = code_Client
        self._code_Assureur = code_Assureur
        self._bon_De_Livraison = bon_De_Livraison

    def __init__(self, valeurChamp):
        self._numAttestation = valeurChamp[0]
        self._numPolice = valeurChamp[1]
        self._date_delivrance = valeurChamp[2]
        self._date_debut = valeurChamp[3]
        self._date_Fin = valeurChamp[4]
        self._couleur = valeurChamp[5]
        self._status = valeurChamp[6]
        self._zone_Circulation = valeurChamp[7]
        self._num_Immatriculation = valeurChamp[8]
        self._code_Client = valeurChamp[9]
        self._code_Assureur = valeurChamp[10]
        self._bon_De_Livraison = valeurChamp[11]


    @property
    def numAttestation(self) -> str:
        return self._numAttestation

    @numAttestation.setter
    def numAttestation(self, numAttestation):
        self._numAttestation = numAttestation

    @property
    def numPolice(self) -> str:
        return self._numPolice

    @numPolice.setter
    def numPolice(self, numPolice) -> None:
        self._numPolice = numPolice

    @property
    def date_delivrance(self) -> str:
        return self._date_delivrance

    @date_delivrance.setter
    def date_delivrance(self, date_delivrance) -> None:
        self._date_delivrance = date_delivrance

    @property
    def date_debut(self) -> str:
        return self._date_debut

    @date_debut.setter
    def date_debut(self, date_debut) -> None:
        self._date_debut = date_debut

    @property
    def couleur(self) -> str:
        return self._couleur

    @couleur.setter
    def couleur(self, couleur) -> None:
        self._couleur = couleur

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status) -> None:
        self._status = status

    @property
    def zone_Circulation(self) -> str:
        return self._zone_Circulation

    @zone_Circulation.setter
    def zone_Circulation(self, zone_Circulation) -> None:
        self._zone_Circulation = zone_Circulation

    @property
    def num_Immatriculation(self) -> str:
        return self._num_Immatriculation

    @num_Immatriculation.setter
    def num_Immatriculation(self, num_Immatriculation) -> None:
        self._num_Immatriculation = num_Immatriculation

    @property
    def code_Client(self) -> str:
        return self._code_Client

    @code_Client.setter
    def code_Client(self, code_Client) -> None:
        self._code_Client = code_Client

    @property
    def code_Assureur(self) -> str:
        return self._code_Assureur

    @code_Assureur.setter
    def code_Assureur(self, code_Assureur) -> None:
        self._code_Assureur = code_Assureur

    @property
    def bon_De_Livraison(self) -> str:
        return self._bon_De_Livraison

    @bon_De_Livraison.setter
    def bon_De_Livraison(self, bon_De_Livraison) -> None:
        self._bon_De_Livraison = bon_De_Livraison