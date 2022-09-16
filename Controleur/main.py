import c31Geometry2 as geometry
import tkinter as tk
import jeu as j

if __name__ == "__main__" :
    
    
    root = tk.Tk()
    root.title("Jeu.py")
    root.geometry("450x600")

    j.NouvellePartie(root)
    
    root.mainloop()   
    
   
        