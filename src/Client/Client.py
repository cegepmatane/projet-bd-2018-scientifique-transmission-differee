import bluetooth
import donneeDAO


adresseServeur = ["",""]  # enregistrement des toutes les adresses MAC du recepteur bluetooth de toutes les bouees existante


def connexionAuServeur():
    """ la connexion repose sur le fait de verifier si il existe une bouee (pour le moment on ne prend pas en
    compte la possibiltie qu'il puisse en avoir plusieur) """

    nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)

    boueeProximite = ""
    for addr, name in nearby_devices:
        print (" %s - %s" % (addr, name))

        # boucle verifiant que l'appareil detecte est bien une bouee
        for i in adresseServeur:
            if addr == i :
                boueeProximite = addr

    # retourne l'addresse de la bouee a laquel nous pouvons nous connecter
    return boueeProximite



def recuperationDonnee():
    """ recuperationDonnee se connecte a la bouee et recupere les donnees envoyees par celle-ci """

    port = 1   #verifie la connexion de l'appareil a un port specifique ainsi autant garder le meme
    backlog = 1  # nombre maximum d'appareil pouvant se connecter au serveur sur le port
    size = 1024

    # # recupere l'adresse de la bouee a proximite pour se connecter et recuperer les donnees
    adresseServeur = connexionAuServeur()

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
