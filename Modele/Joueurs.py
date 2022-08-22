# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where
from Vue.affichage import ClassVueAffichage


class ClassJoueurs:
    def __init__(self):
        pass

#Permet la création de tous les joueurs à partir des saisies de Ctrl_Joueurs, ils seront mis dans la bd par le contrôleur ou directement ici
    def CreatJoueurs(self, joueur):
        #self.joueur=joueur
        #joueur =""

        #CREATION DES DONNEES DU JOUEUR DANS LA BASE DE DONNEES
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        mode_ouv_fichier_json = "a+"
        with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
            pass
        #Ajout du joueur dans la base de données à partir de l'attribut
        db_joueurs.insert(joueur)

        #exemple de reconversion de l'instance sérialisée
        #name = (joueur['Nom'])
        return (joueur)
