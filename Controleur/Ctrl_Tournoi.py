class Class_Tournoi():
    def __init__(self):
        pass

    def creat_new_tournois():
        # identifiant tournoi
        import os
        import datetime
        from Vue.affichage import ClassVueAffichage
        from Modele.Tournoi import ClassModTournoi

        # Appel du Modèle pour création d'un identifiant du tournoi, retourne le prochain identifiant libre
        str_id_libre = ClassModTournoi.CreatIdentifiantTournoi(self=True)
        id_tournoi = int(str_id_libre)

        # Appel Vue pour saisie du nom
        nom = ClassVueAffichage.Input(self=True, texte1="saisie nom :")

        if nom == "":
            nom = ("Tournoi " + str(id_tournoi))
            ClassVueAffichage.Affichage(self=True,
                                        texte1="en absence de nom, "
                                               "le nom par défaut "
                                               "est " + nom,
                                        texte2="",
                                        texte3="")

        if nom == "r":
            nom = ("Tournoi " + str(id_tournoi))
            ClassVueAffichage.Affichage(self=True,
                                        texte1="r est un nom interdit, "
                                               "cela correspond à une "
                                               "commande clavier, "
                                               "le nom par défaut "
                                               "est " + nom,
                                        texte2="", texte3="")
        if nom == "E":
            nom = ("Tournoi " + str(id_tournoi))
            ClassVueAffichage.Affichage(self=True,
                                        texte1="E est un nom interdit, "
                                               "cela correspond à une commande"
                                               " clavier, le nom par défaut "
                                               "enregistré est " + nom,
                                        texte2="",
                                        texte3="")

        lieu = ClassVueAffichage.Input(self=True, texte1="saisie lieu :")

        # Appel Vue pour saisie du lieu
        if lieu == "":
            lieu = ("Lieu " + str(id_tournoi))

        date = ClassVueAffichage.Input(self=True,
                                       texte1="date (format DD/MM/YYYY): ")

        # Appel du Vue pour saisie de la date
        if date == "":
            date_heure = datetime.datetime.now()
            str_date_heure = str(date_heure)
            char = '.'
            PositChar = str_date_heure.find(char)
            str_date_heure = str_date_heure[0:(PositChar - 9)]
            date = str_date_heure

        # Appel du Vue pour saisie du nombre de rounds
        nbr_rounds = ClassVueAffichage.Input(self=True,
                                             texte1="saisie nombre de rounds, "
                                                    "4 rounds si pas de saisie "
                                                    "ou erreur de saisie: ")

        if nbr_rounds == "":
            nbr_rounds = "4"
        try:
            int_nbr_rounds = int(nbr_rounds)
        except ValueError:
            ClassVueAffichage.Affichage(self=True, texte1="Nombre de round "
                                                          "max = 7, mini = 1, "
                                                          "4 par défaut",
                                        texte2="",
                                        texte3="")
            int_nbr_rounds = 4
            nbr_rounds = "4"

        if int_nbr_rounds > 7 or int_nbr_rounds < 1:
            ClassVueAffichage.Affichage(self=True,
                                        texte1="Nombre de round max = 7, "
                                               "mini = 1, 4 par défaut",
                                        texte2="",
                                        texte3="")
            nbr_rounds = "4"

        id_j1 = ""; id_j2 = ""; id_j3 = ""; id_j4 = ""; id_j5 = ""; id_j6 = ""; id_j7 = ""; id_j8 = ""
        round_1 = ""; round_2 = ""; round_3 = ""; round_4 = ""; round_5 = ""; round_6 = ""; round_7 = ""

        # saisie du type de matchs, bullet, blitz, ou coup rapide
        temps_matchs = ""
        saisie = ""
        list_tps = {1: "bullet", 2: "blitz", 3: "coup rapide"}
        while saisie != "1" and saisie != "2" and saisie != "3":
            # Appel du modèle Vue pour saisie type de temps du match
            saisie = ClassVueAffichage.Input(self=True,
                                             texte1="saisie type de match "
                                                    ": \"1\" pour bullet, "
                                                    "\"2\"pour blitz,\"3\""
                                                    "pour coup rapide. "
                                                    "E pour stopper le programme")
            if saisie == "E":
                os._exit(0)
        else:
            temps_matchs = list_tps[int(saisie)]

        print(temps_matchs)
        print()

        # appel vue pour saisie des remarques générale organisateur
        remarque_tournoi = ClassVueAffichage.Input(self=True,
                                                   texte1="saisie des remarques "
                                                          "de l'organisateur "
                                                          "du tournoi :")
        print()
        # Appel du modele tournoi pour Serialisation et enregistrement des données dans la base
        ClassModTournoi.CreatNewTournois(self=True, id_tournoi = id_tournoi, nom=nom, lieu=lieu, date=date,
                                         nbr_rounds=nbr_rounds, id_j1=id_j1, id_j2=id_j2, id_j3=id_j3, id_j4=id_j4,
                                         id_j5=id_j5, id_j6=id_j6, id_j7=id_j7, id_j8=id_j8, round_1=round_1,
                                         round_2=round_2, round_3=round_3, round_4=round_4, round_5=round_5,
                                         round_6=round_6, round_7=round_7, temps_matchs=temps_matchs,
                                         remarque_tournoi=remarque_tournoi)
        return ()

    def lect_tournois():
        from Modele.Tournoi import ClassModTournoi
        # Appel du modèle tournoi pour récupérer le liste des tournois
        tournois=ClassModTournoi.AffichageTournois(self=True)
        index = 0
        for i in tournois:
            print(tournois[index])
            print()
            index = index + 1
        return ()

    # supprimer un tournoi de la liste pour éventuellement le ressaisir
    def sup_tournois(menu_niv_2):
        from Modele.Tournoi import ClassModTournoi
        if menu_niv_2.isdigit():
            id_tournoi_del = int(menu_niv_2)
            ClassModTournoi.SupprimTournois(self=True, numero_tournoi= id_tournoi_del)
        else:
            print("le numéro de tournoi doit être un nombre")

    def purge_tournois():
        from Modele.Tournoi import ClassModTournoi
        ClassModTournoi.PurgeTournois()

    def charge_joueurs_tournoi():
        import os
        from Controleur.fonctions import ClassFonctions
        from Vue.affichage import ClassVueAffichage
        from Modele.Tournoi import ClassModTournoi

        # Appel de la fonction de sélection du tournoi
        id_tournoi_select = ClassFonctions.select_tournoi()
        # Appel de la méthode vue du modèle VMC pour affichage de la
        # résultante de la base de données
        str_poubl = ""
        str_poubl = "Chargement des joueurs dans le tournoi " + id_tournoi_select
        ClassVueAffichage.Affichage(self=True, texte1=str_poubl, texte2="", texte3="")
        str_poubl = ""
        list_joueurs = []

        index = 0
        # Appel du modèle pour mise à disposition de la liste des joueurs de la base de donnée.
        from Modele.Joueurs import ClassJoueursModel
        serie_joueurs = ClassJoueursModel.MisADispoJoueurChargTournoi(self=True)
        str_joueurs = str(serie_joueurs)


        # Création d'une liste temporaire de joueurs
        char = "{"
        joueur_cherche = 1
        index = 1
        for i in serie_joueurs:
            index = index + 1
            # Extraction de l'id
            char = 'id_joueur'
            PositDebNbre = (str_joueurs.find(char))
            char = "Nom"
            PositFinNbre = (str_joueurs.find(char))
            id_joueur = str_joueurs[(PositDebNbre + 12): (PositFinNbre - 3)]

            # Supprimer le 1er joueur traité de la trame du dictionnaire car il ne peut être chargé deux fois
            char = '}'
            PositDebNbre = (str_joueurs.find(char))
            str_joueurs = str_joueurs[(PositDebNbre + 2):-1]
            list_joueurs.append(id_joueur)
            joueur_cherche = joueur_cherche + 1

        # Appel de la méthode vue du modèle VMC pour affichage de la
        # résultante de la base de données
        ClassVueAffichage.Affichage(self=True,
                                    texte1="liste Id joueurs",
                                    texte2=list_joueurs, texte3="")

        # Faire input de l'id, comparer avec les id de la liste,
        # si id de la liste, mettre
        # dans le tournoi à l'emplacement de l'id 1 au début, et supprimer
        # l'élément de la liste
        # sinon, forcer à ressaisir jusqu'à un id correct
        # if id pas dans la liste, afficher messsage defaut et recommmencer
        # sinon le charger dans le Tournoi et le supprimer de la liste,
        # puis reproposer la liste pour le prochain joueur à charger
        joueur_a_charger = 1
        while (joueur_a_charger < 9):
            # saisie d'un Id de joueur existant pour le joueur n°"
            str_poubl = "saisie Id ou n° de joueur existant pour le joueur n°" + str(joueur_a_charger)
            id_a_charger = ClassVueAffichage.Input(self=True, texte1=str_poubl)

            if id_a_charger == "E" or id_a_charger == "e":
                os._exit(0)

            if id_a_charger in list_joueurs:
                # Appel de la méthode vue du modèle VMC pour affichage de la
                # résultante de la base de données
                str_poubl = "joueur n°" + id_a_charger + " sélectionné pour le tournoi"
                ClassVueAffichage.Affichage(self=True, texte1=str_poubl, texte2="", texte3="")

                list_joueurs.remove(id_a_charger)
                str_list_joueurs = str(list_joueurs)
                str_list_joueurs = str_list_joueurs.replace('[', '')
                str_list_joueurs = str_list_joueurs.replace('\',', ' -')
                str_list_joueurs = str_list_joueurs.replace('\']', '')
                str_list_joueurs = str_list_joueurs.replace('\'', 'joueur n°')

                ClassVueAffichage.Affichage(self=True,
                                            texte1="liste des numéros des "
                                                   "joueurs non sélectionnés :",
                                            texte2=str_list_joueurs,
                                            texte3="")

                # Sélection du joueur de la table tournoi à charger
                id_jx = ("id_j" + str(joueur_a_charger))

                id_tournoi_select = int(id_tournoi_select)

                # Appel du modèle pour charger le joueur dans la base de données du tournoi
                ClassModTournoi.UpdateJoueurTournois(self=True,
                                                  nom_donnees=id_jx,
                                                  donnees=id_a_charger,
                                                  numero_tournoi=id_tournoi_select)

                joueur_a_charger = joueur_a_charger + 1

            else:
                ClassVueAffichage.Affichage(self=True,
                                            texte1="n° de joueur absent de la "
                                                   "liste des joueurs ou déjà"
                                                   " sélectionné pour le tournoi",
                                            texte2="",
                                            texte3="")

    def lecture_match_tournoi(self):
        # Récupération des informations du fichier JSON du tournoi
        # pour créer les rounds
        import os
        from tinydb import TinyDB, where
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        db_tournois = TinyDB('tournois.json')

        tournoi_select = ClassVueAffichage.Input(self=True,
                                                 texte1="saisie Id du tournoi "
                                                        "pour lequel on veut "
                                                        "le résultat des matchs")
        tournoi_trouv = ClassFonctions.tournoi_exist(id_tournoi_select=tournoi_select)
        if tournoi_trouv == []:
            print("Numéro de tournoi introuvable")
            os._exit(0)
        int_tournoi_select = int(tournoi_select)

        # charger le tournoi selectionné à partir de la base de données tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

        try:
            score_round1 = (tournoi[0]['ScoreMatchRound1'])
            print("Score round 1 - ID joueur + score : " + str(score_round1[0]) + str(score_round1[1]))
            print("Score round 1 - ID joueur + score : " + str(score_round1[2]) + str(score_round1[3]))
            print("Score round 1 - ID joueur + score : " + str(score_round1[4]) + str(score_round1[5]))
            print("Score round 1 - ID joueur + score : " + str(score_round1[6]) + str(score_round1[7]))
            print()
        except KeyError:
            print("pas de score pour le round 1")

        try:
            score_round2 = (tournoi[0]['ScoreMatchRound2'])
            print("Score round 2 - ID joueur + score : " + str(score_round2[0]) + str(score_round2[1]))
            print("Score round 2 - ID joueur + score : " + str(score_round2[2]) + str(score_round2[3]))
            print("Score round 2 - ID joueur + score : " + str(score_round2[4]) + str(score_round2[5]))
            print("Score round 2 - ID joueur + score : " + str(score_round2[6]) + str(score_round2[7]))
            print()
        except KeyError:
            print("pas de score pour le round 2")

        try:
            score_round3 = (tournoi[0]['ScoreMatchRound3'])
            print("Score round 3 - ID joueur + score : " + str(score_round3[0]) + str(score_round3[1]))
            print("Score round 3 - ID joueur + score : " + str(score_round3[2]) + str(score_round3[3]))
            print("Score round 3 - ID joueur + score : " + str(score_round3[4]) + str(score_round3[5]))
            print("Score round 3 - ID joueur + score : " + str(score_round3[6]) + str(score_round3[7]))
            print()
        except KeyError:
            print("pas de score pour le round 3")

        try:
            score_round4 = (tournoi[0]['ScoreMatchRound4'])
            print("Score round 4 - ID joueur + score : " + str(score_round4[0]) + str(score_round4[1]))
            print("Score round 4 - ID joueur + score : " + str(score_round4[2]) + str(score_round4[3]))
            print("Score round 4 - ID joueur + score : " + str(score_round4[4]) + str(score_round4[5]))
            print("Score round 4 - ID joueur + score : " + str(score_round4[6]) + str(score_round4[7]))
            print()
        except KeyError:
            print("pas de score pour le round 4")

        try:
            score_round5 = (tournoi[0]['ScoreMatchRound5'])
            print("Score round 5 - ID joueur + score : " + str(score_round5[0]) + str(score_round5[1]))
            print("Score round 5 - ID joueur + score : " + str(score_round5[2]) + str(score_round5[3]))
            print("Score round 5 - ID joueur + score : " + str(score_round5[4]) + str(score_round5[5]))
            print("Score round 5 - ID joueur + score : " + str(score_round5[6]) + str(score_round5[7]))
            print()
        except KeyError:
            print("pas de score pour le round 5")
            print()

    def lecture_round_tournoi(self):
        # Récupération des informations du fichier JSON du tournoi
        # pour créer les rounds
        import os
        from tinydb import TinyDB, where
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        db_tournois = TinyDB('tournois.json')

        tournoi_select = ClassVueAffichage.Input(self=True,
                                                 texte1="saisie Id du tournoi "
                                                        "pour lequel on veut "
                                                        "afficher les rounds")
        tournoi_trouv = ClassFonctions.tournoi_exist(tournoi_select)
        if tournoi_trouv == []:
            print("Numéro de tournoi introuvable")
            os._exit(0)

        int_tournoi_select = int(tournoi_select)

        # charger le tournoi sélectionné à partir de la base
        # de données dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

        # ROUND 1
        # Extraction de round 1 de la base de donnée
        round1 = ""
        try:
            round1 = (tournoi[0]['round_1+match'])
            try:
                print("Round 1 - Date du tournoi : " + str(round1[0]))
                print()
            except IndexError:
                print("pas de round 1 créé")
            index = 1
            if round1 != "":
                while index < 5:
                    str_poubl = "Round 1 - Paire" + str(index) + " - Joueur 1 : " + "ID : "
                    str_poubl = str_poubl + str(round1[index][0][0]) + " - "
                    str_poubl = str_poubl + str(round1[index][0][2]) + " - : "
                    str_poubl = str_poubl + str(round1[index][0][3])
                    print(str_poubl)
                    str_poubl = ""

                    str_poubl = "Round 1 - Paire" + str(index) + " - Joueur 2 : " + "ID : "
                    str_poubl = str_poubl + str(round1[index][1][0]) + " - "
                    str_poubl = str_poubl + str(round1[index][1][2]) + " - : "
                    str_poubl = str_poubl + str(round1[index][1][3])
                    print(str_poubl)
                    str_poubl = ""
                    index = index + 1
                    print()
        except KeyError:
            print("pas de round créé pour le round 1")

        # ROUND 2 ET PLUS
        index_round = 2
        while index_round < 6:
            round_bd = "round_" + str(index_round) + "+match"
            roundx = (tournoi[0][round_bd])
            try:
                print("Round" + str(index_round) + " - Date du tournoi : " + str(roundx[0]))

                index = 1
                while index < 5:
                    str_poubl = "Round" + str(index_round) + " - Paire" + str(index)
                    print(str_poubl + " - Joueur 1 : " + "ID : " + str(roundx[index][0]))
                    str_poubl = ""

                    str_poubl = "Round" + str(index_round) + " - Paire" + str(index)
                    print(str_poubl + " - Joueur 2 : " + "ID : " + str(roundx[index][1]))
                    str_poubl = ""
                    index = index + 1
                    print()
            except IndexError:
                print("pas de round " + str(index_round) + "créé")
            index_round = index_round + 1
        print()

    def lecture_joueur_tournoi(self):
        # Récupération des informations du fichier JSON du tournoi
        # pour créer les rounds
        import os
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        from tinydb import TinyDB, where
        db_tournois = TinyDB('tournois.json')

        tournoi_select = ClassVueAffichage.Input(self=True,
                                                 texte1="saisie Id tournoi "
                                                        "pour lequel on veut "
                                                        "afficher les joueurs")

        tournoi_trouv = ClassFonctions.tournoi_exist(tournoi_select)
        if tournoi_trouv == []:
            print("Numéro de tournoi introuvable")
            os._exit(0)

        int_tournoi_select = int(tournoi_select)

        # charger le tournoi sélectionné à partir de la base de données tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        id_j1 = (tournoi[0]['id_j1'])
        id_j2 = (tournoi[0]['id_j2'])
        id_j3 = (tournoi[0]['id_j3'])
        id_j4 = (tournoi[0]['id_j4'])
        id_j5 = (tournoi[0]['id_j5'])
        id_j6 = (tournoi[0]['id_j6'])
        id_j7 = (tournoi[0]['id_j7'])
        id_j8 = (tournoi[0]['id_j8'])

        db_joueurs = TinyDB('joueurs.json')
        # charger le tournoi sélectionné à partir de la base de données tournoi

        joueur_charge = "False"
        # Joueur 1
        try:
            joueur1 = (db_joueurs.search(where('id_joueur') == int(id_j1)))
        except ValueError:
            print("pas de joueur 1 chargé dans le tournoi")

        # Joueur 2
        try:
            joueur2 = (db_joueurs.search(where('id_joueur') == int(id_j2)))
        except ValueError:
            print("pas de joueur 2 chargé dans le tournoi")

        # Joueur 3
        try:
            joueur3 = (db_joueurs.search(where('id_joueur') == int(id_j3)))
        except ValueError:
            print("pas de joueur 3 chargé dans le tournoi")

        # Joueur 4
        try:
            joueur4 = (db_joueurs.search(where('id_joueur') == int(id_j4)))
        except ValueError:
            print("pas de joueur 4 chargé dans le tournoi")

        # Joueur 5
        try:
            joueur5 = (db_joueurs.search(where('id_joueur') == int(id_j5)))
        except ValueError:
            print("pas de joueur 5 chargé dans le tournoi")
        # Joueur 6
        try:
            joueur6 = (db_joueurs.search(where('id_joueur') == int(id_j6)))
        except ValueError:
            print("pas de joueur 6 chargé dans le tournoi")

        # Joueur 7
        try:
            joueur7 = (db_joueurs.search(where('id_joueur') == int(id_j7)))
        except ValueError:
            print("pas de joueur 7 chargé dans le tournoi")
        # Joueur 8
        try:
            joueur8 = (db_joueurs.search(where('id_joueur') == int(id_j8)))
            joueur_charge = "True"
        except ValueError:
            print("pas de joueur 8 chargé dans le tournoi")
            joueur_charge = "False"

        if joueur_charge == "True":
            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur1)

            str_poubl = "JOUEUR 1 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur2)
            str_poubl = "JOUEUR 2 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur3)
            str_poubl = "JOUEUR 3 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur4)
            str_poubl = "JOUEUR 4 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur5)
            str_poubl = "JOUEUR 5 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur6)
            str_poubl = "JOUEUR 6 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur7)
            str_poubl = "JOUEUR 7 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur8)
            str_poubl = "JOUEUR 8 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

    def lecturetournoi(self):
        # Récupération des informations du fichier JSON du tournoi pour
        # créer les rounds
        from tinydb import TinyDB
        db_tournois = TinyDB('tournois.json')
        str_poubl = ""
        serialised_tournois = db_tournois.all()
        print()
        index = 0
        for i in serialised_tournois:
            str_poubl = "ID tournoi n°" + str(serialised_tournois[index]['id_tournoi'])
            str_poubl = str_poubl + ",   appelé " + str(serialised_tournois[index]['nom'])
            str_poubl = str_poubl + (", qui s'est passé à " + str(serialised_tournois[index]['lieu']))
            print(str_poubl + (", en date du " + str(serialised_tournois[index]['date du tournoi'])))
            str_poubl = ""
            print()
            index = index + 1

    def liste_joueur_tournoi(joueur):
        from Controleur.fonctions import ClassFonctions
        dict_joueur1 = ClassFonctions.creat_dict(donnees_db=joueur)
        id_j = (dict_joueur1["id_joueur"])
        nom_j = (dict_joueur1["Nom"])
        prenom_j = (dict_joueur1["Prenom"])
        date_j = (dict_joueur1["date de naissance"])
        sexe_j = (dict_joueur1["sexe"])
        classement_j = (dict_joueur1["Classement"])
        return (id_j, nom_j, prenom_j, date_j, sexe_j, classement_j)

    def lecture_joueur_tournoi_class(self):
        import os
        from Vue.affichage import ClassVueAffichage
        from Controleur.fonctions import ClassFonctions
        # Récupération des informations du fichier JSON du tournoi
        # pour créer les rounds
        from tinydb import TinyDB, where
        db_tournois = TinyDB('tournois.json')
        print(db_tournois)
        tournoi_select = ClassVueAffichage.Input(self=True,
                                                 texte1="saisie Id tournoi "
                                                        "pour lequel on veut "
                                                        "afficher les joueurs")
        tournoi_trouv = ClassFonctions.tournoi_exist(tournoi_select)
        if tournoi_trouv == []:
            print("Numéro de tournoi introuvable")
            os._exit(0)

        int_tournoi_select = int(tournoi_select)

        # charger le tournoi sélectionné à partir de la base de données tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        id_j1 = (tournoi[0]['id_j1'])
        id_j2 = (tournoi[0]['id_j2'])
        id_j3 = (tournoi[0]['id_j3'])
        id_j4 = (tournoi[0]['id_j4'])
        id_j5 = (tournoi[0]['id_j5'])
        id_j6 = (tournoi[0]['id_j6'])
        id_j7 = (tournoi[0]['id_j7'])
        id_j8 = (tournoi[0]['id_j8'])
        db_joueurs = TinyDB('joueurs.json')
        # charger le tournoi sélectionné à partir de la base de données tournoi
        liste_joueurc_tournoi = []
        joueur_charge = "False"
        # Joueur 1
        try:
            joueur1 = (db_joueurs.search(where('id_joueur') == int(id_j1)))
            liste_joueurc_tournoi.append(joueur1)
        except ValueError:
            print("pas de joueur 1 chargé dans le tournoi")

        # Joueur 2
        try:
            joueur2 = (db_joueurs.search(where('id_joueur') == int(id_j2)))
            liste_joueurc_tournoi.append(joueur2)
        except ValueError:
            print("pas de joueur 2 chargé dans le tournoi")

        # Joueur 3
        try:
            joueur3 = (db_joueurs.search(where('id_joueur') == int(id_j3)))
            liste_joueurc_tournoi.append(joueur3)
        except ValueError:
            print("pas de joueur 3 chargé dans le tournoi")

        # Joueur 4
        try:
            joueur4 = (db_joueurs.search(where('id_joueur') == int(id_j4)))
            liste_joueurc_tournoi.append(joueur4)
        except ValueError:
            print("pas de joueur 4 chargé dans le tournoi")

        # Joueur 5
        try:
            joueur5 = (db_joueurs.search(where('id_joueur') == int(id_j5)))
            liste_joueurc_tournoi.append(joueur5)
        except ValueError:
            print("pas de joueur 5 chargé dans le tournoi")
        # Joueur 6
        try:
            joueur6 = (db_joueurs.search(where('id_joueur') == int(id_j6)))
            liste_joueurc_tournoi.append(joueur6)
        except ValueError:
            print("pas de joueur 6 chargé dans le tournoi")

        # Joueur 7
        try:
            joueur7 = (db_joueurs.search(where('id_joueur') == int(id_j7)))
            liste_joueurc_tournoi.append(joueur7)
        except ValueError:
            print("pas de joueur 7 chargé dans le tournoi")
        # Joueur 8
        try:
            joueur8 = (db_joueurs.search(where('id_joueur') == int(id_j8)))
            liste_joueurc_tournoi.append(joueur8)
            joueur_charge = "True"
        except ValueError:
            print("pas de joueur 8 chargé dans le tournoi")
            joueur_charge = "False"

        if joueur_charge == "True":
            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur1)

            str_poubl = "JOUEUR 1 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur2)
            str_poubl = "JOUEUR 2 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur3)
            str_poubl = "JOUEUR 3 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur4)
            str_poubl = "JOUEUR 4 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur5)
            str_poubl = "JOUEUR 5 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur6)
            str_poubl = "JOUEUR 6 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur7)
            str_poubl = "JOUEUR 7 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = Class_Tournoi.liste_joueur_tournoi(joueur8)
            str_poubl = "JOUEUR 8 DU TOURNOI : Identifiant n°" + str(id_j) + " - "
            str_poubl = str_poubl + str(nom_j) + " - " + str(prenom_j) + " - "
            print(str_poubl + str(date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))
            str_poubl = ""

            dict_joueurs = ClassFonctions.creat_dict(donnees_db=liste_joueurc_tournoi)
            print(dict_joueurs)

            from operator import itemgetter
            joueur_class_croissant = (sorted(dict_joueurs, key=itemgetter("Nom"), reverse=False))

            print("Affichage des joueurs classés par nom")
            index = 0
            for i in joueur_class_croissant:
                print(joueur_class_croissant[index])
                index = index + 1
            print()

            print("Affichage des joueurs par classement croissant du tournoi")
            joueur_class_croissant = (sorted(dict_joueurs, key=itemgetter("Classement"), reverse=False))
            index = 0
            for i in joueur_class_croissant:
                print(joueur_class_croissant[index])
                index = index + 1
            print()
