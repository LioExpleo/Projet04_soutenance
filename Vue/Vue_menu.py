import os


class ClassVueMenu():
    def Action_menu(self):
        from Controleur.Ctrl_Joueurs import ClassJoueurs
        from Controleur.Ctrl_Tournoi import Class_Tournoi
        from Controleur.Ctrl_Round import Class_Round
        from Controleur.Ctrl_Match import Class_Match
        menu_niv_0 = ""
        menu_niv_1 = ""
        menu_niv_2 = ""

        # Boucle / Menu.
        while (True):
            id_tournoi, \
                saisie_clavier, \
                menu_niv_0, \
                menu_niv_1, \
                menu_niv_2 = ClassMainMenu(id_tournoi="",
                                           clavier="",
                                           niv0=menu_niv_0,
                                           niv1=menu_niv_1,
                                           niv2=menu_niv_2).CommandeClavier()

            if (menu_niv_0 == "J" and menu_niv_1 == "w" and saisie_clavier == "w"):
                ClassJoueurs.creat_new_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "r" and saisie_clavier == "r"):
                ClassJoueurs.lect_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                ClassJoueurs.sup_joueurs(menu_niv_2)

            if (menu_niv_0 == "J" and menu_niv_1 == "purge"):
                ClassJoueurs.purge_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "class"):
                ClassJoueurs.creat_new_class_joueurs()

            if (menu_niv_0 == "T" and menu_niv_1 == "w" and saisie_clavier == "w"):
                Class_Tournoi.creat_new_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "r" and saisie_clavier == "r"):
                Class_Tournoi.lect_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                Class_Tournoi.sup_tournois(menu_niv_2)

            if (menu_niv_0 == "T" and menu_niv_1 == "purge"):
                Class_Tournoi.purge_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "c" and saisie_clavier == "c"):
                Class_Tournoi.charge_joueurs_tournoi()

            if (menu_niv_0 == "R" and menu_niv_1 == "+" and saisie_clavier == "+"):
                print("Cr??ation d'un round selon le syst??me suisse ")
                Class_Round.creat_round()

            if (menu_niv_0 == "M" and menu_niv_1 == "w"):
                Class_Match.creat_match()

            if (menu_niv_0 == "JCN"):
                ClassJoueurs.lecture_joueurs_class_nom()

            if (menu_niv_0 == "JCC"):
                ClassJoueurs.lecture_joueurs_classement()

            if (menu_niv_0 == "JCI"):
                ClassJoueurs.lecture_joueurs_class_id()

            if (menu_niv_0 == "TJ"):
                Class_Tournoi.lecture_joueur_tournoi_class()

            if (menu_niv_0 == "TR"):
                print("Saisir ensuite l'id du tournoi, s'afficheront "
                      "tous les rounds")
                Class_Tournoi.lecture_round_tournoi()

            if (menu_niv_0 == "TM"):
                print("Saisir ensuite l'id du tournoi, s'afficheront "
                      "tous les rounds - ID Joueur, numero round, et score")
                Class_Tournoi.lecture_match_tournoi()

            if (menu_niv_0 == "TT"):
                print()
                print("Affichage de la liste simplifi??e des "
                      "tournois avec ID, nom, lieu et date")
                Class_Tournoi.lecturetournoi()


