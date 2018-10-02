import bluetooth


def connexionAuServeur():
    # connexion bluetooth au serveur (Raspberry) en acceptant la connexion emise celui-ci
    adresseServeur = ["",""]  # enregistrement des adresses MAC du recepteur bluetooth de toute les bouees
    port = 1250
    backlog = 1  # nombre maximum d'appareil pouvant se connecter au serveur sur le port
    size = 1024

    for serveur in adresseServeur:
        ## RFCOMM type de socket pour le type de socket bluetooth
        client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        client_sock.bind((serveur, port))
        client_sock.listen(backlog)

        return serveur



def recuperationDonnee(adresseServeur):
    ## accepte la connexion du serveur
    serveur_sock, adresse = client_sock.accept()

    ## recupere les donnees envoyee par le serveur
    donnee = serveur_sock.recv(size)
    print ("donnees recuperées :", donnee)

    ## ferme les sockets
    client_sock.close()
    serveur_sock.close()

    # while True:
    #     serveur_sock, serveurInfo = client_sock.accept()
    #     try:
    #         while True:
    #             donnee = serveur_sock.recv(size)
    #             if donnee:
    #                 print(donnee)
    #     except:
    #         print("Fermeture du socket")
    #         serveur_sock.close()
    # client_sock.close()
