import c31Geometry2 as g
# HARDCODE
import tkinter as tk

if __name__ == "__main__" :

    # Créée la fenêtre de base
    root = tk.Tk()
    # Ajouter un titre à la fenêtre
    root.title("Jeu.py")
    # Modifier la taille
    root.geometry("800x800")
    

    # HARDCODE
    vecCarreBlanc = g.Vecteur(300,300)
    vecCarreRouge = g.Vecteur(300,300)
    vecRectangle1 = g.Vecteur(150,150)
    
    
    aireDeJeu = tk.Canvas(root, background="black", height="600", width="600") 
    carreBlanc = g.Carre(aireDeJeu,vecCarreBlanc,450,0,remplissage="white",bordure="white")
    carreRouge = g.Carre(aireDeJeu,vecCarreRouge,50,0,remplissage="red",bordure="red")
    rectangle1 = g.Rectangle(aireDeJeu,vecRectangle1,50,10,0,remplissage="blue",bordure="blue")
    aireDeJeu.grid()
    carreBlanc.draw()
    carreRouge.draw()
    rectangle1.draw()


    # Lancer la boucle principale
    root.mainloop()    