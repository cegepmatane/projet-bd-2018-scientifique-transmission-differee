from tkinter import *
from bluetooth import *
from subprocess import *
import bluetooth
import sys
from tkinter import messagebox
from tkinter import Label
global ListeAppareils
global listeAdresse
global fenetreListeAppareils

#---------------------------------------------------------------#
fenetrePrincipale = Tk()
fenetrePrincipale.title('Transmission differee')
#fenetrePrincipale.pack_propagate(0)
fenetrePrincipale.geometry("300x150")
fenetrePrincipale.resizable(0,0)

framePrincipale = Frame(master=fenetrePrincipale,bg='grey')
framePrincipale.pack_propagate(0)
framePrincipale.pack(fill=BOTH, expand=True)

#---------------------------------------------------------------#
fenetreListeAppareils = Tk()
fenetreListeAppareils.title("Liste appareils")

frameListeAppareils = Frame(master=fenetreListeAppareils,bg='grey')
frameListeAppareils.pack_propagate(0)
frameListeAppareils.pack(fill=BOTH, expand=True)

ListeAppareils = []
listeAdresse = []
#---------------------------------------------------------------#

def afficherListeAppareils():
    global ListeAppareils
    global listeAdresse
    global fenetreListeAppareils

    for ligne in range(len(ListeAppareils)):
        for colonne in range(2):
            Label(frameListeAppareils, text='[%s]' % ', '.join(map(str, ListeAppareils[ligne])),borderwidth=1).grid(row=ligne, column=1,padx=5,pady=5)
            Button(frameListeAppareils, text='Se connecter',command=lambda address=ligne: seConnecter(listeAdresse[address])).grid(row=ligne, column=2,padx=5,pady=5)
    fenetreListeAppareils.protocol("WM_DELETE_WINDOW", on_closing)
    fenetreListeAppareils.mainloop()
#--------------------------------------------------------------------------#

def on_closing():
    global listeAdresse
    if messagebox.askokcancel("Quitter","Fermer la liste des appareils ?"):
        fenetreListeAppareils.destroy()
        boutonConnexion.config(state="disabled")
        listeAdresse.clear()
        print('Liste adresses :', listeAdresse)
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

    print("Connecte !")
    sock.send("Bonjour monde !")
    print("Message envoye !")
    data = sock.recv(1024)
    print ('Reception : ', data.decode())


    sock.close()

    """while True :
        message = raw_input('Envoyer :')
        if not message : break
        sock.send(message)
        data = sock.recv(1024)
        print ('Reception : ', data)
    sock.close()"""
#----------------------------------------------------------------------#


#print('[%s]' % ', '.join(map(str, listeAdresse)))

boutonRechercher = Button(master=framePrincipale,text="Rechercher des appareils", command = listerAppareils)
boutonRechercher.pack(padx=5,pady=5)

boutonConnexion = Button(master=framePrincipale,text="Choisir un appareil", command = afficherListeAppareils, state="disabled")
boutonConnexion.pack(padx=5,pady=5)

boutonTelecharger = Button(master=framePrincipale,text="Telecharger les donnees", state="disabled")
boutonTelecharger.pack(padx=5,pady=5)

boutonTeleverser = Button(master=framePrincipale,text="Televerser les donnees", state="disabled")
boutonTeleverser.pack(padx=5,pady=5)

fenetrePrincipale.mainloop()