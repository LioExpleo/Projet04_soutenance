class ClassMatch:
    def __init__(self, id_tournoi="", num_round="", num_paire="", tuple_match=""):

        self.id_tournoi = id_tournoi
        self.num_round = num_round
        self.num_paire = num_paire
        self.tuple_match = tuple_match

    def CreatMatch(self, id_tournoi, num_round, num_paire, tuple_match):

        # Création de l'instance de match à partir des attributs de la classe pour création d'un match
        inst_r = ClassMatch(id_tournoi, num_round, num_paire, tuple_match)

        # CREATION DES DONNEES DU match DANS LA BASE DE DONNEES
        # Serialize l'instance joueurs
        match = {"ID tournoi ": inst_r.id_tournoi, "numero du round": num_round,
                 "numero paire": inst_r.num_paire, "tuple paire": inst_r.tuple_match}

        from tinydb import TinyDB
        db_match = TinyDB('Match.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_match.insert(match)
