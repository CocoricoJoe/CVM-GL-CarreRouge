from cProfile import label
from pyparsing import col
import c31Geometry2 as g
import tkinter as tk
from datetime import date
import csv

def LireScore(): 

    filePath = "C:/travail/CVM-GL-CarreRouge/Controleur/stats.csv"
    file = open(filePath) 
    reader = csv.reader(file)
    Data = list(reader)
    
    listbox = tk.Listbox(root, border=10, width=60,height=25)
    for x,y in enumerate(Data):
        listbox.insert(x,y)

    listbox.grid(column=0,row=0)
    
    

def EcrireScore(array):
    
   filePath = "C:/travail/CVM-GL-CarreRouge/Controleur/stats.csv" 
   file = open(filePath)
   writer = csv.writer(file)    
   for partie in array:
        writer.writerow(partie.nom)

def NouvellePartie():
    
    vecCarreNoir  = g.Vecteur(225,225)
    vecCarreBlanc = g.Vecteur(225,225)
    vecCarreRouge = g.Vecteur(225,225)
    vecRectangle1 = g.Vecteur(100,100)
    vecRectangle2 = g.Vecteur(300,85)
    vecRectangle3 = g.Vecteur(85,300)
    vecRectangle4 = g.Vecteur(355,340)
    
    aireDeJeu = tk.Canvas(root, background="white", height="450", width="450") 
    carreNoir = g.Carre(aireDeJeu,vecCarreNoir,450,0,remplissage="black",bordure="black")
    carreBlanc = g.Carre(aireDeJeu,vecCarreBlanc,350,0,remplissage="white",bordure="white")
    carreRouge = g.Carre(aireDeJeu,vecCarreRouge,40,0,remplissage="red",bordure="red")
    rectangle1 = g.Rectangle(aireDeJeu,vecRectangle1,60,60,0,remplissage="blue",bordure="blue")
    rectangle2 = g.Rectangle(aireDeJeu,vecRectangle2,60,50,0,remplissage="blue",bordure="blue")
    rectangle3 = g.Rectangle(aireDeJeu,vecRectangle3,30,60,0,remplissage="blue",bordure="blue")
    rectangle4 = g.Rectangle(aireDeJeu,vecRectangle4,100,10,0,remplissage="blue",bordure="blue")
    boutonNouvellePartie = tk.Button(root, text = "Nouvelle partie", command=NouvellePartie)
    boutonNouvelleSession = tk.Button(root, text = "Nouvelle session", command=NouvelleSession)
    boutonAfficherScore = tk.Button(root, text = "Afficher les scores", command=LireScore)
    nomJoueur = tk.StringVar(root)
    champNom = tk.Entry(root,textvariable=nomJoueur,width=30)
    champNom.insert(0,"Entrez un nom d'utilisateur")
    
    aireDeJeu.grid(column=0,row=0)
    boutonNouvellePartie.grid(column=0,row=2)
    boutonNouvelleSession.grid(column=0,row=3)
    champNom.grid(column=0, row=1)
    boutonAfficherScore.grid(column=0, row=4)
    carreNoir.draw()
    carreBlanc.draw()
    carreRouge.draw()
    rectangle1.draw()
    rectangle2.draw()
    rectangle3.draw()
    rectangle4.draw()
    
def NouvelleSession():
    NouvellePartie()
    partie = Partie(1000,"FuckTheo")
    scoresSession = []
    scoresSession.append(partie)
    EcrireScore(scoresSession)

class Partie:
    
    pointage = 0
    nom = "NA"
    dateJeu = 0
    
    
    def __init__(self,score,nom="NA"):
        self.pointage = score
        self.nom = nom
        self.dateJeu = date.today()
  
    


if __name__ == "__main__" :

    
    root = tk.Tk()
    root.title("Jeu.py")
    root.geometry("450x600")

    NouvellePartie()
    
    
    
    root.mainloop()   
    
   
        
    
