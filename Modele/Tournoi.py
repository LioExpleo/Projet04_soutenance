class ClassModTournoi:
    def __init__(self):
        pass

    def CreatNewTournois(self,  id_tournoi, nom, lieu, date, nbr_rounds,
                         id_j1, id_j2, id_j3, id_j4, id_j5, id_j6, id_j7, id_j8,
                         round_1, round_2, round_3, round_4, round_5, round_6, round_7,
                         temps_matchs, remarque_tournoi):
        # insertion des données de création d'un tournoi
        # dans la nase de données
        # Serialize l'instance tournoi
        tournoi = {"id_tournoi": id_tournoi, "nom": nom, "lieu": lieu,
                   "date du tournoi": date,
                   "nombre de rounds": nbr_rounds, "id_j1": id_j1, "id_j2": id_j2,
                   "id_j3": id_j3, "id_j4": id_j4, "id_j5": id_j5, "id_j6": id_j6,
                   "id_j7": id_j7, "id_j8": id_j8, "round_1+match": round_1,
                   "round_2+match": round_2, "round_3+match": round_3,
                   "round_4+match": round_4, "round_5+match": round_5,
                   "round_6+match": round_6, "round_7+match": round_7,
                   "Temps": temps_matchs,
                   "Remarques de l'organisateur": remarque_tournoi}

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

    def ListeDonneesTournoiSelect(self, nom_donnees, donnees, numero_tournoi):
        # insertion des données des matchs dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournois = TinyDB('tournois.json')

        db_tournois.update({nom_donnees: donnees},
                           Todo.id_tournoi == numero_tournoi)
        return ()

    def CreatIdentifiantTournoi(self):
        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournoi = TinyDB('tournois.json')

        # Rechercher un id libre dans la base de donnée en incrémentant
        # l'id de test jusqu'à trouver un ID libre
        tournoi_cherche = 1
        tournoi_trouve = 0
        id_libre = 0

        # Si l' id_tournoi_cherché n'est pas trouvé, on le prend pour le
        # mettre à l'id du nouveau tournoi
        # sinon, on reboucle jusqu'a trouver un id libre. On commence
        # par regarder si l'id 1 existe
        tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
        tournoi_trouv = str(tournoi_trouve)
        # recherche de la position de id_joueur dans la chaine
        char = 'id_tournoi'
        PositDebNbre = (tournoi_trouv.find(char))
        # recherche de la position de nom dans la chaine
        char = "nom"
        PositFinNbre = (tournoi_trouv.find(char))

        # Recherche de l'id à partir des positions précédentes et suivantes'
        id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        # tant que l'id cherché existe, on recherche jusqu'à en trouver
        # un libre en l'incrémentant
        while (id_tournoi != ""):
            tournoi_cherche = tournoi_cherche + 1
            tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
            tournoi_trouv = str(tournoi_trouve)
            char = 'id_tournoi'
            PositDebNbre = (tournoi_trouv.find(char))

            char = "nom"
            PositFinNbre = (tournoi_trouv.find(char))

            id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        else:
            id_libre = tournoi_cherche

        return (id_libre)

    def AffichageTournois(self):
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        tournois = db_tournois.all()
        return (tournois)

    def SupprimTournois(self, numero_tournoi):
        from tinydb import TinyDB, Query
        Todo=Query()
        db_tournois = TinyDB('tournois.json')
        tournois = db_tournois.all()
        db_tournois.remove(Todo.id_tournoi == numero_tournoi)
        return ()

    def PurgeTournois():
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        db_tournois.truncate()
        return ()

    def Lect1Tournoi(self, tournoi_select):
        import os
        from tinydb import TinyDB, where
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        db_tournois = TinyDB('tournois.json')
        tournoi = (db_tournois.search(where('id_tournoi') == tournoi_select))
        return (tournoi)

    def Lect1Tournoi(self, tournoi_select):
        import os
        from tinydb import TinyDB, where
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        db_tournois = TinyDB('tournois.json')
        tournoi = (db_tournois.search(where('id_tournoi') == tournoi_select))
        return (tournoi)

