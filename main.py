
import tools
import datetime
import psycopg2

# Press the green button in the gutter to run the script.
from Connexion.DatabaseConnexion import DatabaseConnexion
#from Dao.AttestationDAO import AttestationDAO
#from mesModeles.Attestation import Attestation
#from tools.Fichier import Fichier
import Connexion

if __name__ == '__main__':
     print('1) se connecter a la BD')
     myConnection=DatabaseConnexion()
     print('--- connexion reussie----')
     #myAttestationDAO=AttestationDAO()
     #mesAttestations=Attestation()
     #myConnection.ExecutionRequete(mesAttestations.requeteAttestation)
#    print('2) executer les requetes vehicule, attestation et clients')

     
#    print('3) creer les fichiers qui recevront les resultats des differentes requetes')
#    print('4) charger les resultats dans un fichier txt')
     myConnection.CloseConnexion()
     print('5) fermer la connexion a la BD')

#    print('6) se connecter par ftp')
#    print('7) envoyer les fichiers creer par ftp')
#    print('8) fermer la connexion ftp')
     #monFichier=Fichier()

     # monFichier.nommerFichier('client')
     #print('2-'+monFichier.fileName)




