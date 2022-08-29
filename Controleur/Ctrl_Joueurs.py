
class ClassJoueurs():
    def __init__(self):
        pass
    """création des joueurs """
    """appel du modele joueur lors de la création des joueurs"""
    """affichage liste joueurs de la base de donnée, """
    """suppression d'un joueur de la base de donnée, purge de la base de donnée"""

    def creat_new_joueurs():
        from Vue.affichage import ClassVueAffichage
        from Modele.Joueurs import ClassJoueursModel
        # CREATION DE L'ID DU JOUEUR ************************************

        # Appel du Modèle pour création d'un identifiant du joueur, retourne le prochain identifiant libre
        str_id_libre = ClassJoueursModel.CreatIdentifiantJoueur(self=True)
        # Appel de Vue, méthode affichage
        ClassVueAffichage.Affichage(self=True,
                                    texte1=str_id_libre, texte2="", texte3="")

        # Appel de la méthode de saisie dans vue pour saisie du nom
        nom = ClassVueAffichage.Input(self=True, texte1="saisie nom :")
        if nom == "":
            nom = ("Joueur " + str_id_libre)
            ClassVueAffichage.Affichage(self=True,
                                        texte1="en absence de nom, le nom par "
                                               "défaut est " + nom,
                                        texte2="", texte3="")
        if nom == "r":
            nom = ("Joueur " + str_id_libre)
            ClassVueAffichage.Affichage(self=True,
                                        texte1="r est un nom interdit, cela "
                                               "correspond à "
                                               "une commande clavier, "
                                               "le nom par défaut est " + nom,
                                        texte2="", texte3="")
        if nom == "E":
            nom = ("Joueur " + str_id_libre)
            ClassVueAffichage.Affichage(self=True,
                                        texte1="E est un nom interdit, "
                                               "cela correspond"
                                               " à une commande clavier, "
                                               "le nom par "
                                               "défaut enregistré est " + nom,
                                        texte2="", texte3="")

        prenom = ClassVueAffichage.Input(self=True,
                                         texte1="saisie prénom :")

        # Appel de la méthode de saisie dans vue pour saisie du prénom
        if prenom == "":
            prenom = ("Prenom " + str_id_libre)
            ClassVueAffichage.Affichage(self=True, texte1="en absence de prenom, le prenom "
                                                          "par défaut est " + prenom,
                                        texte2="", texte3="")
        if prenom == "r":
            prenom = ("Prenom " + str_id_libre)
            ClassVueAffichage.Affichage(self=True, texte1="r est un nom interdit, réservé "
                                                          "à commande clavier, le prenom "
                                                          "par défaut est " + prenom,
                                        texte2="", texte3="")
        if prenom == "E":
            prenom = ("Prenom " + str_id_libre)
            ClassVueAffichage.Affichage(self=True, texte1="E est un nom interdit, "
                                                          "cela correspond à une commande clavier, "
                                                          "le prenom par défaut enregistré "
                                                          "est " + prenom,
                                        texte2="", texte3="")

        # Appel de la méthode de saisie dans vue pour saisie de la date de naissance
        date_naissance = ClassVueAffichage.Input(self=True,
                                                 texte1="date de naissance (format DD/MM/YYYY):")
        if date_naissance == "":
            date_naissance = "01-01-1900"

        # Appel de la méthode de saisie dans vue pour saisie sexe
        sexe = ClassVueAffichage.Input(self=True, texte1="saisie sexe h ou f ou nc :")
        if sexe == "":
            sexe = "nc"
            ClassVueAffichage.Affichage(self=True, texte1="en absence d'indication, "
                                                          "le sexe est indiqué nc",
                                        texte2="", texte3="")

        # Appel de la méthode de saisie dans vue pour saisie du classement
        classement = ClassVueAffichage.Input(self=True, texte1="classement :")
        if classement.isdigit():
            ClassVueAffichage.Affichage(self=True, texte1="classement " + str(classement) + " ok",
                                        texte2="", texte3="")
        else:
            # classement par défaut
            classement = int(str_id_libre) + 100
            ClassVueAffichage.Affichage(self=True, texte1="Absence saisie, classement, "
                                                          "par défaut est numéro id + "
                                                          "100, " + str(classement),
                                        texte2="", texte3="")

        # Mise à disposition des attributs de la méthode du modèle pour sérialisation et enregistrement de donnée
        id_joueur = int(str_id_libre)
        ClassJoueursModel.CreatJoueur(self=True, id_joueur=id_joueur, nom=nom, prenom=prenom,
                                      date_naissance=date_naissance, sexe=sexe, classement=classement)
        return ()

    def lect_joueurs():
        from Vue.affichage import ClassVueAffichage
        from Modele.Joueurs import ClassJoueursModel
        # Appel du modèle pour mise à disposition de la liste des joueurs de la base de donnée.
        liste_joueurs = ClassJoueursModel.MisADispoJoueurBddList(self=True)

        # Appel de la méthode vue du modèle VMC
        # pour affichage de la résultante de la base de données
        ClassVueAffichage.Affichage(self=True, texte1="",
                                    texte2="Joueurs de la base de données :",
                                    texte3=liste_joueurs + "\n")
        return ()

    def sup_joueurs(menu_niv_2):
        from Modele.Joueurs import ClassJoueursModel
        ClassJoueursModel.SupJoueur(self=True, numero_joueur=int(menu_niv_2))

    def purge_joueurs():
        from Modele.Joueurs import ClassJoueursModel
        ClassJoueursModel.PurgeBddJoueur()

    def lecture_joueurs_class_nom():
        # Récupération des informations du fichier
        # JSON du tournoi pour créer les rounds
        from Modele.Joueurs import ClassJoueursModel
        from Vue.affichage import ClassVueAffichage
        serie_joueurs = ClassJoueursModel.MisADispoJoueursRapport()
        index = 0
        liste_joueurs = []
        for i in serie_joueurs:
            liste1 = ["ID joueur n°:", int(serie_joueurs[index]['id_joueur']),
                      "nom,", (serie_joueurs[index]['Nom']),
                      "prénom ,", (serie_joueurs[index]['Prenom']),
                      "class:", int(serie_joueurs[index]['Classement'])]
            liste_joueurs.append(liste1)
            index = index + 1

        from operator import itemgetter
        joueur_id_decroissant = (sorted(liste_joueurs, key=itemgetter(3), reverse=False))

        ClassVueAffichage.Affichage(self=True, texte1="Affichage des joueurs par ordre alphabétique de leurs noms :",
                                    texte2="", texte3="")
        index = 0
        for i in joueur_id_decroissant:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=joueur_id_decroissant[index])
            index = index + 1

    def lecture_joueurs_class_id():
        # Récupération des informations du fichier
        # JSON du tournoi pour créer les rounds
        from Modele.Joueurs import ClassJoueursModel
        from Vue.affichage import ClassVueAffichage
        serie_joueurs = ClassJoueursModel.MisADispoJoueursRapport()
        index = 0
        liste_joueurs = []
        for i in serie_joueurs:
            liste1 = ["ID joueur n°:", int(serie_joueurs[index]['id_joueur']),
                      "nom,", (serie_joueurs[index]['Nom']),
                      "prénom ,", (serie_joueurs[index]['Prenom']),
                      "class:", int(serie_joueurs[index]['Classement'])]
            liste_joueurs.append(liste1)
            index = index + 1
        from operator import itemgetter
        joueur_id_decroissant = (sorted(liste_joueurs, key=itemgetter(1), reverse=False))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Affichage des joueurs par ordre "
                                                 "alphabétique de leurs identifiant :")
        index = 0
        for i in joueur_id_decroissant:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=joueur_id_decroissant[index])
            index = index + 1

    def lecture_joueurs_classement():
        # Récupération des informations du fichier
        from Modele.Joueurs import ClassJoueursModel
        from Vue.affichage import ClassVueAffichage
        serie_joueurs = ClassJoueursModel.MisADispoJoueursRapport()
        index = 0
        liste_joueurs = []
        for i in serie_joueurs:
            liste1 = ["ID joueur n°:", int(serie_joueurs[index]['id_joueur']),
                      "nom,", (serie_joueurs[index]['Nom']),
                      "prénom ,", (serie_joueurs[index]['Prenom']),
                      "class:",
                      int(serie_joueurs[index]['Classement'])]
            liste_joueurs.append(liste1)
            index = index + 1

        # tri des joueurs
        from operator import itemgetter
        joueur_class_decr = (sorted(liste_joueurs, key=itemgetter(7), reverse=False))
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="Affichage des joueurs "
                                                            "dans l'ordre de leurs classements :")
        index = 0
        for i in joueur_class_decr:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=joueur_class_decr[index])
            index = index + 1

    def creat_new_class_joueurs():
        import os
        from Vue.affichage import ClassVueAffichage
        from Modele.Joueurs import ClassJoueursModel

        # Appel de la méthode model de mise à disposition de la liste des joueurs à partir de la bdd
        liste_joueurs = ClassJoueursModel.LectListeListeJoueursBdd()
        ClassVueAffichage.Affichage(self=True, texte1="liste joueurs", texte2=liste_joueurs, texte3="")

        # Tri de la liste des joueurs
        from operator import itemgetter
        joueur_class_decr = (sorted(liste_joueurs, key=itemgetter(7), reverse=False))
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="Affichage des joueurs dans "
                                                            "l'ordre de leurs classements :")
        index = 0
        for i in joueur_class_decr:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=joueur_class_decr[index])
            index = index + 1
        index = 0

        for i in liste_joueurs:
            # Appel de la méthode model de mise à disposition du joueur à classer à partir de l'index de la boucle
            joueur_a_classer = ClassJoueursModel.MiseADispoJourAClasser(self=True, index=index)

        # Appel de la méthode input de la vue pour saisie du nouveau classment du joueur
            saisie_new_cl = ClassVueAffichage. \
                Input(self=True, texte1="Saisie nouveau classement joueur n°" + joueur_a_classer)

            if saisie_new_cl == "E":
                break
                os._exit(0)

            if saisie_new_cl.isdigit():
                new_classement = saisie_new_cl
                identifiant_joueur = int(joueur_a_classer)

                # Appel du modèle pour mise à jour du classement du joueur
                ClassJoueursModel.UpdateClassJoueurs(self=True,
                                                     nom_donnees="Classement",
                                                     donnees=new_classement,
                                                     numero_joueur=identifiant_joueur)
            else:
                ClassVueAffichage.Affichage1Ligne(self=True, texte1="pas de modification de classement pour ce joueur")
            index = index + 1
