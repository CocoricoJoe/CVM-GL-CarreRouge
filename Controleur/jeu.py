from curses import COLOR_BLACK
from tkinter import Canvas
from c31Geometry2 import Vecteur
import c31Geometry2 as geometry
# HARDCODE
import tkinter as tk

if __name__ == "__main__" :

    # Créée la fenêtre de base
    root = tk.Tk()
    # Ajouter un titre à la fenêtre
    root.title("Jeu.py")
    # Modifier la taille
    root.geometry("600x800")
    
    


    # HARDCODE

    aireDeJeu = tk.Canvas(root, background="black", height="500", width="600")
    carreRouge = geometry.Carre(canvas=aireDeJeu, origine=Vecteur(200,300), largeur=150, remplissage="red", bordure="red", epaisseur=0)
    aireDeJeu.grid()
    
    


    # Lancer la boucle principale
    root.mainloop()    