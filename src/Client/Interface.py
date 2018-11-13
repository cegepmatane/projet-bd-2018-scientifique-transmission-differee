import tkinter as tk
import Client
import connexionNodeJS

class Interface(tk.Frame):

    """Notre fenetre principale
    Tous les widgets sont stockes comme attributs de cette fenetre."""

    connexion = False
    adresseServeur = ""
    LANGUAGE = locale.getdefaultlocale()[0]

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=tk.BOTH)
        self.nb_clic = 0

        # Creation de nos widgets
        self.boutonConnexion = tk.Button(self, text=_("Connexion"), command = self.connexionBouee)
        self.boutonConnexion.pack()

        self.boutonTelechargement = tk.Button(self, text=_("Telechargement"), command = self.recuperationDonnee, state="disabled")
        self.boutonTelechargement.pack()

        self.boutonTeleversement = tk.Button(self, text=_("Televersement"), command = self.envoieDonnee, state="disabled")
        self.boutonTeleversement.pack()



    def connexionBouee(self):
        """Change la valeur du label message pour afficher les bouees a proimite
        permet de ce connecter a la bouee souhaite"""

        """Amelioration possible en permettant de selectionner la bouee souhaiter a proximite si il en existe plusieurs """

        ListeAdresseBouee = Client.connexionBouee()
        #print (ListeAdresseBouee)
        if len(ListeAdresseBouee)!= 0 :  # si il y a appareil a proximite permet d'acceder au bouton de telechargement ou le televersement
            self.boutonTelechargement.config(state="normal")
            


    def recuperationDonnee(self):
        """Lance la récupération des données"""
        Client.recuperationDonnee()


    def envoieDonnee(self):
        """Envoie les donnees au serveur par internet pour le moment non operationnel, il faut d'abord verifier si
        notre base donnee possede des donnees  et si on peut se connecter au serveur"""
        connexionNodeJS.on_send()


    def _(s):
        spanishStrings = {'Connexion': 'Conexión', 'Telechargement': 'Descargar', 'Televersement': 'Subir'}
        englishStrings = {'Connexion': 'Connection', 'Telechargement': 'Download', 'Televersement': 'Uploading'}
        germanStrings = {'Connexion': 'Verbindung', 'Telechargement': 'Herunterladen', 'Televersement': 'Hochladen'}

        if LANGUAGE == 'French':
            return s
        if LANGUAGE == 'Spanish':
            return spanishStrings[s]
        if LANGUAGE == 'English':
            return englishStrings[s]
        if LANGUAGE == 'German':
            return germanStrings[s]



fenetre = tk.Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
