from tkinter import *
from bluetooth import *
from subprocess import *
import bluetooth
import sys
import locale
from tkinter import messagebox
from tkinter import Label

global ListeAppareils
global listeAdresse
global fenetreListeAppareils
global langage

langage = locale.getdefaultlocale()[0].split('_')[0]
print(langage)

#---------------------------------------------------------------#
fenetrePrincipale = Tk()
fenetrePrincipale.geometry("300x150")
fenetrePrincipale.resizable(0,0)

framePrincipale = Frame(master=fenetrePrincipale,bg='grey')
framePrincipale.pack_propagate(0)
framePrincipale.pack(fill=BOTH, expand=True)
#---------------------------------------------------------------#
ListeAppareils = []
listeAdresse = []

#---------------------------------------------------------------#
def afficherListeAppareils():
    global ListeAppareils
    global listeAdresse
    global fenetreListeAppareils

    fenetreListeAppareils = Tk()
    fenetreListeAppareils.title(changementLangue("List of devices"))

    frameListeAppareils = Frame(master=fenetreListeAppareils,bg='grey')
    frameListeAppareils.pack_propagate(0)
    frameListeAppareils.pack(fill=BOTH, expand=True)

    for ligne in range(len(ListeAppareils)):
        for colonne in range(2):
            Label(frameListeAppareils, text='[%s]' % ', '.join(map(str, ListeAppareils[ligne])),borderwidth=1).grid(row=ligne, column=1,padx=5,pady=5)
            Button(frameListeAppareils, text=changementLangue("Connect"),command=lambda address=ligne: seConnecter(listeAdresse[address])).grid(row=ligne, column=2,padx=5,pady=5)

    fenetreListeAppareils.protocol("WM_DELETE_WINDOW", on_closing)
    fenetreListeAppareils.mainloop()

#--------------------------------------------------------------------------#
def on_closing():
    global listeAdresse
    if messagebox.askokcancel(changementLangue("Quit"),changementLangue("Close the list of devices?")):
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
#Changement langue 
def changementLangue(s):
    global langage

    spanishStrings = {'Delayed transmission': 'Transmisión retrasada', 'List of devices': 'Lista de dispositivos', 'Connect': 'Conectar', 'Quit': 'Dejar', 'Close the list of devices?': 'Cerrar la lista de dispositivos?', 'Find devices': 'Encontrar dispositivos', 'Choose a device': 'Elija un dispositivo', 'Download data': 'Descargar datos', 'Upload data': 'Subir datos'}
    frenchStrings = {'Delayed transmission': 'Transmission differee', 'List of devices': 'Liste des appareils', 'Connect': 'Se connecter', 'Quit': 'Quitter', 'Close the list of devices?': 'Fermer la liste des appareils ?', 'Find devices': 'Rechercher des appareils', 'Choose a device': 'Choisir un appareil', 'Download data': 'Telecharger les donnees', 'Upload data': 'Televerser les donnees'}
    germanStrings = {'Delayed transmission': 'Verspätete Übertragung', 'List of devices': 'Liste der Geräte', 'Connect': 'Verbinden', 'Quit': 'Verlassen', 'Close the list of devices?': 'Schließen Sie die Liste der Geräte?', 'Find devices': 'Geräte suchen', 'Choose a device': 'Wähle ein Gerät', 'Download data': 'Daten herunterladen', 'Upload data': 'Daten hochladen'}

    if langage == 'en':
        return s
    if langage == 'es':
        return spanishStrings[s]
    if langage == 'fr':
        return frenchStrings[s]
    if langage == 'de':
        return germanStrings[s]
#----------------------------------------------------------------------#


#print('[%s]' % ', '.join(map(str, listeAdresse)))

fenetrePrincipale.title(changementLangue("Delayed transmission"))

boutonRechercher = Button(master=framePrincipale,text=changementLangue("Find devices"), command = listerAppareils)
boutonRechercher.pack(padx=5,pady=5)

boutonConnexion = Button(master=framePrincipale,text=changementLangue("Choose a device"), command = afficherListeAppareils, state="disabled")
boutonConnexion.pack(padx=5,pady=5)

boutonTelecharger = Button(master=framePrincipale,text=changementLangue("Download data"), state="disabled")
boutonTelecharger.pack(padx=5,pady=5)

boutonTeleverser = Button(master=framePrincipale,text=changementLangue("Upload data"), state="disabled")
boutonTeleverser.pack(padx=5,pady=5)

fenetrePrincipale.mainloop()