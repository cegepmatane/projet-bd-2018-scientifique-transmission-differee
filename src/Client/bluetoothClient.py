import bluetooth
import Client
import Serveur
import connexionNodeJS
import sys


class Bluetooth(object):
    # lancement fichier python pour commencer la connexion bluetooth du client
    def StartBluetoothClient():
        Client.connexionAuServeur()

    def EnvoieDonneeAuServeur():
        connexionNodeJS.on_send();

    def __init__ == 'main':
        cmd = sys.argv[1]
        if (cmd == 'client'):
            StartBluetoothClient()
        elif (cmd == 'serveur'):
            EnvoieDonneeAuServeur()
        else :
            print ("Bluetooth")
