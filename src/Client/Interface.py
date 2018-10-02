import tkinter as tk
import os
import bluetooth

class Interface(tk.Frame):

    """Notre fenetre principale
    Tous les widgets sont stockes comme attributs de cette fenetre."""


    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=tk.BOTH)
        self.nb_clic = 0

        # Creation de nos widgets
        self.message = tk.Label(self, text="Vous n'etes connecte a aucune bouee.")
        self.message.pack()

        self.boutonConnexion = tk.Button(self, text="connexion", command = self.connexionServeur)
        self.boutonConnexion.pack()

        self.boutonTelechargement = tk.Button(self, text="Telechargement")
        self.boutonTelechargement.pack()

        self.boutonTeleversement = tk.Button(self, text="Televersement")
        self.boutonTeleversement.pack()


    def connexionServeur(self):
        """Il y a eu un clic sur le bouton, on change la valeur du label message
        Si on detecte une bouee on se connecte et ainsi on recoit les donnees"""

        nearby_devices = bluetooth.discover_devices(lookup_names = True, flush_cache = True, duration = 20)

        for addr, name in nearby_devices:
            print (" %s - %s" % (addr, name))
            self.message["text"] = "Bouee detectee : {} ".format(addr)

        os.system("python bluetooth.py client")


fenetre = tk.Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
