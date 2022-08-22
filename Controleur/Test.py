import os
import re
import time
import json
from Modele.Tournoi import ClassTournoi
from Vue.affichage import ClassVueAffichage
from tinydb import TinyDB, Query, where
from datetime import datetime
from Controleur.Ctrl_Tournoi import select_tournoi
Todo = Query()

"""création des joueurs - appel du modele joueur 
lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, 
suppression d'un joueur de la base de donnée, purge de la base de donnée"""

def creat_match():
        print("saisie des scores du match")

        id_t = (tournoi[0]['id_tournoi'])
        ClassVueAffichage.Affichage(self=True, texte1= "id_tournoi :", texte2=str(id_t),texte3="")

        try:
            round_en_cours = (tournoi[0]['round_en_cours'])
            ClassVueAffichage.Affichage(self=True, texte1="round en cours :", texte2=round_en_cours, texte3="")
            print("round_en_cours : " + str(round_en_cours))
        except KeyError:
            lassVueAffichage.Affichage(self=True, texte1="Le round doit être créé dans le match pour que les scores du match puissent être saisis, - R suivi de + - pour créer le 1er round", texte2="", texte3="")
            print("Le round doit être créé dans le match pour que les scores du match puissent être saisis, - R suivi de + - pour créer le 1er round")
            os._exit(0)

        tournoi = id_t
        round=round_en_cours
        if round_en_cours == 1:
            creat_match_r1(tournoi,round)
        else:
            creat_match_r2(tournoi, round)
