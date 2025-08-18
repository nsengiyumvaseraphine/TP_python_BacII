import tkinter as tk
from tkinter import messagebox 


def action_bouton():
    """Fonction appelée lorsque le bouton est cliqué.""" 
    print("Le bouton a été cliqué !") 
    messagebox.showinfo("Information", "Vous avez cliqué sur le bouton !")

def afficher_texte():
    """Récupère et affiche le texte des widgets de saisie.""" 
    nom_saisi = champ_saisie.get() 
    message_saisi = zone_texte.get("1.0", tk.END) # "1.0"signifie à partir de la 1ère ligne, 0ème caractère 
    print(f"Nom : {nom_saisi}") 
    print(f"Message : {message_saisi}") 
    messagebox.showinfo("Informations", f"Nom: {nom_saisi}\nMessage: {message_saisi}") 

fenetre = tk.Tk() 
fenetre.title("Mon application avec widgets") 
fenetre.geometry("400x300") 

# Créer une étiquette (Label) 
etiquette = tk.Label(fenetre, text="Bonjour, Tkinter !") 
etiquette.pack(pady=10) 

bouton = tk.Button(fenetre, text="Cliquez-moi",command=action_bouton)  
bouton.pack(pady=10) 

# Champ de saisie pour une seule ligne 
label_nom = tk.Label(fenetre, text="Entrez votre nom :") 
label_nom.pack(pady=5) 
champ_saisie = tk.Entry(fenetre, width=40) 
champ_saisie.pack() 
# Zone de texte pour plusieurs lignes 
label_message = tk.Label(fenetre, text="Entrez votre message :") 
label_message.pack(pady=5) 
zone_texte = tk.Text(fenetre, height=5, width=40) 
zone_texte.pack() 
# Bouton pour afficher les saisies 
bouton_afficher = tk.Button(fenetre, text="Afficher",command=afficher_texte) 
bouton_afficher.pack(pady=10) 


fenetre.mainloop()