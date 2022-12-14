class Class_Round():
    def __init__(self):
        pass

    import os
    from Controleur.fonctions import ClassFonctions
    from datetime import datetime
    from Controleur.Ctrl_Tournoi import Class_Tournoi
    from Modele.Tournoi import ClassModTournoi

    def creat_round():
        from Modele.Tournoi import ClassModTournoi
        from Controleur.fonctions import ClassFonctions
        from Vue.affichage import ClassVueAffichage
        # selection du tournoi
        tournoi_select = ClassFonctions.select_tournoi()
        int_tournoi_select = int(tournoi_select)

        # Appel du modèle pour mettre à disposition les données du round sélectionné
        tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int_tournoi_select)

        tournoi_round_en_cours = 0
        try:
            tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
            tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
            nb_r = (tournoi[0]['nombre de rounds'])
            if str(tournoi_round_en_cours) == str(nb_r):
                ClassVueAffichage.Affichage1Ligne(self=True,
                                                  texte1="le nombre de round maximum a déjà été créé pour ce tournoi")
                quit()
            else:
                nb_r = (tournoi[0]['nombre de rounds'])
                if str(tournoi_round_en_cours) == str(nb_r):
                    ClassVueAffichage.Affichage1Ligne(self=True,
                                                      texte1="le nombre de round maximum a déjà été créé "
                                                             "pour ce tournoi")
                    quit()

        except KeyError:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="création du round 1")

        if tournoi_round_en_cours == 1:
            try:
                scoreMatchRound1 = (tournoi[0]['ScoreMatchRound1'])
            except KeyError:
                ClassVueAffichage.Affichage1Ligne(self=True, texte1="Saisir les scores du précédent round avant "
                                                                    "d'en créer un nouveau")
                quit()
            scoreMatchRound1 = scoreMatchRound1

        if tournoi_round_en_cours == 2:
            try:
                scoreMatchRound2 = (tournoi[0]['ScoreMatchRound2'])
            except KeyError:
                ClassVueAffichage.Affichage1Ligne(self=True, texte1="Saisir les scores du précédent round avant "
                                                                    "d'en créer un nouveau")
                quit()
            scoreMatchRound3 = scoreMatchRound2

        if tournoi_round_en_cours == 3:
            try:
                scoreMatchRound3 = (tournoi[0]['ScoreMatchRound3'])
            except KeyError:
                ClassVueAffichage.Affichage1Ligne(self=True, texte1="Saisir les scores du précédent round avant "
                                                                    "d'en créer un nouveau")
                quit()
            scoreMatchRound3 = scoreMatchRound3

        if tournoi_round_en_cours == 4:
            try:
                scoreMatchRound4 = (tournoi[0]['ScoreMatchRound4'])
            except KeyError:
                ClassVueAffichage.Affichage1Ligne(self=True, texte1="Saisir les scores du précédent round avant "
                                                                    "d'en créer un nouveau")
                quit()
            scoreMatchRound4 = scoreMatchRound4

        # selon que le 1er round ait été créé ou non, appel de création round 1 ou round au delà
        if tournoi_round_en_cours == 0:
            Class_Round.creat_round_1(tournoi_select)
        else:
            Class_Round.creat_round_2(tournoi_select)
        return ()

    def creat_round_1(tournoi_select):
        import datetime
        import os
        from Controleur.fonctions import ClassFonctions
        from Modele.Tournoi import ClassModTournoi
        from Modele.Joueurs import ClassJoueursModel
        from Vue.affichage import ClassVueAffichage
        from Modele.Round import ClassRound

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="CreatRound_1")
        liste_liste_class_joueur = []

        # Appel du modèle pour mettre à disposition les données du round sélectionné
        int_tournoi_select = int(tournoi_select)
        tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int_tournoi_select)

        list_id_joueur = []
        list_id_joueur = ClassFonctions.ListejoueursTournoi(self=True, tournoi=tournoi, clef1="id_j1", clef2="id_j2",
                                                            clef3="id_j3", clef4="id_j4", clef5="id_j5", clef6="id_j6",
                                                            clef7="id_j7", clef8="id_j8")

        id_joueur_en_cours = ""
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=list_id_joueur)
        index_joueur = 0
        id_joueur_en_cours = list_id_joueur[index_joueur]
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=id_joueur_en_cours)

        index_joueur = 0
        while (index_joueur < 8):
            id_joueur_en_cours = ""
            int_id_joueur_en_cours = ""
            # Essayer de récupérer les joueurs du tournoi
            try:
                id_joueur_en_cours = list_id_joueur[index_joueur]
            except ValueError:
                ClassVueAffichage.Affichage1Ligne(self=True,
                                                  texte1="Vous devez choisir un tournoi où les 8 joueurs sont "
                                                         "chargés pour créer des rounds")
                os._exit()

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                ClassVueAffichage.Affichage1Ligne(self=True,
                                                  texte1="Erreur, vous devez choisir un tournoi où les joueurs sont "
                                                         "chargés pour créer des rounds")
                os._exit(0)

            # Appel du modele joueur pour mise à disposition d'un joueur
            joueur = ClassJoueursModel.MisADispoJoueurTournoi(self=True, id_joueur=int_id_joueur_en_cours)
            dict_joueur = ClassFonctions.creat_dict(donnees_db=joueur)

            round_id_joueur = (dict_joueur["id_joueur"])
            round_nom_joueur = (dict_joueur["Nom"])
            round_prenom_joueur = (dict_joueur["Prenom"])
            round_class_joueur = (dict_joueur["Classement"])
            liste_class_joueur = [round_id_joueur, int(round_class_joueur),
                                  round_nom_joueur,
                                  round_prenom_joueur]
            liste_liste_class_joueur.append(liste_class_joueur)
            index_joueur = index_joueur + 1

        # Mise des joueurs dans ordre décroissant
        from operator import itemgetter

        # Mise en ordre des joueurs par classement, le classement étant
        # la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur,
                                         key=itemgetter(1),
                                         reverse=False))

        liste_paire_1 = []
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])

        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Paire 1, par ordre de classement, 1er joueur contre 5ème")
        str_poubl = ("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_1[0][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="VS")
        str_poubl = ("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_1[1][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        str_poubl = ("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_2[0][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="VS")
        str_poubl = ("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_2[1][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        str_poubl = ("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_3[0][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="VS")
        str_poubl = ("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_3[1][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        str_poubl = ("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_4[0][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="ID")
        str_poubl = ("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]))
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1=str_poubl + " , Prénom : " + str(liste_paire_4[1][3]))
        str_poubl = ""
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="*** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ***")
        ClassVueAffichage.Affichage1Ligne(self=True,
                                          texte1="Round 1 créé")
        # mise de l'heure de depart dans la liste pour la mettre dans la base
        # de donnée du tournoi
        date_heure_debut = datetime.datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="début heure round : " + str_date_heure_debut)

        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire_1)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire_2)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire_3)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_paire_4)

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="*** FIN CREATION ROUND 1 ***")

        # Stocker les instances de Round dans le tournoi
        liste_round_1 = []
        liste_round_1.append(str_date_heure_debut)
        liste_round_1.append(liste_paire_1)
        liste_round_1.append(liste_paire_2)
        liste_round_1.append(liste_paire_3)
        liste_round_1.append(liste_paire_4)

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="numéro de tournoi")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=int_tournoi_select)

        # appel du modele round pour enregistrer le nouveau round dans la base de données
        ClassRound.CreatRound(self=True, id_tournoi=int_tournoi_select, num_round=1,
                              liste_paire1=liste_paire_1, liste_paire2=liste_paire_2,
                              liste_paire3=liste_paire_3, liste_paire4=liste_paire_4)

        # appel du modele tournoi pour enregistrer le nouveau tournoi dans la base de données
        ClassModTournoi.UpdateDonneesTournoi(self=True,
                                             numero_tournoi=int_tournoi_select,
                                             nom_donnee="round_1+match",
                                             donnee=liste_round_1)

        # appel du modele tournoi pour enregistrer le round en cours
        ClassModTournoi.UpdateDonneesTournoi(self=True,
                                             numero_tournoi=int_tournoi_select,
                                             nom_donnee="round_en_cours",
                                             donnee=1)
        return ()

    def creat_round_2(tournoi_select):
        import datetime
        import os
        from Controleur.fonctions import ClassFonctions
        from Modele.Tournoi import ClassModTournoi
        from Modele.Joueurs import ClassJoueursModel
        from Vue.affichage import ClassVueAffichage
        from operator import itemgetter
        from Modele.Round import ClassRound

        liste_liste_class_joueur = []

        int_tournoi_select = int(tournoi_select)
        tournoi = ClassModTournoi.Lect1Tournoi(self=True, tournoi_select=int_tournoi_select)

        Tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="Round précédent : " + str(Tournoi_round_en_cours))

        nb_r = (tournoi[0]['nombre de rounds'])

        list_id_joueur = []
        list_id_joueur = ClassFonctions.ListejoueursTournoi(self=True, tournoi=tournoi, clef1="id_j1", clef2="id_j2",
                                                            clef3="id_j3", clef4="id_j4", clef5="id_j5", clef6="id_j6",
                                                            clef7="id_j7", clef8="id_j8")

        index_joueur = 0
        list_jx = []
        while (index_joueur < 8):

            id_joueur_en_cours = ""
            int_id_joueur_en_cours = ""
            try:
                id_joueur_en_cours = list_id_joueur[index_joueur]
            except IndexError:
                ClassVueAffichage.Affichage1Ligne(self=True,
                                                  texte1="Vous devez choisir un tournoi où les 8 joueurs "
                                                         "sont chargés pour créer des rounds X")
                os._exit(1)

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                ClassVueAffichage.Affichage1Ligne(self=True,
                                                  texte1="Erreur, vous devez choisir un tournoi où les 8 joueurs "
                                                         "sont chargés pour créer des rounds Y")
                os._exit(0)

            # Appel du modele joueur pour mise à disposition d'un joueur
            joueur = ClassJoueursModel.MisADispoJoueurTournoi(self=True, id_joueur=int_id_joueur_en_cours)
            dict_joueur = ClassFonctions.creat_dict(joueur)
            # identifiant joueur
            round_id_joueur = (dict_joueur["id_joueur"])
            # nom joueur
            round_nom_joueur = (dict_joueur["Nom"])
            # Prénom
            round_prenom_joueur = (dict_joueur["Prenom"])
            # Classement
            round_class_joueur = (dict_joueur["Classement"])

            # reconstitution liste plus courte avec id_joueur, classement joueur,
            # nom, prenom")
            liste_class_joueur = [round_id_joueur,
                                  int(round_class_joueur),
                                  round_nom_joueur,
                                  round_prenom_joueur]

            liste_liste_class_joueur.append(liste_class_joueur)

            # SI TOURNOI ROUND EN COURS = 1 FAIRE
            list_ja = [round_id_joueur, int(round_class_joueur), 0]
            list_jx.append(list_ja)
            index_joueur = index_joueur + 1

        # Récupération des scores des joueurs dans le tournoi pour les mettre
        # dans une liste
        # de joueur qui contient, l'id du joueur, son score, son classement
        # les scores s'incrémentent des scores des matchs précédents en utilisant
        # le round en cours
        # pour savoir combien de scores à aller chercher, attention,
        # les joueurs ne sont pas dans le même ordre
        # Ajout des scores précédents à la liste
        # Récupération des scores des précédents matchs.
        joueur_score_class_id = []
        if Tournoi_round_en_cours > 1:
            Tournoi_round_en_cours_temp = Tournoi_round_en_cours
        else:
            Tournoi_round_en_cours_temp = Tournoi_round_en_cours

        joueur_score_class_id_new = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0],
                                     ["", 0], ["", 0], ["", 0]]

        # Récupération des scores précédents pour les aditionner
        while Tournoi_round_en_cours_temp > 0:

            # Construction de l'étiquette permettant d'aller chercher les résultats
            # des rounds précédents
            # dans la base de donnée
            # ScoreMatchRound1, "ScoreMatchRound2", "ScoreMatchRound3",
            # "ScoreMatchRound4"
            score_match_round_temp = "ScoreMatchRound" + \
                                     str(Tournoi_round_en_cours_temp)  # New

            # Recherche des scores du match dans la base de donnée du round traité
            # le round suivant sera traité dans le tous qui suit jusqu'à ce que
            # tous les rounds soient traités
            score_matchRx_temp = (tournoi[0][score_match_round_temp])

            # Les résultats du match sont triés par ordre d'id des joueurs
            # pour que les résultats qu'on additionne soit cohérent
            joueur_score_class_id_temp = (sorted(score_matchRx_temp,
                                                 key=itemgetter(0),
                                                 reverse=True))
            joueur_score_class_id.append(joueur_score_class_id_temp)
            index = 0
            # Pour les 8 joueurs,
            while index < 8:
                joueur_score_class_id_new[index][0] = \
                    joueur_score_class_id_temp[index][0]

                score_en_cours = float(joueur_score_class_id_temp[index][1])

                score_enreg = float(joueur_score_class_id_new[index][1])

                score_total = score_en_cours + score_enreg
                joueur_score_class_id_new[index].insert(1, str(score_total))
                index = index + 1

            Tournoi_round_en_cours_temp = Tournoi_round_en_cours_temp - 1

        list_jx_class_id = (sorted(list_jx, key=itemgetter(0), reverse=True))
        index_0 = 0
        index_1 = 1
        index_2 = 2
        while index_1 < 16:
            score_total = float(joueur_score_class_id_new[index_0][1])
            list_jx_class_id[index_0][2] = score_total
            index_0 = index_0 + 1
            index_1 = index_1 + 2
            index_2 = index_2 + 3

        # Mise des joueurs dans ordre décroissant
        from operator import itemgetter

        # Mise en ordre des joueurs par classement, le classement étant
        # la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(list_jx,
                                         key=itemgetter(1),
                                         reverse=False))

        joueur_class_score_croissant = (sorted(joueur_class_croissant,
                                               key=itemgetter(2),
                                               reverse=True))

        # Construction liste de joueurs déjà affrontés par joueur;
        joueur_1 = [joueur_class_score_croissant[0][0]]
        joueur_2 = [joueur_class_score_croissant[1][0]]
        joueur_3 = [joueur_class_score_croissant[2][0]]
        joueur_4 = [joueur_class_score_croissant[3][0]]
        joueur_5 = [joueur_class_score_croissant[4][0]]
        joueur_6 = [joueur_class_score_croissant[5][0]]
        joueur_7 = [joueur_class_score_croissant[6][0]]
        joueur_8 = [joueur_class_score_croissant[7][0]]

        list_jy = []
        list_jy.append(joueur_1)
        list_jy.append(joueur_2)
        list_jy.append(joueur_3)
        list_jy.append(joueur_4)
        list_jy.append(joueur_5)
        list_jy.append(joueur_6)
        list_jy.append(joueur_7)
        list_jy.append(joueur_8)

        # faire une boucle sur tous les rounds joués
        # donc enlever 1 au tournoi en cours temp
        # Rechercher les scores de chaque joueur dont l'emplacment est
        # différent selon le round

        if Tournoi_round_en_cours > 1:
            Tournoi_round_en_cours_temp = Tournoi_round_en_cours
        else:
            Tournoi_round_en_cours_temp = Tournoi_round_en_cours

        # recherche joueurs déjà affrontés ROUND 2 ET PLUS")
        list_j_opp = [[joueur_class_score_croissant[0][0]],
                      [joueur_class_score_croissant[1][0]],
                      [joueur_class_score_croissant[2][0]],
                      [joueur_class_score_croissant[3][0]],
                      [joueur_class_score_croissant[4][0]],
                      [joueur_class_score_croissant[5][0]],
                      [joueur_class_score_croissant[6][0]],
                      [joueur_class_score_croissant[7][0]]]

        # "list_j_opp - joueurs triés en fonction de leur score en "
        #         "priorité et de leur classement en second lieu"
        while Tournoi_round_en_cours_temp > 0:
            nom_donnees = "ScoreMatchRound" + str(Tournoi_round_en_cours_temp)

            score_matchRx = (tournoi[0][nom_donnees])

            # Faire une boucle avec les 8 joueurs, et faire une liste de liste de
            # joueur ayant déjà joué ensemble
            index_id_jy = 0

            # Faire une liste de 8 joueurs en y ajoutant tous les joueurs affrontés
            # dans des duels précédents
            while (index_id_jy < 8):
                index_position_paire = 1
                index_position_impaire = 0
                # faire une boucle des 4 paires des scores
                # Faire une boucle pour vérifier que l'id du joueur se trouve dans
                # les 4 paires
                # Construction de la liste des 8 joueurs avec les joueurs affrontés
                # précédemment
                # Dans le cas où le joueur opposé est en position index paire,
                # c'est le joueur suivant qui
                # est comparé, alors qu'en position impaire c'est le joueur
                # précédent,
                # d'où les 2 tests dans la boucle while
                while index_position_impaire < 7:
                    # Recherche si l'id est dans les scores précédents,
                    if list_j_opp[index_id_jy][0] ==\
                            score_matchRx[index_position_impaire][0]:
                        index = index_position_impaire + 1
                        list_jy[index_id_jy].append(score_matchRx[index][0])

                    if list_j_opp[index_id_jy][0] == \
                            score_matchRx[index_position_paire][0]:
                        index = index_position_paire - 1
                        list_jy[index_id_jy].append(score_matchRx[index][0])

                    index_position_impaire = index_position_impaire + 2
                    index_position_paire = index_position_paire + 2
                index_id_jy = index_id_jy + 1

            Tournoi_round_en_cours_temp = Tournoi_round_en_cours_temp - 1
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="list_jy_joueurs deja "
                                                                "affrontés dans les rounds précédents : ")
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=list_jy)

        liste_paire_1 = []
        liste_paire_1.append(joueur_class_score_croissant[0])
        liste_paire_1.append(joueur_class_score_croissant[1])
        # 1er joueur contre 2ème "
        #       "si pas déjà rencontré le 2ème")

        # Tester joueur suivant liste temporaire triée [0] avec liste des joueurs
        # déjà rencontrée [x] jusqu'à ce que x égal nbre de round

        # Si pas joueur rencontré, et liste parcourue,
        # mettre le joueur suivant testé dans la paire

        # Sinon, refaire le test avec le joueur suivant

        # Supprimer les joueurs de la liste triée temporaire et de l'autre
        # liste les joueurs mis dans la paire

        # et faire le test encore pour le joueur 1, puisqu'en supprimant
        # les joueurs de la liste, le deuxième joueur testé est remonté en haut
        # de la liste

        joueur_class_score_croissant_temp = joueur_class_score_croissant

        # Tant que les paires crées <= 3, la dernière étant constituée
        # des 2 joueurs restants
        list_jy_temp = list_jy

        list_list_part = []
        nbr_part_rest_a_tester = 8
        while nbr_part_rest_a_tester > 0:
            index_partenaire = 1

            # Tant que tous les 7 partenaires non testés
            list_part = []
            list_list_part = []
            while index_partenaire < nbr_part_rest_a_tester and nbr_part_rest_a_tester != 0:
                index_nbr_part_affront = 0

                # tant que tous les partenaires testés n'ont pas vérifié
                # tous les partenaires affrontés
                index_joueur_affront = 1
                test_joueur_affront = 0
                # test les joueurs affrontés précédemment, le nombre de fois
                # correspondant au nombre de round précédent
                partenaire_libre = ""
                while index_nbr_part_affront < Tournoi_round_en_cours and nbr_part_rest_a_tester != 0:
                    joueur_1_test = joueur_class_score_croissant_temp[index_partenaire][0]

                    if list_jy_temp[index_partenaire][0] == list_jy_temp[0][index_joueur_affront]:

                        test_joueur_affront = test_joueur_affront + 1
                    else:
                        pass

                    # Si tous les joueurs testés et pas trouvé de déjà rencontré,
                    # le partenaire est ok
                    if test_joueur_affront == 0 and index_nbr_part_affront == \
                        (Tournoi_round_en_cours - 1) and \
                            nbr_part_rest_a_tester != 0:
                        partenaire_libre = joueur_1_test
                    # Si le partenaire testé est le 7ème, on le donne libre même
                    # s'il est déjà rencontré
                    # Si index partenaire = 1, et reste que 2 partenaires à tester
                    if (index_partenaire + 1) == nbr_part_rest_a_tester:
                        partenaire_libre = joueur_1_test

                    # Si partenaire libre, faire une liste de paire
                    # puis, faire une liste de liste de paire
                    # ensuite, supprimer les 2 joueurs de la liste à tester
                    list_part = []
                    if partenaire_libre == joueur_1_test:
                        list_part.append(list_jy_temp[0])
                        # si les derniers partenaires, les appairer d'office
                        if nbr_part_rest_a_tester == 2:
                            list_part.append(list_jy_temp[1])
                        else:
                            list_part.append(list_jy_temp[index_partenaire])

                        list_list_part.append(list_part)
                        list_jy_temp.pop(0)
                        # enlever 1 à l'index, la suppression du joueur ayant
                        # décalé le partenaire à supprimer
                        list_jy_temp.pop(index_partenaire - 1)
                        nbr_part_rest_a_tester = nbr_part_rest_a_tester - 2
                        index_partenaire = 0
                    index_joueur_affront = index_joueur_affront + 1
                    index_nbr_part_affront = index_nbr_part_affront + 1
                index_partenaire = index_partenaire + 1

        ClassVueAffichage.Affichage1Ligne(self=True, texte1=list_list_part)
        list_paire1_round = []
        list_list_paire1_round = []
        list_paire1_round.append(list_list_part[0][0][0])
        list_paire1_round.append(list_list_part[0][1][0])
        list_list_paire1_round.append(list_paire1_round)

        list_list_paire2_round = []
        list_paire2_round = []
        list_paire2_round.append(list_list_part[1][0][0])
        list_paire2_round.append(list_list_part[1][1][0])
        list_list_paire2_round.append(list_paire2_round)

        list_list_paire3_round = []
        list_paire3_round = []
        list_paire3_round.append(list_list_part[2][0][0])
        list_paire3_round.append(list_list_part[2][1][0])
        list_list_paire3_round.append(list_paire3_round)

        list_list_paire4_round = []
        list_paire4_round = []
        list_paire4_round.append(list_list_part[3][0][0])
        list_paire4_round.append(list_list_part[3][1][0])
        list_list_paire4_round.append(list_paire4_round)

        # Stocker les instances de Round dans le tournoi
        date_heure_debut = datetime.datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="début heure round : " + str_date_heure_debut)

        liste_round_x = []
        liste_round_x.append(str_date_heure_debut)
        liste_round_x.append(list_paire1_round)
        liste_round_x.append(list_paire2_round)
        liste_round_x.append(list_paire3_round)
        liste_round_x.append(list_paire4_round)
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="liste_round" + str(Tournoi_round_en_cours + 1))
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=liste_round_x)

        ClassVueAffichage.Affichage1Ligne(self=True, texte1="")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1="numéro de tournoi")
        ClassVueAffichage.Affichage1Ligne(self=True, texte1=int_tournoi_select)

        # Test si dernier round du tournoi
        if Tournoi_round_en_cours < int(nb_r):
            Tournoi_round_en_cours = Tournoi_round_en_cours + 1
        else:
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="Nombre maxi de round atteint !")

        # update la base de donnée
        if Tournoi_round_en_cours <= int(nb_r):
            update_round = ("round_" + str(Tournoi_round_en_cours) + "+match")
            ClassVueAffichage.Affichage1Ligne(self=True, texte1="nouveau round")
            ClassVueAffichage.Affichage1Ligne(self=True, texte1=Tournoi_round_en_cours)

            # appel du modele round pour enregistrer le nouveau round dans la base de données
            ClassRound.CreatRound(self=True, id_tournoi=int_tournoi_select, num_round=Tournoi_round_en_cours,
                                  liste_paire1=list_paire1_round, liste_paire2=list_paire2_round,
                                  liste_paire3=list_paire3_round, liste_paire4=list_paire4_round)

            # appel du modele tournoi pour enregistrer le nouveau tournoi dans la base de données
            ClassModTournoi.UpdateDonneesTournoi(self=True,
                                                 numero_tournoi=int_tournoi_select,
                                                 nom_donnee=update_round,
                                                 donnee=(liste_round_x))

            # appel du modele tournoi pour enregistrer le round en cours
            ClassModTournoi.UpdateDonneesTournoi(self=True,
                                                 numero_tournoi=int_tournoi_select,
                                                 nom_donnee="round_en_cours",
                                                 donnee=Tournoi_round_en_cours)
        return ()
