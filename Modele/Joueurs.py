
class ClassJoueurs:
    def __init__(self):
        pass

# Permet la création de tous les joueurs à partir des saisies de Ctrl_Joueurs,
# ils seront mis dans la bd par le contrôleur ou directement ici
    def CreatJoueurs(self, joueur):
        # CREATION DES DONNEES DU JOUEUR DANS LA BASE DE DONNEES
        from tinydb import TinyDB
        # Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_joueurs.insert(joueur)

        return (joueur)

    def UpdateClassJoueurs(self, nom_donnees, donnees, numero_joueur):
        # Réécriture du classement d'un joueur dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        db_joueurs.update({nom_donnees: donnees},
                          Todo.id_joueur == numero_joueur)

        return ()
