class Class_Match():
    def __init__(self):
        pass

    def creat_match():
        import os
        from tinydb import TinyDB, where
        from Controleur.fonctions import ClassFonctions
        from Vue.affichage import ClassVueAffichage
        # from Controleur.Ctrl_Tournoi import select_tournoi
        db_tournois = TinyDB('tournois.json')
        print("saisie des scores du match")
        tournoi_select = ClassFonctions.select_tournoi()
        int_tournoi_select = int(tournoi_select)
        print("int_tournoi_select : " + str(int_tournoi_select))
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        # print("tournoi" + str(tournoi))
        id_t = (tournoi[0]['id_tournoi'])
        try:
            round_en_cours = (tournoi[0]['round_en_cours'])
            ClassVueAffichage.Affichage(self=True,
                                        texte1="round en cours :",
                                        texte2=round_en_cours,
                                        texte3="")
            print("round_en_cours : " + str(round_en_cours))
        except KeyError:
            ClassVueAffichage.Affichage(self=True,
                                        texte1="Le round doit être créé "
                                               "dans le match pour que les "
                                               "scores du match puissent être "
                                               "saisis, - R suivi de + - pour "
                                               "créer le 1er round",
                                        texte2="",
                                        texte3="")
            print(
                "Le round doit être créé dans le match pour "
                "que les scores du match puissent être saisis, "
                "- R suivi de + - pour créer le 1er round")
            os._exit(0)

        tournoi = id_t
        round = round_en_cours
        if round_en_cours == 1:
            Class_Match.creat_match_r1(tournoi, round)
        else:
            Class_Match.creat_match_r2(tournoi, round)

    def creat_match_r1(tournoi, round):
        import os
        from Vue.affichage import ClassVueAffichage
        from Modele.Tournoi import ClassTournoi
        import datetime
        ClassVueAffichage.Affichage(self=True,
                                    texte1="tournoi r1 : ",
                                    texte2=tournoi,
                                    texte3="")
        ClassVueAffichage.Affichage(self=True,
                                    texte1="round r1 : ",
                                    texte2=round,
                                    texte3="")
        ClassVueAffichage.Affichage(self=True,
                                    texte1="saisie des scores du match",
                                    texte2="",
                                    texte3="")
        # faire un input pour indiquer le tournoi à sélectionner

        # Vérifier que la saisie du numero du tournoi est correcte
        # charger le tournoi selectionné à partir de
        # la base de données dans tournoi
        # tournoi_select = select_tournoi()


        # Appel du modèle pour mise à disposition des données du tournoi

        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        int_tournoi_select = tournoi
        tournoi_select = tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

        print(tournoi)

        # Récupération des informations du fichier
        # JSON du tournoi pour vérifier le round en cours



        try:
            round_en_cours = (tournoi[0]['round_en_cours'])
            ClassVueAffichage.Affichage(self=True,
                                        texte1="round_en_cours : ",
                                        texte2=round_en_cours,
                                        texte3="")
        except KeyError:
            ClassVueAffichage.Affichage(self=True,
                                        texte1="Le round doit être créé dans "
                                               "le match pour que les scores "
                                               "du match puissent être saisis"
                                               ", - R suivi de + - "
                                               "pour créer le 1er round",
                                        texte2="",
                                        texte3="")
            os._exit(0)

        List_de_liste_joueur = (tournoi[0]['round_en_cours'])
        round_select = "round_" + str(round_en_cours) + "+match"

        # aller chercher les listes en fonction du round en cours
        List_de_liste_joueur = (tournoi[0][round_select])
        print("paire 1")
        print(List_de_liste_joueur[1])
        print()
        print("paire 2")
        print(List_de_liste_joueur[2])
        print()
        print("paire 3")
        print(List_de_liste_joueur[3])
        print()
        print("paire 4")
        print(List_de_liste_joueur[4])

        # Saisie des scores de la paire 1
        str_liste_liste_joueur1 = str(List_de_liste_joueur[1][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[1][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 1er Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 1er Match"
        saisie_score1, saisie_score2 = ClassVueAffichage.SaisieScore(
            self,
            str_liste_liste_joueur1,
            str_liste_liste_joueur2,
            texteJ1,
            texteJ2)
        ClassVueAffichage.Affichage(self=True,
                                    texte1="saisie score 1 et 2 du match 1:",
                                    texte2=saisie_score1,
                                    texte3=saisie_score2)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire1_j1 = []
        print(List_de_liste_joueur)
        print(List_de_liste_joueur[1][0])
        liste_paire1_j1.append(List_de_liste_joueur[1][0][0])
        liste_paire1_j1.append(saisie_score1)
        print(liste_paire1_j1)
        # joueur 2
        liste_paire1_j2 = []
        liste_paire1_j2.append(List_de_liste_joueur[1][1][0])
        liste_paire1_j2.append(saisie_score2)
        print(liste_paire1_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple1 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_" + \
                     "Match" + "1"
        globals()[nom_tuple1] = ((liste_paire1_j1[0],
                                  liste_paire1_j1[1],
                                  liste_paire1_j2[0],
                                  liste_paire1_j2[1]))

        # Saisie des scores de la paire 2
        str_liste_liste_joueur1 = str(List_de_liste_joueur[2][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[2][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 2ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 2ème Match"
        saisie_score3, saisie_score4 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2,
                                                                     texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 2: ' + (saisie_score3) + " - " + saisie_score4)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire2_j1 = []
        liste_paire2_j1.append(List_de_liste_joueur[2][0][0])
        liste_paire2_j1.append(saisie_score3)
        print(liste_paire2_j1)
        # joueur 2
        liste_paire2_j2 = []
        liste_paire2_j2.append(List_de_liste_joueur[2][1][0])
        liste_paire2_j2.append(saisie_score4)
        print(liste_paire2_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple2 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_" + \
                     "Match" + "2"

        globals()[nom_tuple2] = ((liste_paire2_j1[0],
                                  liste_paire2_j1[1],
                                  liste_paire2_j2[0],
                                  liste_paire2_j2[1]))

        # Saisie des scores de la paire 3
        str_liste_liste_joueur1 = str(List_de_liste_joueur[3][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[3][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 3ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 3ème Match"
        saisie_score5, saisie_score6 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2,
                                                                     texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire3_j1 = []
        liste_paire3_j1.append(List_de_liste_joueur[3][0][0])
        liste_paire3_j1.append(saisie_score5)
        print(liste_paire3_j1)
        # joueur 2
        liste_paire3_j2 = []
        liste_paire3_j2.append(List_de_liste_joueur[3][1][0])
        liste_paire3_j2.append(saisie_score6)
        print(liste_paire3_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple3 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_"  \
                     + "Match" + "3"

        globals()[nom_tuple3] = ((liste_paire3_j1[0],
                                  liste_paire3_j1[1],
                                  liste_paire3_j2[0],
                                  liste_paire3_j2[1]))

        # Saisie des scores de la paire 4
        str_liste_liste_joueur1 = str(List_de_liste_joueur[4][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[4][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 4ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 4ème Match"
        saisie_score7, saisie_score8 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2,
                                                                     texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 4: ' + (saisie_score7) + " - " + saisie_score8)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire4_j1 = []
        liste_paire4_j1.append(List_de_liste_joueur[4][0][0])
        liste_paire4_j1.append(saisie_score7)
        print(liste_paire4_j1)
        # joueur 2
        liste_paire4_j2 = []
        liste_paire4_j2.append(List_de_liste_joueur[4][1][0])
        liste_paire4_j2.append(saisie_score8)
        print(liste_paire4_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple4 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_" + \
                     "Match" + "4"

        globals()[nom_tuple4] = ((liste_paire4_j1[0],
                                  liste_paire4_j1[1],
                                  liste_paire4_j2[0],
                                  liste_paire4_j2[1]))

        from tinydb import TinyDB, Query, where
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)
        print(round_select)

        # préparation pour mise dans la base de donnée
        liste_match1 = []
        liste_match1.append(globals()[nom_tuple1])

        liste_match2 = []
        liste_match2.append(globals()[nom_tuple2])

        liste_match3 = []
        liste_match3.append(globals()[nom_tuple3])

        liste_match4 = []
        liste_match4.append(globals()[nom_tuple4])

        liste_4matchs = []
        liste_4matchs.append(liste_match1)
        liste_4matchs.append(liste_match2)
        liste_4matchs.append(liste_match3)
        liste_4matchs.append(liste_match4)

        # mise de l'heure de fin du match pour la mettre dans
        # la base de donnée du tournoi
        date_heure_fin = datetime.datetime.now()
        str_date_heure_fin = str(date_heure_fin)
        char = '.'
        PositChar = str_date_heure_fin.find(char)
        str_date_heure_fin = str_date_heure_fin[0:(PositChar)]
        print("fin round en cours " + str(round_en_cours) + " : " + str_date_heure_fin)

        # chargment dans la base de données de
        # la fin de match du round en cours
        nom_donne_fin_match = ("fin round " + str(round_en_cours))
        donne_fin_match = str_date_heure_fin
        db_tournois.update({nom_donne_fin_match: donne_fin_match},
                           Todo.id_tournoi == int_tournoi_select)

        # chargement dans la base de données des scores des 4 matchs du round
        nom_donnees = "ScoreMatchRound" + str(round_en_cours)
        # print(nom_donnees)

        liste_4matchs = []
        liste_4matchs.append(liste_paire1_j1)
        liste_4matchs.append(liste_paire1_j2)
        liste_4matchs.append(liste_paire2_j1)
        liste_4matchs.append(liste_paire2_j2)
        liste_4matchs.append(liste_paire3_j1)
        liste_4matchs.append(liste_paire3_j2)
        liste_4matchs.append(liste_paire4_j1)
        liste_4matchs.append(liste_paire4_j2)
        # Appel du modele pour updater les donnees des matchs
        # dans la base de donnée
        ClassTournoi.UpdateMatchTournois(self=True,
                                         nom_donnees=nom_donnees,
                                         donnees=liste_4matchs,
                                         numero_tournoi=int_tournoi_select)

    def creat_match_r2(tournoi, round):
        import datetime
        import os
        from Vue.affichage import ClassVueAffichage
        from tinydb import TinyDB, Query, where
        print("tournoi r1 : " + str(tournoi))
        print("round r1 : " + str(round))
        print()
        print("saisie des scores du match")

        # Vérifier que la saisie du numero du tournoi est correcte
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        int_tournoi_select = tournoi
        tournoi_select = tournoi
        print("int_tournoi_select")
        print(int_tournoi_select)

        # va chercher l'id du tournoi dans la base de donnée
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        # Récupération des informations du fichier JSON
        # du tournoi pour vérifier le round en cours
        id_t = (tournoi[0]['id_tournoi'])
        print("id tournoi : " + str(id_t))

        try:
            round_en_cours = (tournoi[0]['round_en_cours'])
            print("round_en_cours : " + str(round_en_cours))

        except KeyError:
            print("Le round doit être créé")
            print("Le round doit être créé dans le match pour que les scores "
                  "du match puissent être saisis, "
                  "- R suivi de + - pour créer le 1er round")
            os._exit(0)

        List_de_liste_joueur = (tournoi[0]['round_en_cours'])
        round_select = "round_" + str(round_en_cours) + "+match"
        print(round_select)

        # aller chercher les listes en fonction du round en cours
        List_de_liste_joueur = (tournoi[0][round_select])

        print("List_de_liste_joueur")
        print(List_de_liste_joueur)
        print()
        print("paire 1")
        print(List_de_liste_joueur[1])
        print()
        print("paire 2")
        print(List_de_liste_joueur[2])
        print()
        print("paire 3")
        print(List_de_liste_joueur[3])
        print()
        print("paire 4")
        print(List_de_liste_joueur[4])

        # Saisie des scores de la paire 1
        str_liste_liste_joueur1 = str(List_de_liste_joueur[1][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[1][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 1er Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 1er Match"
        saisie_score1, saisie_score2 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2,
                                                                     texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 1: ' + (saisie_score1) + " - " + saisie_score2)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire1_j1 = []
        liste_paire1_j2 = []
        print("List_de_liste_joueur")
        print(List_de_liste_joueur)
        print("List_de_liste_joueur[1][0]")
        print(List_de_liste_joueur[1][0])
        liste_paire1_j1.append(List_de_liste_joueur[1][0])
        liste_paire1_j1.append(saisie_score1)

        print(liste_paire1_j1)
        print(liste_paire1_j2)
        # joueur 2
        liste_paire1_j2 = []
        liste_paire1_j2.append(List_de_liste_joueur[1][1])
        liste_paire1_j2.append(saisie_score2)
        print(liste_paire1_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple1 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_" + \
                     "Match" + "1"
        globals()[nom_tuple1] = ((liste_paire1_j1[0],
                                  liste_paire1_j1[1],
                                  liste_paire1_j2[0],
                                  liste_paire1_j2[1]))

        # Saisie des scores de la paire 2
        str_liste_liste_joueur1 = str(List_de_liste_joueur[2][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[2][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 2ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 2ème Match"
        saisie_score3, saisie_score4 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2,
                                                                     texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 2: ' + (saisie_score3) + " - " + saisie_score4)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire2_j1 = []
        liste_paire2_j1.append(List_de_liste_joueur[2][0])
        liste_paire2_j1.append(saisie_score3)
        print(liste_paire2_j1)
        # joueur 2
        liste_paire2_j2 = []
        liste_paire2_j2.append(List_de_liste_joueur[2][1])
        liste_paire2_j2.append(saisie_score4)
        print(liste_paire2_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple2 = "IdTournoi" + str(tournoi_select) + "_" + "Round" + str(round_en_cours) + "_" + \
                     "Match" + "2"

        globals()[nom_tuple2] = ((liste_paire2_j1[0],
                                  liste_paire2_j1[1],
                                  liste_paire2_j2[0],
                                  liste_paire2_j2[1]))

        # Saisie des scores de la paire 3
        str_liste_liste_j1 = str(List_de_liste_joueur[3][0])
        str_liste_liste_j2 = str(List_de_liste_joueur[3][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 3ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 3ème Match"
        saisie_score5, saisie_score6 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_j1,
                                                                     str_liste_liste_j2,
                                                                     texteJ1,
                                                                     texteJ2)
        print('saisie score 1 et 2 du match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire3_j1 = []
        liste_paire3_j1.append(List_de_liste_joueur[3][0])
        liste_paire3_j1.append(saisie_score5)
        print(liste_paire3_j1)
        # joueur 2
        liste_paire3_j2 = []
        liste_paire3_j2.append(List_de_liste_joueur[3][1])
        liste_paire3_j2.append(saisie_score6)
        print(liste_paire3_j2)

        # Chaque match génèrera 1 tuple avec comme nom, « Tuple_
        # « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple3 = "IdTournoi" + str(tournoi_select) + "_" \
                     + "Round" + str(round_en_cours) + "_" + \
                     "Match" + "3"
        globals()[nom_tuple3] = ((liste_paire3_j1[0],
                                  liste_paire3_j1[1],
                                  liste_paire3_j2[0],
                                  liste_paire3_j2[1]))

        # Saisie des scores de la paire 4
        str_liste_liste_j1 = str(List_de_liste_joueur[4][0])
        str_liste_liste_j2 = str(List_de_liste_joueur[4][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 4ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 4ème Match"

        saisie_score7, saisie_score8 = ClassVueAffichage.SaisieScore(self,
                                                                     str_liste_liste_j1,
                                                                     str_liste_liste_j2,
                                                                     texteJ1, texteJ2)

        print('saisie score 1 et 2 du match 4: ' + (saisie_score7) + " - " + saisie_score8)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire4_j1 = []
        liste_paire4_j1.append(List_de_liste_joueur[4][0])
        liste_paire4_j1.append(saisie_score7)
        print(liste_paire4_j1)

        # joueur 2
        liste_paire4_j2 = []
        liste_paire4_j2.append(List_de_liste_joueur[4][1])
        liste_paire4_j2.append(saisie_score8)
        print(liste_paire4_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple4 = "IdTournoi" + str(tournoi_select) + "_" + "Round" + str(round_en_cours) + "_" + "Match" + "4"

        globals()[nom_tuple4] = ((liste_paire4_j1[0],
                                  liste_paire4_j1[1],
                                  liste_paire4_j2[0],
                                  liste_paire4_j2[1]))

        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        print()
        # print("numéro de tournoi")
        # print(int_tournoi_select)
        # print(round_select)

        # préparation  pour mise dans la base de donnée
        # joueur 1
        # print(List_de_liste_joueur[1])
        liste_match1 = []
        liste_match1.append(globals()[nom_tuple1])
        # print("liste_match1")
        # print(liste_match1)

        # joueur 2
        # print(List_de_liste_joueur[2])
        liste_match2 = []
        liste_match2.append(globals()[nom_tuple2])
        # print("liste_match2")
        # print(liste_match2)

        # joueur 3
        # print(List_de_liste_joueur[3])
        liste_match3 = []
        liste_match3.append(globals()[nom_tuple3])
        # print("liste_match3")
        # print(liste_match3)

        # joueur 4
        # print(List_de_liste_joueur[4])
        liste_match4 = []
        liste_match4.append(globals()[nom_tuple4])
        # print("liste_match4")
        # print(liste_match4)

        liste_4matchs = []
        liste_4matchs.append(liste_match1)
        liste_4matchs.append(liste_match2)
        liste_4matchs.append(liste_match3)
        liste_4matchs.append(liste_match4)

        # print("liste_4matchs.append(liste_match4)")
        # print(liste_4matchs)

        # print(liste_4matchs[0])
        # print(liste_4matchs[0][0][0])
        # print(liste_4matchs[0][0][1])
        # print(liste_4matchs[0][0][2])
        # print(liste_4matchs[0][0][3])

        # print(liste_4matchs[1])
        # print(liste_4matchs[1][0])
        # print(liste_4matchs[1][0][0])
        # print(liste_4matchs[1][0][1])
        # print(liste_4matchs[1][0][2])
        # print(liste_4matchs[1][0][3])

        # print(liste_4matchs[2])
        # print(liste_4matchs[2][0])
        # print(liste_4matchs[2][0][0])
        # print(liste_4matchs[2][0][1])
        # print(liste_4matchs[2][0][2])
        # print(liste_4matchs[2][0][3])

        # print(liste_4matchs[3])
        # print(liste_4matchs[3][0])
        # print(liste_4matchs[3][0][0])
        # print(liste_4matchs[3][0][1])
        # print(liste_4matchs[3][0][2])
        # print(liste_4matchs[3][0][3])

        # mise de l'heure de fin du match
        # pour la mettre dans la base de donnée du tournoi
        date_heure_fin = datetime.datetime.now()
        str_date_heure_fin = str(date_heure_fin)
        char = '.'
        PositChar = str_date_heure_fin.find(char)
        str_date_heure_fin = str_date_heure_fin[0:(PositChar)]
        print("fin round en cours " + str(round_en_cours) + " : " + str_date_heure_fin)

        # chargement dans la base de données
        # de la fin de match du round en cours
        nom_donne_fin_match = ("fin round " + str(round_en_cours))
        donne_fin_match = str_date_heure_fin
        db_tournois.update({nom_donne_fin_match: donne_fin_match},
                           Todo.id_tournoi == int_tournoi_select)

        # chargment dans la base de données des scores des 4 matchs du round
        nom_donnees = "ScoreMatchRound" + str(round_en_cours)
        # print(nom_donnees)

        liste_4matchs = []
        liste_4matchs.append(liste_paire1_j1)
        liste_4matchs.append(liste_paire1_j2)
        liste_4matchs.append(liste_paire2_j1)
        liste_4matchs.append(liste_paire2_j2)
        liste_4matchs.append(liste_paire3_j1)
        liste_4matchs.append(liste_paire3_j2)
        liste_4matchs.append(liste_paire4_j1)
        liste_4matchs.append(liste_paire4_j2)

        db_tournois.update({nom_donnees: liste_4matchs},
                           Todo.id_tournoi == int_tournoi_select)
        print()
