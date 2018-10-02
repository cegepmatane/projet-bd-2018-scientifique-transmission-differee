from tkinter import *
import os
import bluetooth

class Interface(Frame):

    """Notre fenêtre principale
    Tous les widgets sont stockés comme attributs de cette fenêtre."""


    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = Label(self, text="Vous n'etes connecte a aucune bouee.")
        self.message.pack()

        self.boutonConnexion = tk.Button(root, text="connexion", command = self.connexionServeur)
        self.boutonConnexion.grid(row=0,column=0)

        self.boutonTelechargement = tk.Button(root, text="Telechargement")
        self.boutonTelechargement.grid(row=1,column=0)

        self.boutonTeleversement = tk.Button(root, text="Televersement")
        self.boutonTeleversement.grid(row=2,column=0)


    def connexionServeur(self):
        """Il y a eu un clic sur le bouton, on change la valeur du label message
        Si on detecte une bouee on se connecte et ainsi on recoit les donnees"""

        nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)

        for addr, name in nearby_devices:
            print (" %s - %s" % (addr, name))
            self.message["text"] = "Bouée détectee : {} ".format(addr)

        os.system("python bluetooth.py client")


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
