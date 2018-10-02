import bluetooth
import donneeDAO

# Preparation Raspberry Pi
# sudo apt-get install python-pip
# sudo pip install pybluez
# sudo pip installl wakeonlan
# commande :  "hciconfig" pour recuperer l'adresse mac du client
# passer le script en Boot


def rechercheAppareil():
    ## recherche de périphérique bluetooth environnent
    print ("recherche peripherique bluetooth proche...")

    nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)
    print ("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        print (" %s - %s" % (addr, name))

    ## affichage donnees des appareils à proximité
    for services in bluetooth.find_service(address = addr):
        print (" Name: %s" % (services["name"]))
        print (" Description: %s" % (services["description"]))
        print (" Protocol: %s" % (services["protocol"]))
        print (" Provider: %s" % (services["provider"]))
        print (" Port: %s" % (services["port"]))
        print (" Service id: %s" % (services["service-id"]))
        print ("")

    return nearby_devices


def connexionAuClient():

    port = 1250   # port pour la connexion en Bluetooth
    ## creer un socket qui ecoute si il y a des connexions acceptee
    serveur_sock = bluetooth.BluetoothServerSocket(bluetooth.RFCOMM)
    # serveur_sock.connect(bluetooth.find_service(address = addr), port)

    ## parcours l'ensemble des appareils detecte pour demander une connexion
    for appareil in rechercheAppareil():
        serveur_sock.connect((appareil, port))
        ## envoie les donnees enregistrer dans la BDD
        serveur_sock.send(donneeDAO.listerDonnee())

    serveur_sock.close()
