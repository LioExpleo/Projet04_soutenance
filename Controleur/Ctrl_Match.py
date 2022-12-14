class Class_Match():
    def __init__(self):
        pass

    def creat_match():
        import os
        from Controleur.fonctions import ClassFonctions
        from Vue.affichage import ClassVueAffichage
        from Modele.Tournoi import ClassModTournoi

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="saisie des scores du match")
        tournoi_select = ClassFonctions.select_tournoi()
        int_tournoi_select = int(tournoi_select)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="int_tournoi_select : " + str(int_tournoi_select))

        # Appel du modele pour mise a disposition données tournoi
        db_tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int_tournoi_select)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="tournoi" + str(db_tournoi))

        id_t = (db_tournoi[0]['id_tournoi'])
        try:
            round_en_cours = (db_tournoi[0]['round_en_cours'])
            ClassVueAffichage.Affichage(self=True,
                                        texte1="round en cours :",
                                        texte2=round_en_cours,
                                        texte3="")
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="round_en_cours : " + str(round_en_cours))
        except KeyError:
            ClassVueAffichage.Affichage(self=True,
                                        texte1="Le round doit être créé "
                                               "dans le match pour que les "
                                               "scores du match puissent être "
                                               "saisis, - R suivi de + - pour "
                                               "créer le 1er round",
                                        texte2="",
                                        texte3="")
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="Le round doit être créé dans le match pour que les"
                                                                " scores du match puissent être saisis, "
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
        from Modele.Tournoi import ClassModTournoi
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

        int_tournoi_select = tournoi
        tournoi_select = tournoi
        # Appel du modele pour creation liste tournoi
        db_tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int(tournoi_select))
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=db_tournoi)
        try:
            round_en_cours = (db_tournoi[0]['round_en_cours'])
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

        List_de_liste_joueur = (db_tournoi[0]['round_en_cours'])
        round_select = "round_" + str(round_en_cours) + "+match"

        # aller chercher les listes en fonction du round en cours
        List_de_liste_joueur = (db_tournoi[0][round_select])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 1")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[1])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 2")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[2])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 3")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[3])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 4")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[4])

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
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[1][0])
        liste_paire1_j1.append(List_de_liste_joueur[1][0][0])
        liste_paire1_j1.append(saisie_score1)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire1_j1)
        # joueur 2
        liste_paire1_j2 = []
        liste_paire1_j2.append(List_de_liste_joueur[1][1][0])
        liste_paire1_j2.append(saisie_score2)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire1_j2)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 2: ' + (saisie_score3) + " - " + saisie_score4)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire2_j1 = []
        liste_paire2_j1.append(List_de_liste_joueur[2][0][0])
        liste_paire2_j1.append(saisie_score3)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire2_j1)
        # joueur 2
        liste_paire2_j2 = []
        liste_paire2_j2.append(List_de_liste_joueur[2][1][0])
        liste_paire2_j2.append(saisie_score4)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire2_j2)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire3_j1 = []
        liste_paire3_j1.append(List_de_liste_joueur[3][0][0])
        liste_paire3_j1.append(saisie_score5)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire3_j1)
        # joueur 2
        liste_paire3_j2 = []
        liste_paire3_j2.append(List_de_liste_joueur[3][1][0])
        liste_paire3_j2.append(saisie_score6)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire3_j2)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du match '
                                                 '4: ' + (saisie_score7) + " - " + saisie_score8)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire4_j1 = []
        liste_paire4_j1.append(List_de_liste_joueur[4][0][0])
        liste_paire4_j1.append(saisie_score7)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire4_j1)
        # joueur 2
        liste_paire4_j2 = []
        liste_paire4_j2.append(List_de_liste_joueur[4][1][0])
        liste_paire4_j2.append(saisie_score8)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire4_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple4 = "IdTournoi" + str(tournoi_select) + "_" + \
                     "Round" + str(round_en_cours) + "_" + \
                     "Match" + "4"

        globals()[nom_tuple4] = ((liste_paire4_j1[0],
                                  liste_paire4_j1[1],
                                  liste_paire4_j2[0],
                                  liste_paire4_j2[1]))

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="numéro de tournoi")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=int_tournoi_select)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=round_select)

        # préparation pour mise dans la base de donnée
        liste_match1 = []
        liste_match1.append(globals()[nom_tuple1])

        liste_match2 = []
        liste_match2.append(globals()[nom_tuple2])

        liste_match3 = []
        liste_match3.append(globals()[nom_tuple3])

        liste_match4 = []
        liste_match4.append(globals()[nom_tuple4])

        # création des tuples
        tupl1 = (liste_paire1_j1, liste_paire1_j2)
        tupl2 = (liste_paire2_j1, liste_paire2_j2)
        tupl3 = (liste_paire3_j1, liste_paire3_j2)
        tupl4 = (liste_paire4_j1, liste_paire4_j2)

        from Modele.Match import ClassMatch
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=1, tuple_match=tupl1)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=2, tuple_match=tupl2)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=3, tuple_match=tupl3)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=4, tuple_match=tupl4)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="fin round en "
                                                 "cours " + str(round_en_cours) + " : " + str_date_heure_fin)

        # chargment dans la base de données de
        # la fin de match du round en cours

        # chargement dans la base de données des scores des 4 matchs du round
        nom_donnees = "ScoreMatchRound" + str(round_en_cours)

        liste_4matchs = []
        liste_4matchs.append(liste_paire1_j1)
        liste_4matchs.append(liste_paire1_j2)
        liste_4matchs.append(liste_paire2_j1)
        liste_4matchs.append(liste_paire2_j2)
        liste_4matchs.append(liste_paire3_j1)
        liste_4matchs.append(liste_paire3_j2)
        liste_4matchs.append(liste_paire4_j1)
        liste_4matchs.append(liste_paire4_j2)

        # Appel Modele Tournoi pour enregistrement des donnees dans la base de donnees
        ClassModTournoi.UpdateDonneesTournoi(self=True, numero_tournoi=int_tournoi_select,
                                             nom_donnee=nom_donnees, donnee=liste_4matchs)

    def creat_match_r2(tournoi, round):
        import datetime
        import os
        from Vue.affichage import ClassVueAffichage
        from Modele.Tournoi import ClassModTournoi
        tournoi_select = tournoi

        # Appel du modele pour mise a disposition données tournoi
        db_tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int(tournoi_select))
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=db_tournoi)

        # Récupération des informations du fichier JSON
        # du tournoi pour vérifier le round en cours
        id_t = (db_tournoi[0]['id_tournoi'])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="id tournoi : " + str(id_t))

        try:
            round_en_cours = (db_tournoi[0]['round_en_cours'])
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="round_en_cours : " + str(round_en_cours))

        except KeyError:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="Le round doit être créé")
            ClassVueAffichage.Affichage1Ligne(self=True,
                                              texte1="Le round doit être créé dans le match pour que les scores "
                                                     "du match puissent être saisis, "
                                                     "- R suivi de + - pour créer le 1er round")
            os._exit(0)

        List_de_liste_joueur = (db_tournoi[0]['round_en_cours'])
        round_select = "round_" + str(round_en_cours) + "+match"
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=round_select)

        # aller chercher les listes en fonction du round en cours
        List_de_liste_joueur = (db_tournoi[0][round_select])

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="List_de_liste_joueur")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 1")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[1])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 2")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[2])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 3")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[3])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="paire 4")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[4])

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

        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 1: ' + (saisie_score1) + " - " + saisie_score2)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire1_j1 = []
        liste_paire1_j2 = []
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="List_de_liste_joueur")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="List_de_liste_joueur[1][0]")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=List_de_liste_joueur[1][0])
        liste_paire1_j1.append(List_de_liste_joueur[1][0])
        liste_paire1_j1.append(saisie_score1)

        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire1_j1)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire1_j2)
        # joueur 2
        liste_paire1_j2 = []
        liste_paire1_j2.append(List_de_liste_joueur[1][1])
        liste_paire1_j2.append(saisie_score2)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire1_j2)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 2: ' + (saisie_score3) + " - " + saisie_score4)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire2_j1 = []
        liste_paire2_j1.append(List_de_liste_joueur[2][0])
        liste_paire2_j1.append(saisie_score3)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire2_j1)
        # joueur 2
        liste_paire2_j2 = []
        liste_paire2_j2.append(List_de_liste_joueur[2][1])
        liste_paire2_j2.append(saisie_score4)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire2_j2)

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
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire3_j1 = []
        liste_paire3_j1.append(List_de_liste_joueur[3][0])
        liste_paire3_j1.append(saisie_score5)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire3_j1)
        # joueur 2
        liste_paire3_j2 = []
        liste_paire3_j2.append(List_de_liste_joueur[3][1])
        liste_paire3_j2.append(saisie_score6)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire3_j2)

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

        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1='saisie score 1 et 2 du '
                                                 'match 4: ' + (saisie_score7) + " - " + saisie_score8)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire4_j1 = []
        liste_paire4_j1.append(List_de_liste_joueur[4][0])
        liste_paire4_j1.append(saisie_score7)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire4_j1)

        # joueur 2
        liste_paire4_j2 = []
        liste_paire4_j2.append(List_de_liste_joueur[4][1])
        liste_paire4_j2.append(saisie_score8)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire4_j2)

        # Chaque match génèrera 1 tuple avec comme nom,
        # « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple4 = "IdTournoi" + str(tournoi_select) + "_" + "Round" + str(round_en_cours) + "_" + "Match" + "4"

        globals()[nom_tuple4] = ((liste_paire4_j1[0],
                                  liste_paire4_j1[1],
                                  liste_paire4_j2[0],
                                  liste_paire4_j2[1]))

        # préparation  pour mise dans la base de donnée
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

        # création des tuples
        tupl1 = (liste_paire1_j1, liste_paire1_j2)
        tupl2 = (liste_paire2_j1, liste_paire2_j2)
        tupl3 = (liste_paire3_j1, liste_paire3_j2)
        tupl4 = (liste_paire4_j1, liste_paire4_j2)

        from Modele.Match import ClassMatch
        # appel des modèles de création de matchs
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=1, tuple_match=tupl1)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=2, tuple_match=tupl2)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=3, tuple_match=tupl3)
        ClassMatch.CreatMatch(self=True, id_tournoi=tournoi_select, num_round=round_en_cours,
                              num_paire=4, tuple_match=tupl4)

        # mise de l'heure de fin du match
        # pour la mettre dans la base de donnée du tournoi
        date_heure_fin = datetime.datetime.now()
        str_date_heure_fin = str(date_heure_fin)
        char = '.'
        PositChar = str_date_heure_fin.find(char)
        str_date_heure_fin = str_date_heure_fin[0:(PositChar)]
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="fin round en "
                                                 "cours " + str(round_en_cours) + " : " + str_date_heure_fin)

        # chargment dans la base de données des scores des 4 matchs du round
        nom_donnees = "ScoreMatchRound" + str(round_en_cours)

        liste_4matchs = []
        liste_4matchs.append(liste_paire1_j1)
        liste_4matchs.append(liste_paire1_j2)
        liste_4matchs.append(liste_paire2_j1)
        liste_4matchs.append(liste_paire2_j2)
        liste_4matchs.append(liste_paire3_j1)
        liste_4matchs.append(liste_paire3_j2)
        liste_4matchs.append(liste_paire4_j1)
        liste_4matchs.append(liste_paire4_j2)

        # Appel Modele Tournoi pour enregistrement des donnees dans la base de donnees
        ClassModTournoi.UpdateDonneesTournoi(self=True, numero_tournoi=int(tournoi_select),
                                             nom_donnee=nom_donnees, donnee=liste_4matchs)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
