class ClassRound:
    def __init__(self, id_tournoi, num_round, liste_paire1="", liste_paire2="",
                 liste_paire3="", liste_paire4=""):
        self.id_tournoi = id_tournoi
        self.num_round = num_round
        self.liste_paire1 = liste_paire1
        self.liste_paire2 = liste_paire2
        self.liste_paire3 = liste_paire3
        self.liste_paire4 = liste_paire4

    def CreatRound(self, id_tournoi, num_round, liste_paire1, liste_paire2, liste_paire3, liste_paire4):
        print("CreatRound")
        # Création de l'instance de classe du joueur à partir des attributs de la classe pour création d'un joueur
        inst_r = ClassRound(id_tournoi, num_round, liste_paire1, liste_paire2, liste_paire3, liste_paire4)

        # CREATION DES DONNEES DU ROUND DANS LA BASE DE DONNEES
        # Serialize l'instance joueurs
        rounds = {"ID tournoi ": inst_r.id_tournoi, "numero du round": num_round,
                  "Liste paire 1": inst_r.liste_paire1, "Liste paire 2": inst_r.liste_paire2,
                  "Liste paire 3": inst_r.liste_paire3, "Liste paire 4": inst_r.liste_paire4,
                  }

        from tinydb import TinyDB
        db_round = TinyDB('round.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_round.insert(rounds)
