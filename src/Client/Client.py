from bluetooth import *
import donneeDAO


adresseServeur = ["",""]  # enregistrement des toutes les adresses MAC du recepteur bluetooth de toutes les bouees existante


def connexionBouee():

    print ("performing inquiry...")

    nearby_devices = discover_devices(lookup_names = True)

    print ("found %d devices" % len(nearby_devices))

    for name, addr in nearby_devices:
         print (" %s - %s" % (addr, name))

    return nearby_devices



def recuperationDonnee():
    """ recuperationDonnee se connecte a la bouee et recupere les donnees envoyees par celle-ci """

    port = 1   #verifie la connexion de l'appareil a un port specifique ainsi autant garder le meme
    backlog = 1  # nombre maximum d'appareil pouvant se connecter au serveur sur le port
    size = 1024

    # # recupere l'adresse de la bouee a proximite pour se connecter et recuperer les donnees
    adresseServeur = connexionBouee()

    client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)  ## RFCOMM type de socket pour le type de socket bluetooth
    client_sock.bind((adresseServeur, port))
    client_sock.listen(backlog)

    ## accepte la connexion du serveur
    serveur_sock, adresse = client_sock.accept()

    ## recupere les donnees envoyee par le serveur
    donnee = serveur_sock.recv(size)

    # # permet de les enregistrer mais n'est pas operationnel pour l'instant
    # donneeDAO.enregistementDonnee(json.loads(donnee))
    print ("donnees recuperees :", donnee)

    ## ferme les sockets
    client_sock.close()
    serveur_sock.close()
