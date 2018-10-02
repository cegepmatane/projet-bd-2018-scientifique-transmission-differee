import tkinter as tk


root = tk.Tk()



boutonConnexion = tk.Button(root, text="connexion")
boutonConnexion.grid(row=0,column=0)

boutonTelechargement = tk.Button(root, text="Telechargement")
boutonTelechargement.grid(row=1,column=0)

boutonTeleversement = tk.Button(root, text="Televersement")
boutonTeleversement.grid(row=2,column=0)

root.mainloop()
