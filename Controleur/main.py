from multiprocessing.dummy import Event
from jeu import Jeu
import c31Geometry2 as geometry
import tkinter as tk
import jeu as j

if __name__ == "__main__" :
    
    jeu = Jeu()
    root = tk.Tk()
    root.title("Jeu.py")
    root.geometry("450x600")

    jeu.NouvelleSession(root)
    #print(jeu.partie.nom)
    
    root.bind('<ButtonPress-1>', lambda e : jeu.clicCarreRouge(e, root))
    
    root.mainloop()