import json
from datetime import datetime
# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassTournoi:
    def __init__(self):
        pass

    def CreatNewTournois(self,tournoi):
        # insertion des données d'un tournoi dans la nase de donnée
        import json
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        mode_ouv_fichier_json = "a+"
        with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
            db_tournois.insert(tournoi)

        return (tournoi)
