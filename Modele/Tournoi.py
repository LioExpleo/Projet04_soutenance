class ClassModTournoi:
    def __init__(self, id_tournoi, nom, lieu, date, nbr_rounds,
                 id_j1, id_j2, id_j3, id_j4, id_j5, id_j6, id_j7, id_j8,
                 round1, round2, round3, round4, round5, round6, round7, temps, description):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_rounds = nbr_rounds
        self.id_j1 = id_j1
        self.id_j2 = id_j2
        self.id_j3 = id_j3
        self.id_j4 = id_j4
        self.id_j5 = id_j5
        self.id_j6 = id_j6
        self.id_j7 = id_j7
        self.id_j8 = id_j8
        self.round1 = round1
        self.round2 = round2
        self.round3 = round3
        self.round4 = round4
        self.round5 = round5
        self.round6 = round6
        self.round7 = round7
        self.temps = temps
        self.description = description

    def CreatNewTournois(self, id_tournoi, nom, lieu, date, nbr_rounds,
                         id_j1, id_j2, id_j3, id_j4, id_j5, id_j6, id_j7, id_j8,
                         round_1, round_2, round_3, round_4, round_5, round_6, round_7,
                         temps_matchs, remarque_tournoi):

        # Création de l'instance de classe du tournoi à partir des attributs de la classe pour la création du tournoi
        inst_t = ClassModTournoi(id_tournoi, nom, lieu, date, nbr_rounds,
                                 id_j1, id_j2, id_j3, id_j4, id_j5, id_j6, id_j7, id_j8,
                                 round_1, round_2, round_3, round_4, round_5, round_6, round_7,
                                 temps_matchs, remarque_tournoi)

        # insertion des données de création d'un tournoi
        # dans la base de données
        # Serialize l'instance tournoi
        tournoi = {"id_tournoi": inst_t.id_tournoi, "nom": inst_t.nom, "lieu": inst_t.lieu,
                   "date du tournoi": inst_t.date,
                   "nombre de rounds": inst_t.nbr_rounds,
                   "id_j1": inst_t.id_j1, "id_j2": inst_t.id_j2,
                   "id_j3": inst_t.id_j3, "id_j4": inst_t.id_j4, "id_j5": inst_t.id_j5, "id_j6": inst_t.id_j6,
                   "id_j7": inst_t.id_j7, "id_j8": inst_t.id_j8,
                   "round_1+match": inst_t.round1, "round_2+match": inst_t.round2,
                   "round_3+match": inst_t.round3, "round_4+match": inst_t.round4,
                   "round_5+match": inst_t.round5, "round_6+match": inst_t.round6,
                   "round_7+match": inst_t.round7,
                   "Temps": inst_t.temps,
                   "Remarques de l'organisateur": inst_t.description}

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
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_tournois.remove(Todo.id_tournoi == numero_tournoi)
        return ()

    def PurgeTournois():
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        db_tournois.truncate()
        return ()

    def Lect1Tournoi(self, tournoi_select):
        from tinydb import TinyDB, where
        db_tournois = TinyDB('tournois.json')
        tournoi = (db_tournois.search(where('id_tournoi') == tournoi_select))
        return (tournoi)

    def LectTournoi():
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        tournoi = db_tournois.all()
        return (tournoi)

    def UpdateDonneesTournoi(self, numero_tournoi, nom_donnee, donnee):

        from tinydb import TinyDB, Query
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_tournois.update({nom_donnee: donnee},
                           Todo.id_tournoi == numero_tournoi)
        return ()
