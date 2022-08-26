import os
from Modele.Joueurs import ClassJoueurs
from Vue.affichage import ClassVueAffichage
from tinydb import TinyDB, Query
Todo = Query()
"""création des joueurs """
"""appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, """
"""suppression d'un joueur de la base de donnée, purge de la base de donnée"""

db_joueurs = TinyDB('joueurs.json')


def creat_new_joueurs():
    # CREATION DE L'ID DU JOUEUR ************************************
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
    str_id_libre = str(id_libre)
    ClassVueAffichage.Affichage(self=True,
                                texte1=str_id_libre, texte2="", texte3="")

    nom = ClassVueAffichage.Input(self=True, texte1="saisie nom :")
    if nom == "":
        nom = ("Joueur " + str(id_libre))
        ClassVueAffichage.Affichage(self=True,
                                    texte1="en absence de nom, le nom par "
                                           "défaut est " + nom,
                                    texte2="", texte3="")
    if nom == "r":
        nom = ("Joueur " + str(id_libre))
        ClassVueAffichage.Affichage(self=True,
                                    texte1="r est un nom interdit, cela "
                                           "correspond à "
                                           "une commande clavier, "
                                           "le nom par défaut est " + nom,
                                    texte2="", texte3="")
    if nom == "E":
        nom = ("Joueur " + str(id_libre))
        ClassVueAffichage.Affichage(self=True,
                                    texte1="E est un nom interdit, "
                                           "cela correspond"
                                           " à une commande clavier, "
                                           "le nom par "
                                           "défaut enregistré est " + nom,
                                    texte2="", texte3="")

    prenom = ClassVueAffichage.Input(self=True,
                                     texte1="saisie prénom :")
    if prenom == "":
        prenom = ("Prenom " + str(id_libre))
        ClassVueAffichage.Affichage(self=True, texte1="en absence de prenom, le prenom "
                                                      "par défaut est " + prenom,
                                    texte2="", texte3="")
    if prenom == "r":
        prenom = ("Prenom " + str(id_libre))
        ClassVueAffichage.Affichage(self=True, texte1="r est un nom interdit, réservé "
                                                      "à commande clavier, le prenom "
                                                      "par défaut est " + prenom,
                                    texte2="", texte3="")
    if prenom == "E":
        prenom = ("Prenom " + str(id_libre))
        ClassVueAffichage.Affichage(self=True, texte1="E est un nom interdit, "
                                                      "cela correspond à une commande clavier, "
                                                      "le prenom par défaut enregistré "
                                                      "est " + prenom,
                                    texte2="", texte3="")

    date_naissance = ClassVueAffichage.Input(self=True,
                                             texte1="date de naissance (format DD/MM/YYYY):")
    if date_naissance == "":
        date_naissance = "01-01-1900"

    sexe = ClassVueAffichage.Input(self=True, texte1="saisie sexe h ou f ou nc :")
    if sexe == "":
        sexe = "nc"
        ClassVueAffichage.Affichage(self=True, texte1="en absence d'indication, "
                                                      "le sexe est indiqué nc",
                                    texte2="", texte3="")
        # print("en absence d'indication, le sexe est indiqué nc")

    classement = ClassVueAffichage.Input(self=True, texte1="classement :")
    # classement = input("classement : \n")
    if classement.isdigit():
        ClassVueAffichage.Affichage(self=True, texte1="classement " + str(classement) + " ok",
                                    texte2="", texte3="")
        # print("classement ok")
    else:
        # classement = 10000
        classement = id_libre + 100
        ClassVueAffichage.Affichage(self=True, texte1="Absence saisie, classement, "
                                                      "par défaut est numéro id + "
                                                      "100, " + str(classement),
                                    texte2="", texte3="")
#  
        # print("Error saisie classement, par défaut, 10000")
    id_joueur = id_libre

    # Serialize l'instance joueurs
    joueur = {"id_joueur": id_joueur,
              "Nom": nom, "Prenom": prenom,
              "date de naissance": date_naissance,
              "sexe": sexe, "Classement": classement}

    ClassJoueurs.CreatJoueurs(self=True, joueur=joueur)
    return (joueur)
    # TEST


def lect_joueurs():  # Afficher la liste des joueurs

    # suppression {, [, et qui remplace chaque { par un \n
    serialised_joueurs = db_joueurs.all()
    str_joueurs = str(serialised_joueurs)

    print_liste_joueurs = ""
    char = "{"
    for x in range(len(char)):
        print_liste_joueurs = str_joueurs.replace(char, "\n")
        print_liste_joueurs = print_liste_joueurs.replace("}", "")
        print_liste_joueurs = print_liste_joueurs.replace(",", "         ")
        print_liste_joueurs = print_liste_joueurs.replace("'", " ")
        # print_liste_joueurs = print_liste_joueurs.replace(":", " ")

    print_liste_joueurs = print_liste_joueurs.replace("[", "")
    print_liste_joueurs = print_liste_joueurs.replace("]", "    ")

    # Appel de la méthode vue du modèle VMC
    # pour affichage de la résultante de la base de données
    ClassVueAffichage.Affichage(self=True, texte1="",
                                texte2="Joueurs de la base de données :",
                                texte3=print_liste_joueurs + "\n")
    return ()


