from datetime import date
class Partie:
    
    pointage = 0
    nom = "NA"
    dateJeu = 0
    
    
    def __init__(self,score,nom="NA"):
        self.pointage = score
        self.nom = nom
        self.dateJeu = date.today()