class Class_Round():
    def __init__(self):
        pass

    import os
    from Controleur.fonctions import ClassFonctions
    from datetime import datetime
    from Controleur.Ctrl_Tournoi import Class_Tournoi
    from Modele.Tournoi import ClassTournoi

    def creat_round():
        from Controleur.fonctions import ClassFonctions
        tournoi_select = ClassFonctions.select_tournoi()
        # print("Prochain round tournoi sélectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, where
        db_tournois = TinyDB('tournois.json')
        int_tournoi_select = int(tournoi_select)

        # récup le tournoi sélectionné à partir de la base de données du tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

        tournoi_round_en_cours = 0
        try:
            tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
            # print("Round précédent : " + str(tournoi_round_en_cours))
            tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
            nb_r = (tournoi[0]['nombre de rounds'])
            if str(tournoi_round_en_cours) == str(nb_r):
                print("le nombre de round maximum a déjà été créé pour"
                      " ce tournoi")
                quit()
            else:
                nb_r = (tournoi[0]['nombre de rounds'])
                if str(tournoi_round_en_cours) == str(nb_r):
                    print("le nombre de round maximum a déjà été créé pour"
                          " ce tournoi")
                    quit()
                # else:
                # creat_round_2(tournoi_select)

        except KeyError:
            print("création du round 1")

        if tournoi_round_en_cours == 1:
            try:
                scoreMatchRound1 = (tournoi[0]['ScoreMatchRound1'])
            except KeyError:
                print("Saisir les scores du précédent round avant "
                      "d'en créer un nouveau")
                quit()
            scoreMatchRound1 = scoreMatchRound1

        if tournoi_round_en_cours == 2:
            try:
                scoreMatchRound2 = (tournoi[0]['ScoreMatchRound2'])
            except KeyError:
                print("Saisir les scores du précédent round avant "
                      "d'en créer un nouveau")
                quit()
            scoreMatchRound3 = scoreMatchRound2

        if tournoi_round_en_cours == 3:
            try:
                scoreMatchRound3 = (tournoi[0]['ScoreMatchRound3'])
            except KeyError:
                print("Saisir les scores du précédent round avant "
                      "d'en créer un nouveau")
                quit()
            scoreMatchRound3 = scoreMatchRound3

        if tournoi_round_en_cours == 4:
            try:
                scoreMatchRound4 = (tournoi[0]['ScoreMatchRound4'])
            except KeyError:
                print("Saisir les scores du précédent round avant "
                      "d'en créer un nouveau")
                quit()
            scoreMatchRound4 = scoreMatchRound4
        if tournoi_round_en_cours == 0:
            Class_Round.creat_round_1(tournoi_select)
        else:
            Class_Round.creat_round_2(tournoi_select)
        return ()

    def creat_round_1(tournoi_select):
        import datetime
        import os
        from Controleur.fonctions import ClassFonctions
        print("CreatRound_1")
        liste_liste_class_joueur = []
        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        # charger le tournoi selectionné à partir de la base de données tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        # Récupération des données de la base de donnée tournoi pour constitution
        # des rounds

        id_t = (tournoi[0]['id_tournoi'])
        print("id tournoi : " + str(id_t))

        nom_t = (tournoi[0]['nom'])
        print("nom : " + nom_t)

        nb_r = (tournoi[0]['nombre de rounds'])
        print(nb_r + " rounds")

        list_id_joueur = []

        id_j1 = (tournoi[0]['id_j1'])
        print("id joueur 1 : " + id_j1)
        list_id_joueur.append(id_j1)

        id_j2 = (tournoi[0]['id_j2'])
        print("id joueur 2 : " + id_j2)
        list_id_joueur.append(id_j2)

        id_j3 = (tournoi[0]['id_j3'])
        print("id joueur 3 : " + id_j3)
        list_id_joueur.append(id_j3)

        id_j4 = (tournoi[0]['id_j4'])
        print("id joueur 4 : " + id_j4)
        list_id_joueur.append(id_j4)

        id_j5 = (tournoi[0]['id_j5'])
        print("id joueur 5 : " + id_j5)
        list_id_joueur.append(id_j5)

        id_j6 = (tournoi[0]['id_j6'])
        print("id joueur 6 : " + id_j6)
        list_id_joueur.append(id_j6)

        id_j7 = (tournoi[0]['id_j7'])
        print("id joueur 7 : " + id_j7)
        list_id_joueur.append(id_j7)

        id_j8 = (tournoi[0]['id_j8'])
        print("id joueur 8 : " + id_j8)
        list_id_joueur.append(id_j8)

        print("nombre de rounds")
        print(nb_r)

        db_joueurs = TinyDB('joueurs.json')
        index_joueur = 0
        while (index_joueur < 8):
            print("id_joueur " + str(index_joueur) + ": ")
            id_joueur_en_cours = ""
            int_id_joueur_en_cours = ""
            # Essayer de récupérer les joueurs du tournoi
            try:
                id_joueur_en_cours = list_id_joueur[index_joueur]
            except ValueError:
                print("Vous devez choisir un tournoi où les 8 joueurs sont "
                      "chargés pour créer des rounds")
                os._exit()

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                print("Erreur, vous devez choisir un tournoi où les joueurs sont "
                      "chargés pour créer des rounds")
                os._exit(0)

            joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
            dict_joueur = ClassFonctions.creat_dict(donnees_db=joueur)

            print("identifiant joueur :")
            round_id_joueur = (dict_joueur["id_joueur"])
            print(round_id_joueur)

            print("Nom :")
            print(dict_joueur["Nom"])
            round_nom_joueur = (dict_joueur["Nom"])

            print("Prénom :")
            print(dict_joueur["Prenom"])
            round_prenom_joueur = (dict_joueur["Prenom"])

            print("Né le :")
            print(dict_joueur["date de naissance"])

            print("Sexe :")
            print(dict_joueur["sexe"])

            print("Classement :")
            round_class_joueur = (dict_joueur["Classement"])
            print(round_class_joueur)

            liste_class_joueur = [round_id_joueur, int(round_class_joueur),
                                  round_nom_joueur,
                                  round_prenom_joueur]
            print("liste : id_joueur, classement joueur, nom, prenom")
            print(liste_class_joueur)
            liste_liste_class_joueur.append(liste_class_joueur)
            print(liste_liste_class_joueur)

            index_joueur = index_joueur + 1

            # print("FIN RECUPERATION DES DONNEES DU JOUEUR")

        print("liste_liste_class_joueur : ")
        print(liste_liste_class_joueur)

        # Mise des joueurs dans ordre décroissant
        from operator import itemgetter
        print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur,
                                                       key=itemgetter(1),
                                                       reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur,
                                           key=itemgetter(1),
                                           reverse=True))
        print(joueur_class_decroissant)

        # Mise en ordre des joueurs par classement, le classement étant
        # la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur,
                                         key=itemgetter(1),
                                         reverse=False))
        print("Affichage joueur par classement croissant")
        print(joueur_class_croissant)

        print("Affichage des paires de joueurs par identifiant du round 1 \n")

        liste_paire_1 = []
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])
        # print(liste_paire_1)

        str_poubl = ""
        print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
        str_poubl = ("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_1[0][3]))
        str_poubl = ""
        print("VS")
        str_poubl = ("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_1[1][3]))
        str_poubl = ""
        print()

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        # print(liste_paire_2)
        print("Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        str_poubl = ("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_2[0][3]))
        str_poubl = ""
        print("VS")
        str_poubl = ("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_2[1][3]))
        str_poubl = ""
        print()

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        # print(liste_paire_3)
        print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        str_poubl = ("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_3[0][3]))
        str_poubl = ""
        print("VS")
        str_poubl = ("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_3[1][3]))
        str_poubl = ""
        print()

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        # print(liste_paire_4)
        print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        str_poubl = ("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_4[0][3]))
        str_poubl = ""
        print("ID")
        str_poubl = ("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]))
        print(str_poubl + " , Prénom : " + str(liste_paire_4[1][3]))
        str_poubl = ""
        print()
        print("*** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ***")
        print("Round 1 créé")
        # mise de l'heure de depart dans la liste pour la mettre dans la base
        # de donnée du tournoi
        date_heure_debut = datetime.datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print("début heure round : " + str_date_heure_debut)

        print(liste_paire_1)
        print(liste_paire_2)
        print(liste_paire_3)
        print(liste_paire_4)

        print("********* FIN CREATION ROUND 1 *************************")

        # Stocker les instances de Round dans le tournoi
        liste_round_1 = []
        liste_round_1.append(str_date_heure_debut)
        liste_round_1.append(liste_paire_1)
        liste_round_1.append(liste_paire_2)
        liste_round_1.append(liste_paire_3)
        liste_round_1.append(liste_paire_4)

        from tinydb import TinyDB, Query, where
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)

        # FAIRE UNE METHODE DANS MODELE ET L'APPELER ICI POUR RESPECT MVC
        # La sélection du round 1 est sauvegardée dans la base de données tournoi
        # il faudra écraser l'instance avec le résultat en plus des matchs
        # Si round_1+match n'existe pas dans la base de donnée, il est créé
        db_tournois.update({"round_1+match": liste_round_1},
                           Todo.id_tournoi == int_tournoi_select)

        # Ecriture du round en cours dans la base de donnée du tournoi
        db_tournois.update({"round_en_cours": 1},
                           Todo.id_tournoi == int_tournoi_select)

        return ()

    def creat_round_2(tournoi_select):
        import datetime
        import os
        from Controleur.fonctions import ClassFonctions
        from Modele.Tournoi import ClassTournoi
        from operator import itemgetter
        from tinydb import TinyDB, Query, where
        # print("CreatRound_2 et plus. Début du programme")
        liste_liste_class_joueur = []
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        int_tournoi_select = int(tournoi_select)

        # charger le tournoi selectionné à partir de la base de données
        # dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

        # Récupération des informations du fichier JSON du tournoi pour
        # créer les rounds

        Tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
        print("Round précédent : " + str(Tournoi_round_en_cours))

        nb_r = (tournoi[0]['nombre de rounds'])

        list_id_joueur = []

        id_j1 = (tournoi[0]['id_j1'])
        list_id_joueur.append(id_j1)

        id_j2 = (tournoi[0]['id_j2'])
        list_id_joueur.append(id_j2)

        id_j3 = (tournoi[0]['id_j3'])
        list_id_joueur.append(id_j3)

        id_j4 = (tournoi[0]['id_j4'])
        list_id_joueur.append(id_j4)

        id_j5 = (tournoi[0]['id_j5'])
        list_id_joueur.append(id_j5)

        id_j6 = (tournoi[0]['id_j6'])
        list_id_joueur.append(id_j6)

        id_j7 = (tournoi[0]['id_j7'])
        list_id_joueur.append(id_j7)

        id_j8 = (tournoi[0]['id_j8'])
        list_id_joueur.append(id_j8)

        db_joueurs = TinyDB('joueurs.json')
        index_joueur = 0
        list_jx = []
        while (index_joueur < 8):

            id_joueur_en_cours = ""
            int_id_joueur_en_cours = ""
            try:
                id_joueur_en_cours = list_id_joueur[index_joueur]
            except IndexError:
                print("Vous devez choisir un tournoi où les 8 joueurs "
                      "sont chargés pour créer des rounds X")
                os._exit(1)

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                print("Erreur, vous devez choisir un tournoi où les 8 joueurs "
                      "sont chargés pour créer des rounds Y")
                os._exit(0)

            joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
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

            # Liste avec id joueur et classement pour construction round > 1
            # Liste contient l'id, le classement, et un score à 0 pour le moment'
            # Attention, il ne faudra pas réécraser le score avec 0 lors
            # des prochains rounds

            # SI TOURNOI ROUND EN COURS = 1 FAIRE
            list_ja = [round_id_joueur, int(round_class_joueur), 0]
            list_jx.append(list_ja)
            index_joueur = index_joueur + 1

        # print("FIN RECUPERATION DES DONNEES DU JOUEUR")
        # Récupération des scores des joueurs dans le tournoi pour les mettre
        # dans une liste
        # de joueur qui contient, l'id du joueur, son score, son classement
        # les scores s'incrémentent des scores des matchs précédents en utilisant
        # le round en cours
        # pour savoir combien de scores à aller chercher, attention,
        # les joueurs ne sont pas dans le même ordre
        # print("")
        # print("Tournoi_round_en_cours : " + str(Tournoi_round_en_cours))

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

        # print("debut test recherche joueurs déjà affrontés ROUND 2 ET PLUS")
        list_j_opp = [[joueur_class_score_croissant[0][0]],
                      [joueur_class_score_croissant[1][0]],
                      [joueur_class_score_croissant[2][0]],
                      [joueur_class_score_croissant[3][0]],
                      [joueur_class_score_croissant[4][0]],
                      [joueur_class_score_croissant[5][0]],
                      [joueur_class_score_croissant[6][0]],
                      [joueur_class_score_croissant[7][0]]]

        # print("list_j_opp - joueurs triés en fonction de leur score en "
        #         "priorité et de leur classement en second lieu")
        # print(list_j_opp)
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
                        # print(score_matchRx[index_position_impaire][0])
                        index = index_position_impaire + 1
                        list_jy[index_id_jy].append(score_matchRx[index][0])
                        # print(score_matchRx[index_position_impaire+1][0])

                    if list_j_opp[index_id_jy][0] == \
                            score_matchRx[index_position_paire][0]:
                        index = index_position_paire - 1
                        list_jy[index_id_jy].append(score_matchRx[index][0])

                        # print(score_matchRx[index_position_impaire - 1][0])

                    index_position_impaire = index_position_impaire + 2
                    index_position_paire = index_position_paire + 2
                index_id_jy = index_id_jy + 1
                # print(list_jy)

            Tournoi_round_en_cours_temp = Tournoi_round_en_cours_temp - 1
            print("list_jy_joueurs deja affrontés dans les rounds précédents : ")
            print(list_jy)

        # print("Affichage des paires de joueurs par identifiant du round " +
        #       str(Tournoi_round_en_cours))
        liste_paire_1 = []
        liste_paire_1.append(joueur_class_score_croissant[0])
        liste_paire_1.append(joueur_class_score_croissant[1])
        # print(liste_paire_1)

        # print("Paire 1, par ordre de classement et score,
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
        list_jy_temp = list_jy
        # print(list_jy_temp)

        # Tant que les paires crées <= 3, la dernière étant constituée
        # des 2 joueurs restants
        list_jy_temp = list_jy

        list_part = []
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
                        # print()

                    # Si tous les joueurs testés et pas trouvé de déjà rencontré,
                    # le partenaire est ok
                    if test_joueur_affront == 0 and index_nbr_part_affront == \
                        (Tournoi_round_en_cours - 1) and \
                            nbr_part_rest_a_tester != 0:
                        # print("test_joueur_affront  " +
                        #      str(test_joueur_affront))
                        # print("index_nbr_part_affront  " +
                        #      str(index_nbr_part_affront))
                        # print("Tournoi_round_en_cours  " +
                        #      str(Tournoi_round_en_cours))

                        partenaire_libre = joueur_1_test
                    # Si le partenaire testé est le 7ème, on le donne libre même
                    # s'il est déjà rencontré

                    # print("SI - DERNIER PARTENAIRE TESTE, LE METTRE LIBRE, CAR "
                    #       "PLUS LE CHOIX, IL FAUT AFFRONTER UN PARTENAIRE "
                    #       "DEJA AFFRONTE")
                    # print(index_partenaire)
                    # print(nbr_part_rest_a_tester)
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

                        # print("LISTE DE JOUEURS POUR CETTE PAIRE : ")
                        # print(list_part)

                        list_list_part.append(list_part)
                        # print()
                        # print("LISTE DE LISTE DES FUTURES PAIRES DE JOUEURS")
                        # print(list_list_part)
                        # print("liste_jy_temp")
                        # print(list_jy_temp)
                        # print("liste_jy_temp après suppression "
                        #      "des joueurs appairés")
                        list_jy_temp.pop(0)
                        # enlever 1 à l'index, la suppression du joueur ayant
                        # décalé le partenaire à supprimer
                        list_jy_temp.pop(index_partenaire - 1)
                        # print(list_jy_temp)
                        nbr_part_rest_a_tester = nbr_part_rest_a_tester - 2
                        # print("nombre de partenaire restant à tester : " +
                        #       str(nbr_part_rest_a_tester))

                        index_partenaire = 0
                    index_joueur_affront = index_joueur_affront + 1
                    index_nbr_part_affront = index_nbr_part_affront + 1
                index_partenaire = index_partenaire + 1

        print(list_list_part)
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
        print("début heure round : " + str_date_heure_debut)

        liste_round_x = []
        liste_round_x.append(str_date_heure_debut)
        liste_round_x.append(list_paire1_round)
        liste_round_x.append(list_paire2_round)
        liste_round_x.append(list_paire3_round)
        liste_round_x.append(list_paire4_round)
        print()
        print("liste_round" + str(Tournoi_round_en_cours + 1))
        print(liste_round_x)

        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)

        # Test si dernier round du tournoi
        if Tournoi_round_en_cours < int(nb_r):
            Tournoi_round_en_cours = Tournoi_round_en_cours + 1
        else:
            print("Nombre maxi de round atteint !")

        # update la base de donnée
        if Tournoi_round_en_cours <= int(nb_r):

            update_round = ("round_" + str(Tournoi_round_en_cours) + "+match")
            # db_tournois.update({update_round: liste_round_x},
            #                    Todo.id_tournoi == int_tournoi_select)

            ClassTournoi.UpdateRoundTournois(self=True,
                                             nom_donnees=update_round,
                                             donnees=liste_round_x,
                                             numero_tournoi=int_tournoi_select)

            print("nouveau round")
            print(Tournoi_round_en_cours)
            db_tournois.update({"round_en_cours": Tournoi_round_en_cours},
                               Todo.id_tournoi == int_tournoi_select)

        return ()
