import c31Geometry2 as g
# HARDCODE
import tkinter as tk

if __name__ == "__main__" :

    # Créée la fenêtre de base
    root = tk.Tk()
    # Ajouter un titre à la fenêtre
    root.title("Jeu.py")
    # Modifier la taille
    root.geometry("600x600")
    

    # HARDCODE
    vecCarreNoir  = g.Vecteur(250,250)
    vecCarreBlanc = g.Vecteur(225,225)
    vecCarreRouge = g.Vecteur(225,225)
    vecRectangle1 = g.Vecteur(100,100)
    vecRectangle2 = g.Vecteur(300,85)
    vecRectangle3 = g.Vecteur(85,300)
    vecRectangle4 = g.Vecteur(355,340)
    
    
    
    aireDeJeu = tk.Canvas(root, background="white", height="500", width="500") 
    carreNoir = g.Carre(aireDeJeu,vecCarreNoir,500,0,remplissage="black",bordure="black")
    carreBlanc = g.Carre(aireDeJeu,vecCarreBlanc,450,0,remplissage="white",bordure="white")
    carreRouge = g.Carre(aireDeJeu,vecCarreRouge,40,0,remplissage="red",bordure="red")
    rectangle1 = g.Rectangle(aireDeJeu,vecRectangle1,60,60,0,remplissage="blue",bordure="blue")
    rectangle2 = g.Rectangle(aireDeJeu,vecRectangle2,60,50,0,remplissage="blue",bordure="blue")
    rectangle3 = g.Rectangle(aireDeJeu,vecRectangle3,30,600,0,remplissage="blue",bordure="blue")
    rectangle4 = g.Rectangle(aireDeJeu,vecRectangle4,100,10,0,remplissage="blue",bordure="blue")
    
    aireDeJeu.grid()
    carreNoir.draw()
    carreBlanc.draw()
    carreRouge.draw()
    rectangle1.draw()


    # Lancer la boucle principale
    root.mainloop()    