class ClassMainMenu():
    def __init__(self, id_tournoi, clavier, niv0, niv1, niv2):
        self.clavier = clavier
        self.niv0 = niv0
        self.niv1 = niv1
        self.niv2 = niv2
        self.id_tournoi = id_tournoi

    def CommandeClavier(self):
        clavier = ""
        menu_niv0 = self.niv0
        menu_niv1 = self.niv1
        menu_niv2 = self.niv2
        id_tournoi = self.id_tournoi

        # *** Exit prog ***
        while (clavier != "E"):
            clavier = input("Entrez une commande valide help pour aide ")
            if (clavier != "") and (clavier != "E"):
                if (clavier == "help"):
                    print("1 pour ..., 2 pour..., 3 pour ...")

                # *** MENU TOURNOI ***
                if (clavier == "T"):
                    menu_niv0 = clavier
                    menu_niv1 = ""
                    menu_niv2 = ""
                    print("TOURNOI : ")
                    print("r pour afficher la liste des tournois - "
                          "w pour cr??er un nouveau tournoi, "
                          "c pour charger les joueurs dans "
                          "un tournoi existant")

                # cr??ation d'un tournoi
                if (menu_niv0 == "T" and clavier == "w"):
                    menu_niv0 = "T"
                    menu_niv1 = clavier
                    print("cr??ation de l'instance de classe pour "
                          "cr??ation du tournoi")
                    # Echange avec le contr??leur qui cr???? l'instance
                    # de tournoi ?? partir du mod??le
                    print("Nom, lieu, date mise en auto, "
                          "date de fin mise en auto")

                # affichage se tous les tournois
                if (menu_niv0 == "T" and clavier == "r"):
                    menu_niv1 = clavier
                    print("requ??te pour afficher la liste des tournois")

                # purge de la table des tournois, utile pour debug
                if (menu_niv0 == "T" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donn??e "
                          "des tournois tapez :\"o\" pour confirmer")
                if (menu_niv0 == "T" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier

                # effacement d'un joueur de la liste si erreur de saisie
                if (menu_niv0 == "T" and clavier == "sup"):
                    menu_niv1 = clavier
                    print(
                        "vous voulez supprimer un tournoi, suite ?? une "
                        "erreur de saisie par exemple, de la liste des "
                        "tournois, tapez l'identifiant du tournoi "
                        "pour le supprimer !")
                # suppression d'un tournoi
                if (menu_niv0 == "T" and menu_niv1 == "sup" and clavier != "sup"):
                    menu_niv2 = clavier

                # s??lectionner du tournoi et chargement des joueurs
                # dans le tournoi
                if (menu_niv0 == "T" and clavier == "c"):
                    menu_niv1 = clavier
                    print("chargement du tournoi avec son id")

                # *** MENU JOUEURS ****
                if (clavier == "J"):
                    menu_niv0 = clavier
                    menu_niv1 = ""
                    menu_niv2 = ""
                    print("JOUEURS : ")
                    print("Vous avez entr?? " + clavier + " pour JOUEURS: r pour lecture, "
                          "w pour cr??ation de joueurs, c pour charger dans un tournoi, "
                          "class pour modifier le classement")

                # cr??ation de la liste des joueurs
                if (menu_niv0 == "J" and clavier == "w"):
                    menu_niv1 = clavier
                    print("cr??ation de la liste des joueurs, "
                          "nom, pr??nom, date de naissance, sexe, classement")

                # affichage la liste des joueurs pour les s??lectionner
                # ensuite dans le tournoi
                if (menu_niv0 == "J" and clavier == "r"):
                    menu_niv1 = clavier

                # purge de la table des joueurs, utile pour debug
                if (menu_niv0 == "J" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donn??e "
                          "des joueurs tapez :\"o\" pour confirmer")
                if (menu_niv0 == "J" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier

                # effacement un joueur de la liste si erreur de saisie
                if (menu_niv0 == "J" and clavier == "sup"):
                    menu_niv1 = clavier
                    print("vous voulez supprimer un joueur, "
                          "suite ?? une erreur de saisie par exemple, "
                          "de la liste des joueurs, tapez l'id du "
                          "joueur ?? supprimer !")

                if (menu_niv0 == "J" and menu_niv1 == "sup" and clavier != "sup"):
                    menu_niv2 = clavier

                # Modification du classment des joueurs
                if (menu_niv0 == "J" and clavier == "class"):
                    menu_niv1 = clavier
                    print("vous voulez modifier le classment de joueur, "
                          "dans la liste des joueurs, en 1er lieu, "
                          "visualisation du classement")

                # *** MENU ROUND ****
                if (clavier == "R"):
                    print(" Touche + pour cr??er un nouveau round")
                    menu_niv0 = clavier
                    menu_niv1 = ""
                    menu_niv2 = ""

                if (menu_niv0 == "R" and clavier == "+"):
                    menu_niv1 = clavier  # ; menu_niv2: ""
                    print(" Cr??ation d'un nouveau round :" + clavier + " S??lectionner "
                                                                       "le tournoi o?? les 8 "
                                                                       "joueurs ont ??t?? saisis")

                if (menu_niv0 == "R" and menu_niv0 == "+" and clavier != "+"):
                    menu_niv1 = clavier

                    # MENU MATCH
                if (clavier == "M"):
                    menu_niv0 = clavier
                    menu_niv1 = ""
                    menu_niv2 = ""
                    print(" Vous avez entr?? :" + clavier + " MATCH : r pour lecture, "
                                                           "w pour ??criture; "
                                                           "si ??criture, le round pr??c??dant "
                                                           "se termine et la saisie des scores "
                                                           "est ?? faire par paire")

                    # chronologiquement, la personne qui saisi doit repasser
                    # au 4 pour refaire des round, peut aussi se faire
                    # automatiquement"

                    # si round 4, fin tournoi, mise ?? jour manuelle du
                    # classement des joueurs"
                    # cr??ation de la liste des joueurs
                if (menu_niv0 == "M" and clavier == "w"):
                    menu_niv1 = clavier
                    print("cr??ation du match")

                # MENU REQUETES EN DEHORS DU TOURNOI

                if (clavier == "JCN"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE AFFICHAGE DE TOUS "
                                                           "LES ACTEURS PAR ORDRE ALPHABETIQUE")

                if (clavier == "JCC"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE  AFFICHAGE DE TOUS"
                                                           " LES ACTEURS PAR ORDRE DE CLASSEMENT")

                if (clavier == "JCI"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE  AFFICHAGE "
                                                           "DE TOUS LES ACTEURS PAR ORDRE "
                                                           "DE CLASSEMENT")

                if (clavier == "TJ"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE AFFICHAGE "
                                                           "DE TOUS LES JOUEURS D'UN TOURNOI"
                                                           " - ENTREZ L'ID DU TOURNOI")

                if (clavier == "TR"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE FFICHAGE DE TOUS "
                                                           "LES ROUNDS D'UN TOURNOI")

                if (clavier == "TM"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE AFFICHAGE DE TOUS "
                                                           "LES MATCHS D'UN TOURNOI")

                if (clavier == "TT"):
                    menu_niv0 = clavier
                    print(" Vous avez entr?? :" + clavier + " REQUETE AFFICHAGE DE "
                                                           "LA LISTE DES TOURNOIS")

                if (clavier != 0):
                    # print(clavier)
                    return (id_tournoi, clavier, menu_niv0,
                            menu_niv1, menu_niv2)
        else:
            print("os._exit(0)")
            os._exit(0)

        print("self.clavier")
        return (id_tournoi, clavier, menu_niv0, menu_niv1, menu_niv2)
