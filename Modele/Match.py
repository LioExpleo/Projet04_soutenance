from Controleur.Ctrl_Tournoi import select_tournoi
from Controleur.fonctions import creat_dict
from datetime import datetime
import os

class ClassMatch:
    def __init__(self, id_tournoi="",nom_round="", type="", remarque = "", liste_paire1 ="",liste_paire2 ="",liste_paire3="",liste_paire4=""):

        self.id_tournoi = id_tournoi
        self.nom_round=nom_round
        self.type = type
        self.remarque=remarque
        self.liste_paire1 = liste_paire1
        self.liste_paire2 = liste_paire2
        self.liste_paire3 = liste_paire3
        self.liste_paire4 = liste_paire4

    def CreatMatch(self):
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatMatch")
        score_Liste_paire1 = input("score : \n")
        if score_Liste_paire1.isdigit():
            pass
            #print("classement ok")
        else:
            print("Error saisie")
