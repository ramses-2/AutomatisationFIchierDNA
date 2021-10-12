#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe de connexion par ftp
from ftplib import FTP
from config import config

class FTPConnexion:
    __connection = None


    def __init__(self):
        __ftp_config=config.config['myftp']
        self.__connection=FTP(__ftp_config['host'],
                              __ftp_config['user'],
                              __ftp_config['password'])

    def closeConnexion(self):
        self.__connection.quit()

    def sendFileToFTP(self, fileName):
        f = open(fileName, 'rb')
        self.__connection.storbinary('STOR ' + fileName, f)
        f.close()

