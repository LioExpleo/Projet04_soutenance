
class ClassJoueursModel:
    # définition des attributs d'instance
    def __init__(self, id_joueur, nom, prenom, date_naissance, sexe, classement):
        self.id_joueur = id_joueur
        self.nom=nom
        self.prenom = prenom
        self.date_naissance=date_naissance
        self.sexe=sexe
        self.classement=classement
        pass

# Permet la création de tous les joueurs à partir des saisies de Ctrl_Joueurs,
# ils seront mis dans la bd par le contrôleur ou directement ici
    def CreatJoueur(self, id_joueur, nom, prenom, date_naissance, sexe, classement):

        # Création de l'instance de classe du joueur à partir des attributs de la classe pour création d'un joueur
        inst_j = ClassJoueursModel(id_joueur, nom, prenom, date_naissance, sexe, classement)

        # CREATION DES DONNEES DU JOUEUR DANS LA BASE DE DONNEES
        # Serialize l'instance joueurs
        joueur = {"id_joueur": inst_j.id_joueur,
                  "Nom": inst_j.nom, "Prenom": inst_j.prenom,
                  "date de naissance": inst_j.date_naissance,
                  "sexe": inst_j.sexe, "Classement": inst_j.classement}
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_joueurs.insert(joueur)

        return (joueur)

    def LectListeListeJoueursBdd():
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        serialised_joueurs = db_joueurs.all()
        index = 0
        liste_joueurs = []
        for i in serialised_joueurs:
            # récupération des champs des joueurs,
            # un par un pour les trier dans l'ordre
            liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                      "nom,", (serialised_joueurs[index]['Nom']),
                      "prénom ,", (serialised_joueurs[index]['Prenom']),
                      "class:",
                      int(serialised_joueurs[index]['Classement'])]
            liste_joueurs.append(liste1)
            index = index + 1
        return (liste_joueurs)

    def MiseADispoJourAClasser(self, index):
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        serialised_joueurs = db_joueurs.all()
        str(serialised_joueurs[index]['id_joueur'])
        joueur_a_classer = str(serialised_joueurs[index]['id_joueur'])
        return (joueur_a_classer)

    def UpdateClassJoueurs(self, nom_donnees, donnees, numero_joueur):
        # Réécriture du classement d'un joueur dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        db_joueurs.update({nom_donnees: donnees},
                          Todo.id_joueur == numero_joueur)
        return ()

    def CreatIdentifiantJoueur(self):
        # Mise à disposition des attributs au modèle pour sérialisation et enregistrement de donnée
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        # Rechercher un id libre dans la base de donnée
        # en incrémentant l'id de test jusqu'à trouver un ID libre
        joueur_cherche = 1
        joueur_trouve = 0
        id_libre = 0
        # Si l' id_joueur_cherché n'est pas trouvé,
        # on le prend pour le mettre à l'id du nouveau joueur
        # sinon, on reboucle jusqu'a trouver un id libre.
        # On commence par regarder si l'id 1 existe
        joueur_trouve = db_joueurs.search(Todo.id_joueur == joueur_cherche)

        joueur_trouv = str(joueur_trouve)
        # recherche de la position de id_joueur dans la chaine
        char = 'id_joueur'
        PositDebNbre = (joueur_trouv.find(char))
        # recherche de la position de nom dans la chaine
        char = "nom"
        PositFinNbre = (joueur_trouv.find(char))

        # Recherche de l'id à partir des positions précédentes et suivantes'
        id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        # tant que l'id cherché existe,
        # on recherche jusqu'à en trouver un libre en l'incrémentant
        while (id_joueur != ""):
            joueur_cherche = joueur_cherche + 1
            joueur_trouve = db_joueurs.search(Todo.id_joueur == joueur_cherche)
            joueur_trouv = str(joueur_trouve)
            char = 'id_joueur'
            PositDebNbre = (joueur_trouv.find(char))
            char = "nom"
            PositFinNbre = (joueur_trouv.find(char))
            id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        else:
            id_libre = joueur_cherche

        identifiant_libre = str(id_libre)

        return (identifiant_libre)

    def MisADispoJoueurBddList(self):
        # Mise à disposition des attributs au modèle pour sérialisation et enregistrement de donnée
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        # suppression {, [, et qui remplace chaque { par un \n
        serialised_joueurs = db_joueurs.all()
        str_joueurs = str(serialised_joueurs)
        la_liste_joueurs = ""
        char = "{"
        for x in range(len(char)):
            la_liste_joueurs = str_joueurs.replace(char, "\n")
            la_liste_joueurs = la_liste_joueurs.replace("}", "")
            la_liste_joueurs = la_liste_joueurs.replace(",", "         ")
            la_liste_joueurs = la_liste_joueurs.replace("'", " ")
        la_liste_joueurs = la_liste_joueurs.replace("[", "")
        liste_joueurs = la_liste_joueurs.replace("]", "    ")
        return (liste_joueurs)

    def SupJoueur(self, numero_joueur):
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        db_joueurs.remove(Todo.id_joueur == numero_joueur)

    def PurgeBddJoueur():
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        db_joueurs.truncate()

    def MisADispoJoueurChargTournoi(self):
        # Mise à disposition des attributs au modèle pour sérialisation et enregistrement de donnée
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        serialised_joueurs = db_joueurs.all()
        joueurs = serialised_joueurs
        return (joueurs)

    def MisADispoJoueurTournoi(self, id_joueur):
        # Mise à disposition des joueurs
        from tinydb import TinyDB, where
        db_joueurs = TinyDB('joueurs.json')
        joueur = (db_joueurs.search(where('id_joueur') == id_joueur))
        return (joueur)

    def MisADispoJoueursRapport():
        # Mise à disposition des joueurs
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        joueurs = db_joueurs.all()
        return (joueurs)
