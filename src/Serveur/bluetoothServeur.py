import bluetooth
import Serveur
import sys


class Bluetooth:
    # lancement fichier python pour commencer la connexion bluetooth du client
    def StartBluetoothServeur(self):
        Serveur.connexionAuClient()

    def __init__ (self):
        cmd = sys.argv[1]
        if (cmd == 'serveur'):
            self.StartBluetoothServeur()
        else :
            print ("Bluetooth")
