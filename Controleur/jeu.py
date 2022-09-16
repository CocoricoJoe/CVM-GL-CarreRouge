from pkgutil import read_code
import re
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
    vecCarreNoir  = g.Vecteur(225,225)
    vecCarreBlanc = g.Vecteur(225,225)
    vecCarreRouge = g.Vecteur(225,225)
    vecRectangle1 = g.Vecteur(100,100)
    vecRectangle2 = g.Vecteur(300,85)
    vecRectangle3 = g.Vecteur(85,300)
    vecRectangle4 = g.Vecteur(355,340)
    
    velocite = 1
    
    
    
    aireDeJeu = tk.Canvas(root, background="white", height="450", width="450") 
    carreNoir = g.Carre(aireDeJeu,vecCarreNoir,450,0,remplissage="black",bordure="black")
    carreBlanc = g.Carre(aireDeJeu,vecCarreBlanc,350,0,remplissage="white",bordure="white")
    carreRouge = g.Carre(aireDeJeu,vecCarreRouge,40,0,remplissage="red",bordure="red")
    rectangle1 = g.Rectangle(aireDeJeu,vecRectangle1,60,60,0,remplissage="blue",bordure="blue")
    rectangle2 = g.Rectangle(aireDeJeu,vecRectangle2,60,50,0,remplissage="blue",bordure="blue")
    rectangle3 = g.Rectangle(aireDeJeu,vecRectangle3,30,60,0,remplissage="blue",bordure="blue")
    rectangle4 = g.Rectangle(aireDeJeu,vecRectangle4,100,10,0,remplissage="blue",bordure="blue")
    rectangles = [rectangle1, rectangle2, rectangle3, rectangle4]
    
    
    aireDeJeu.grid()
    carreNoir.draw()
    carreBlanc.draw()
    carreRouge.draw()
    rectangle1.draw()
    rectangle2.draw()
    rectangle3.draw()
    rectangle4.draw()
    
    # Collisions   
    
    def collisionRectangle(rectangle:g.Polygone):
        colli = ''
        
        for point in rectangle.get_coordonnees():
            if point[0] <= 0 or point[0] >= 449:
                colli = 'X'
            if point[1] <= 0 or point[1] >= 450:
                colli = 'Y'
            # if point[0] <= 0 and point[1] <= 0 or point[0] <= 0 and point[1] >= 450 or point[1] <= 0 and point[0] >= 450 or point[1] >= 450 and point[0] >= 450 :
            #     colli = 'XY'
            return colli
    
    def collisionCarre(carre:g.Polygone, rectangles):
        
        # min/max pour trouver les coins        
        
        centreCarre = carre.get_barycentre()
        collision = False
        for rectangle in rectangles:
            for point in rectangle.get_coordonnees():
                if (g.Vecteur(point[0],point[1]).distance(centreCarre) <= 20):
                    collision = True
        return collision
    
        # collision = False
            # pointsCarre = carre.get_coordonnees()
            # pointsRectangles = []
            # for rectangle in rectangles:
            #     for point in rectangle.get_coordonnees():
            #         pointsRectangles.append(point)
            
            # for pointC in pointsCarre:
            #     for pointR in pointsRectangles:
            #         if pointC == pointR:
            #             collision = True
            #             break
            
            # return collision
            
                    
    
    
    # Déplacements
    def deplacementRectangles(e):
        for rectangle in rectangles:
            
            if collisionRectangle(rectangle) == 'X':
                rectangle.sensX *= -1
            if collisionRectangle(rectangle) == 'Y':
                rectangle.sensY *= -1                
                
            nouvellePosition = (rectangle.get_barycentre() + g.Vecteur(velocite*rectangle.sensX,velocite*rectangle.sensY)) - rectangle.get_barycentre()                
            rectangle.translate(nouvellePosition)
            rectangle.draw()   
            
    
    def deplacementCarreRouge(e):
        x= e.x
        y= e.y
        nouvellePosition = g.Vecteur(x,y) - carreRouge.get_barycentre()
        carreRouge.translate(nouvellePosition)        
        if collisionCarre(carreRouge, rectangles):
                carreRouge.set_remplissage("black")
        carreRouge.draw()
             
    root.bind('<Motion>', deplacementRectangles)
    root.bind('<Motion>', deplacementCarreRouge)
        
    
    
    # Lancer la boucle principale
    root.mainloop()