# supprimer un joueur de la liste pour éventuellement le ressaisir
def sup_joueurs(menu_niv_2):
    # db_joueurs.remove(Todo.Nom == menu_niv_2)
    menu_niv_2 = int(menu_niv_2)
    db_joueurs.remove(Todo.id_joueur == menu_niv_2)


# purge de la base de donnée
def purge_joueurs():
    db_joueurs.truncate()


def lecture_joueurs_class_nom():
    # Récupération des informations du fichier
    # JSON du tournoi pour créer les rounds
    from tinydb import TinyDB
    db_joueurs = TinyDB('joueurs.json')

    serialised_joueurs = db_joueurs.all()

    index = 0
    liste_joueurs = []

    for i in serialised_joueurs:
        liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                  "nom,", (serialised_joueurs[index]['Nom']),
                  "prénom ,", (serialised_joueurs[index]['Prenom']),
                  "class:", int(serialised_joueurs[index]['Classement'])]
        liste_joueurs.append(liste1)
        index = index + 1

    from operator import itemgetter
    joueur_id_decroissant = (sorted(liste_joueurs, key=itemgetter(3), reverse=False))

    print("Affichage des joueurs par ordre alphabétique de leurs noms :")
    index = 0
    for i in joueur_id_decroissant:
        print(joueur_id_decroissant[index])
        index = index + 1


def lecture_joueurs_class_id():
    # Récupération des informations du fichier
    # JSON du tournoi pour créer les rounds
    from tinydb import TinyDB
    db_joueurs = TinyDB('joueurs.json')

    serialised_joueurs = db_joueurs.all()

    index = 0
    liste_joueurs = []

    for i in serialised_joueurs:
        liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                  "nom,", (serialised_joueurs[index]['Nom']),
                  "prénom ,", (serialised_joueurs[index]['Prenom']),
                  "class:", int(serialised_joueurs[index]['Classement'])]

        liste_joueurs.append(liste1)
        index = index + 1

    from operator import itemgetter
    joueur_id_decroissant = (sorted(liste_joueurs, key=itemgetter(1), reverse=False))

    print("Affichage des joueurs par ordre "
          "alphabétique de leurs identifiant :")
    index = 0
    for i in joueur_id_decroissant:
        print(joueur_id_decroissant[index])
        index = index + 1


def lecture_joueurs_classement():
    # Récupération des informations du fichier
    # JSON du tournoi pour créer les rounds
    from tinydb import TinyDB
    db_joueurs = TinyDB('joueurs.json')
    serialised_joueurs = db_joueurs.all()

    index = 0
    liste_joueurs = []
    for i in serialised_joueurs:
        liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                  "nom,", (serialised_joueurs[index]['Nom']),
                  "prénom ,", (serialised_joueurs[index]['Prenom']),
                  "class:",
                  int(serialised_joueurs[index]['Classement'])]
        liste_joueurs.append(liste1)
        index = index + 1

    # tri des joueurs
    from operator import itemgetter
    joueur_class_decr = (sorted(liste_joueurs, key=itemgetter(7), reverse=False))

    print("Affichage des joueurs dans l'ordre de leurs classements :")
    index = 0
    for i in joueur_class_decr:
        print(joueur_class_decr[index])
        index = index + 1


def creat_new_class_joueurs():
    # CREATION DE L'ID DU JOUEUR ************************************
    # Récupération des informations du fichier
    # JSON du tournoi pour créer les rounds
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

    # Tri de la liste des joueurs
    from operator import itemgetter
    joueur_class_decr = (sorted(liste_joueurs, key=itemgetter(7), reverse=False))

    print()

    # affichage un par un des joueurs dans l'ordre de leurs classment
    print("Affichage des joueurs dans l'ordre de leurs classements :")
    index = 0
    for i in joueur_class_decr:
        print(joueur_class_decr[index])
        index = index + 1
    index = 0
    liste_joueurs = []

    for i in serialised_joueurs:
        # récupération des champs des joueurs un par un
        liste1 = ["ID joueur n°:", int(serialised_joueurs[index]['id_joueur']),
                  "nom,", (serialised_joueurs[index]['Nom']),
                  "prénom ,", (serialised_joueurs[index]['Prenom']),
                  "class:", int(serialised_joueurs[index]['Classement'])]

        liste_joueurs.append(liste1)

        saisie_new_cl = ClassVueAffichage.\
            Input(self=True,
                  texte1="Saisie nouveau classement joueur "
                         "n°" + str(serialised_joueurs[index]['id_joueur']))

        print()

        if saisie_new_cl == "E":
            break
            os._exit(0)

        if saisie_new_cl.isdigit():
            new_classement = saisie_new_cl
            identifiant_joueur = int(serialised_joueurs[index]['id_joueur'])
            ClassJoueurs.UpdateClassJoueurs(self=True,
                                            nom_donnees="Classement",
                                            donnees=new_classement,
                                            numero_joueur=identifiant_joueur)

            # db_joueurs.update({"Classement": new_classement},
            #                  Todo.id_joueur ==
            #                  int(serialised_joueurs[index]['id_joueur']))
        else:
            print("pas de modification de classement pour ce joueur")

        index = index + 1
