class ClassTournoi:
    def __init__(self):
        pass

    def CreatNewTournois(self, tournoi):
        # insertion des données de création d'un tournoi
        # dans la nase de données
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')

        db_tournois.insert(tournoi)
        return ()

    def UpdateRoundTournois(self, nom_donnees, donnees, numero_tournoi):
        # insertion des données des matchs dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_tournois.update({nom_donnees: donnees},
                           Todo.id_tournoi == numero_tournoi)
        return ()

    def UpdateMatchTournois(self, nom_donnees, donnees, numero_tournoi):
        # insertion des données des matchs dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournois = TinyDB('tournois.json')

        db_tournois.update({nom_donnees: donnees},
                           Todo.id_tournoi == numero_tournoi)
        return ()

    def UpdateJoueurTournois(self, nom_donnees, donnees, numero_tournoi):
        # insertion des données des matchs dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournois = TinyDB('tournois.json')

        db_tournois.update({nom_donnees: donnees},
                           Todo.id_tournoi == numero_tournoi)
        return ()
