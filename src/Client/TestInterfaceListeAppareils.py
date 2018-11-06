from tkinter import *
from bluetooth import *
from subprocess import *
import bluetooth
from tkinter import messagebox
from tkinter import Label
global ListeAppareils
global listeAdresse
global fenetreListeAppareils

fenetrePrincipale = Tk()
ListeAppareils = []
listeAdresse = []



#boutonTelechargement = fenetrePrincipale.Button(text="Telechargement", command = recuperationDonnee, state="disabled")
#boutonTelechargement.pack()

#boutonTeleversement = fenetrePrincipale.Button(text="Televersement", command = envoieDonnee, state="disabled")
#boutonTeleversement.pack()


def afficherListeAppareils():
    global ListeAppareils
    global listeAdresse
    global fenetreListeAppareils
    fenetreListeAppareils = Tk()

    for ligne in range(len(ListeAppareils)):
        for colonne in range(2):
            Label(fenetreListeAppareils, text='[%s]' % ', '.join(map(str, ListeAppareils[ligne])),borderwidth=1).grid(row=ligne, column=1)
            Button(fenetreListeAppareils, text='Se connecter',command=lambda address=ligne: seConnecter(listeAdresse[address])).grid(row=ligne, column=2)
    fenetreListeAppareils.protocol("WM_DELETE_WINDOW", on_closing)
    fenetreListeAppareils.mainloop()

#--------------------------------------------------------------------------#

def on_closing():
    if messagebox.askokcancel("Quitter","Fermer la liste des appareils ?"):
        fenetreListeAppareils.destroy()
        boutonConnexion.config(state="disabled")

#-------------------------------------------------------------------------------#


def listerAppareils():
    global ListeAppareils
    global listeAdresse
    print ("performing inquiry...")

    nearby_devices = discover_devices(lookup_names = True, flush_cache=True, lookup_class=False)

    #print ("found %d devices" % len(nearby_devices))

    #for name, addr in nearby_devices:
       # print (" %s - %s" % (addr, name))
    
    nearby_devices

    ListeAppareils = nearby_devices

    for name, addr in ListeAppareils:
       listeAdresse.append(name)

    print('Liste adresses :', listeAdresse)    
    boutonConnexion.config(state="normal")

#----------------------------------------------------------------------#
def seConnecter(addresse):
    global fenetreListeAppareils
    global listeAdresse

    listeAdresse.clear()
    print('Liste adresses :', listeAdresse)  
    
    fenetreListeAppareils.destroy()
    boutonConnexion.config(state="disabled")   

    print(addresse)
    port = 3

    sock = BluetoothSocket(RFCOMM)
    sock.connect((addresse, port))
    print("coucou")
    sock.send("hello!!")

    sock.close()
#----------------------------------------------------------------------#


#print('[%s]' % ', '.join(map(str, listeAdresse)))

boutonRechercher = Button(fenetrePrincipale,text="Rechercher des appareils", command = listerAppareils)
boutonRechercher.pack()

boutonConnexion = Button(fenetrePrincipale,text="Choisir un appareil", command = afficherListeAppareils, state="disabled")
boutonConnexion.pack()

boutonTelecharger = Button(fenetrePrincipale,text="Telecharger les donnees", state="disabled")
boutonTelecharger.pack()

boutonTeleverser = Button(fenetrePrincipale,text="Televerser les donnees", state="disabled")
boutonTeleverser.pack()

fenetrePrincipale.mainloop()