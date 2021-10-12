import datetime




class Fichier:

    def __init__(self):
        self.__instanceFichier=None
        self.__fileName=''
        self.__modeOuverture='w'

        # getter method
    def get_instanceFichier(self):
        return self.__instanceFichier

        # setter method
    def set_instanceFichier(self, x):
        self.__instanceFichier = x

            # getter method

    def get_fileName(self):
        return self.__fileName

        # setter method

    def set_fileName(self, x):
        self.__fileName = x


    def get_modeOuverture(self):
        return self.__fileName

        # setter method

    def set_modeOuverture(self, x):
        self.set_fileName(x)


    def ouvrirFichier(self):
        self.set_instanceFichier(open(self.get_fileName(), self.get_modeOuverture()))

    def fermerFichier(self):
        self.get_instanceFichier().close()


    def nommerFichier(self,typeRequete):
        self.set_fileName(typeRequete+datetime.datetime.today().strftime('_%d_%m_%Y_%H_%M_%S')+'.txt')
