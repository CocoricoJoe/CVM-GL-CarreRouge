from msilib.schema import Class
import c31Geometry2 as g
import tkinter as tk
from datetime import date
import csv
from functools import partial
import partie as p

def LireScore(root): 

    filePath = "X:/GL/CVM-GL-CarreRougeDEV/Controleur/stats.csv"
    file = open(filePath) 
    reader = csv.reader(file)
    Data = list(reader)
    
    listbox = tk.Listbox(root, border=10, width=60,height=25)
    for x,y in enumerate(Data):
        listbox.insert(x,y)

    listbox.grid(column=0,row=0)

def EffacerScore():
    filePath = "X:/GL/CVM-GL-CarreRougeDEV/Controleur/stats.csv"
    file = open(filePath, "w" )
    file.truncate()
    file.close()

def EcrireScore(array):
    
   filePath = "X:/GL/CVM-GL-CarreRougeDEV/Controleur/stats.csv" 
   file = open(filePath, "w")
   writer = csv.writer(file)    
   for item in array:
        writer.writerow(item.nom)

class Jeu:
     
    vecCarreNoir = 0
    vecCarreBlanc = 0
    vecCarreRouge = 0
    vecRectangle1 = 0
    vecRectangle2  = 0
    vecRectangle3 = 0
    vecRectangle4 = 0
    velocite = 0
    aireDeJeu = 0
    carreNoir = 0
    carreBlanc = 0
    carreRouge = 0
    etatCarre = "Vivant"
    rectangle1 = 0
    rectangle2 = 0
    rectangle3 = 0
    rectangle4 = 0
    rectangles = 0
    boutonNouvellePartie = 0
    boutonNouvelleSession = 0
    boutonAfficherScore = 0
    boutonEffacerScore = 0
    nomJoueur = 0
    champNom = 0
    scoreSession = 0
    partie = 0
    
    def NouvellePartie(self,root,array):
        
        self.vecCarreNoir  = g.Vecteur(225,225)
        self.vecCarreBlanc = g.Vecteur(225,225)
        self.vecCarreRouge = g.Vecteur(225,225)
        self.vecRectangle1 = g.Vecteur(100,100)
        self.vecRectangle2 = g.Vecteur(300,85)
        self.vecRectangle3 = g.Vecteur(85,300)
        self.vecRectangle4 = g.Vecteur(355,340)
        
        self.velocite = 1
        
        self.aireDeJeu = tk.Canvas(root, background="white", height="450", width="450") 
        self.carreNoir = g.Carre(self.aireDeJeu,self.vecCarreNoir,450,0,remplissage="black",bordure="black")
        self.carreBlanc = g.Carre(self.aireDeJeu,self.vecCarreBlanc,350,0,remplissage="white",bordure="white")
        self.carreRouge = g.Carre(self.aireDeJeu,self.vecCarreRouge,40,0,remplissage="red",bordure="red")
        self.rectangle1 = g.Rectangle(self.aireDeJeu,self.vecRectangle1,60,60,0,remplissage="blue",bordure="blue")
        self.rectangle2 = g.Rectangle(self.aireDeJeu,self.vecRectangle2,60,50,0,remplissage="blue",bordure="blue")
        self.rectangle3 = g.Rectangle(self.aireDeJeu,self.vecRectangle3,30,60,0,remplissage="blue",bordure="blue")
        self.rectangle4 = g.Rectangle(self.aireDeJeu,self.vecRectangle4,100,10,0,remplissage="blue",bordure="blue")
        self.rectangles = [self.rectangle1,self.rectangle2,self.rectangle3,self.rectangle4]
        self.boutonNouvellePartie = tk.Button(root, text = "Nouvelle partie", command=partial(self.NouvellePartie,root,array))
        self.boutonNouvelleSession = tk.Button(root, text = "Nouvelle session", command=partial(self.NouvelleSession,root))
        self.boutonAfficherScore = tk.Button(root, text = "Afficher les scores", command=partial(LireScore,root))
        self.boutonEffacerScore = tk.Button(root,text = "Effacer les scores", command=partial(EffacerScore))
        self.nomJoueur = tk.StringVar(root)
        self.champNom = tk.Entry(root,textvariable=self.nomJoueur,width=30)
        self.champNom.insert(0,"Entrez un nom d'utilisateur")
        
        self.aireDeJeu.grid(column=0,row=0)
        self.boutonNouvellePartie.grid(column=0,row=2)
        self.boutonNouvelleSession.grid(column=0,row=3)
        self.champNom.grid(column=0, row=1)
        self.boutonAfficherScore.grid(column=0, row=4)
        self.boutonEffacerScore.grid(column=0,row=5)
        self.carreNoir.draw()
        self.carreBlanc.draw()
        self.carreRouge.draw()
        self.rectangle1.draw()
        self.rectangle2.draw()
        self.rectangle3.draw()
        self.rectangle4.draw()
        
    def NouvelleSession(self,root):
        
        self.scoresSession = []
        self.partie = p.Partie(1000,"je suis cavolo")
        #self.scoresSession.append(partie)
        #EcrireScore(scoresSession)
        self.NouvellePartie(root,self.scoresSession)
        
    # Collisions 
    def collisionRectangle(self, rectangle:g.Polygone):
        colli = ''
        points = rectangle.get_coordonnees()
        xPoints = [point[0] for point in points]
        yPoints = [point[1] for point in points]
        hautRectangle = min(yPoints)
        gaucheRectangle = min(xPoints)
        basRectangle = max(yPoints)
        droiteRectangle = max(xPoints)
        
        if hautRectangle <= 0 or basRectangle >= 450:
            colli = 'Y'
        if gaucheRectangle <= 0 or droiteRectangle >= 449:
            colli = 'X'
        
        return colli


    def collisionCarre(self):
        collision = False
        centreCarre = self.carreRouge.get_barycentre()
        
        for rectangle in self.rectangles:
            for point in rectangle.get_coordonnees():
                if (g.Vecteur(point[0],point[1]).distance(centreCarre) <= 20):
                    self.carreRouge.set_remplissage("black")  
                    collision = True  
                                        
        return collision


        
    # Déplacements
    def deplacementRectangles(self):
        for rectangle in self.rectangles:
            
            if self.collisionRectangle(rectangle) == 'X':
                rectangle.sensX *= -1
            if self.collisionRectangle(rectangle) == 'Y':
                rectangle.sensY *= -1                
                
            nouvellePosition = (rectangle.get_barycentre() + g.Vecteur(self.velocite*rectangle.sensX,self.velocite*rectangle.sensY)) - rectangle.get_barycentre()                
            rectangle.translate(nouvellePosition)
            rectangle.draw()   
            

    def deplacementCarreRouge(self, e):
        x= e.x
        y= e.y
        nouvellePosition = g.Vecteur(x,y) - self.carreRouge.get_barycentre()
        self.carreRouge.translate(nouvellePosition)    
            
        if self.collisionCarre():
            self.etatCarre = "Mort"
        
        print(self.etatCarre)            
        self.carreRouge.draw()
            
            
    # Actualiser le jeu
    def update(self):
            self.deplacementRectangles()