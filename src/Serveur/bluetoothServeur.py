import bluetooth
import Serveur
import connexionNodeJS
import sys


class Bluetooth(object):
    # lancement fichier python pour commencer la connexion bluetooth du client
    def StartBluetoothServeur():
        Serveur.connexionAuClient()

    def __init__ == 'main':
        cmd = sys.argv[1]
        if (cmd == 'serveur'):
            StartBluetoothClient()
        else :
            print ("Bluetooth")
