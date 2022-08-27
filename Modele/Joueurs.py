
class ClassJoueursModel:
    def __init__(self):
        pass

# Permet la création de tous les joueurs à partir des saisies de Ctrl_Joueurs,
# ils seront mis dans la bd par le contrôleur ou directement ici
    def CreatJoueur(self, id_joueur, nom, prenom, date_naissance, sexe, classement):
        # CREATION DES DONNEES DU JOUEUR DANS LA BASE DE DONNEES
        # Serialize l'instance joueurs
        joueur = {"id_joueur": id_joueur,
                  "Nom": nom, "Prenom": prenom,
                  "date de naissance": date_naissance,
                  "sexe": sexe, "Classement": classement}
        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_joueurs.insert(joueur)

        return (joueur)
    '''
    def CreatJoueurs(self, joueur):
        # CREATION DES DONNEES DU JOUEUR DANS LA BASE DE DONNEES

        from tinydb import TinyDB
        db_joueurs = TinyDB('joueurs.json')
        # Ajout du joueur dans la base de données à partir de l'attribut
        db_joueurs.insert(joueur)

        return (joueur)
    '''

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
        '''
        for i in serialised_joueurs:
            # récupération des champs des joueurs un par un
            liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                      "nom,", (serialised_joueurs[index]['Nom']),
                      "prénom ,", (serialised_joueurs[index]['Prenom']),
                      "class:", int(serialised_joueurs[index]['Classement'])]
        '''
        return (joueur_a_classer)

    def UpdateClassJoueurs(self, nom_donnees, donnees, numero_joueur):
        # Réécriture du classement d'un joueur dans la base de données
        from tinydb import TinyDB, Query
        Todo = Query()
        print(nom_donnees)
        print(donnees)
        print(numero_joueur)
        db_joueurs = TinyDB('joueurs.json')
        db_joueurs.update({nom_donnees: donnees},
                          Todo.id_joueur == numero_joueur)

        return ()
