class ClassFonctions():
    def __init__(self):
        pass

    def creat_dict(donnees_db):
        import os
        str_donnees = str(donnees_db)
        str_donnees = str_donnees.replace("[", "")
        str_donnees = str_donnees.replace("]", "")

        import ast
        try:
            dict_donnees = ast.literal_eval(str_donnees)

        except SyntaxError:
            print("")
            print("Le tournoi est déjà chargé avec des rounds, "
                  "supprimer et recréer ce tournoi pour le recharger")
            os._exit(0)
        return (dict_donnees)

    def tournoi_exist(id_tournoi_select):
        import os
        from tinydb import TinyDB, where
        # verif si tournoi existe, renvoie le numero du tournoi si existe
        # sinon, sort du prog en affichant un message
        db_tournois = TinyDB('tournois.json')

        int_tournoi_select = int(id_tournoi_select)

        # charger le tournoi selectionné à partir de la table dans tournoi
        try:
            trouve_tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        except KeyError:
            trouve_tournoi = ""
            print("tournoi introuvable ")
            os._exit(0)
        return (trouve_tournoi)

    def creat_list(donnees_db):
        str_donnees = str(donnees_db)
        str_donnees = str_donnees.replace("{", "")
        str_donnees = str_donnees.replace("}", "")
        liste_donnees = str_donnees
        return (liste_donnees)

    def select_tournoi():
        import os
        from tinydb import TinyDB
        from Vue.affichage import ClassVueAffichage
        db_tournois = TinyDB('tournois.json')
        id_tournoi_select = ""
        list_tournoi = []
        str_poubl = ""
        # SELECTION DU TOURNOI
        serialised_tournoi = db_tournois.all()
        str_tournoi = str(serialised_tournoi)
        tournoi_cherche = 1
        index = 1
        for i in serialised_tournoi:
            index = index + 1  # A SUPPRIMER

            # Extraction de l'id
            char = 'id_tournoi'
            PositDebNbre = (str_tournoi.find(char))
            char = "nom"
            PositFinNbre = (str_tournoi.find(char))
            id_tournoi = str_tournoi[(PositDebNbre + 13): (PositFinNbre - 3)]
            # Supprimer le 1er tournoi traité de la trame du dictionnaire
            char = '}'
            PositDebNbre = (str_tournoi.find(char))
            str_tournoi = str_tournoi[(PositDebNbre + 2):-1]
            list_tournoi.append(id_tournoi)

            tournoi_cherche = tournoi_cherche + 1

        str_list_tournoi = str(list_tournoi)
        str_list_tournoi = str_list_tournoi.replace('[', '')
        str_list_tournoi = str_list_tournoi.replace('\',', ' -')
        str_list_tournoi = str_list_tournoi.replace('\']', '')
        str_list_tournoi = str_list_tournoi.replace('\'', 'tournoi n°')

        # Appel de la méthode vue du modèle VMC pour affichage de la résultante
        # de la base de données
        ClassVueAffichage.Affichage(self=True,
                                    texte1="",
                                    texte2="liste des numéros de tournois dans"
                                           " la base de donnée qu'il est possible"
                                           " de sélectionner :",
                                    texte3=str_list_tournoi + "\n")

        tournoi_a_charger = 1
        while (tournoi_a_charger < 2):
            # saisie d'un Id de joueur existant pour le joueur
            id_a_charger = ClassVueAffichage.Input(self=True,
                                                   texte1="saisie Id ou n° du tournoi existant "
                                                          "à sélectionner")

            if id_a_charger == "E" or id_a_charger == "e":
                print("E = commande pour sortir du prog")
                os._exit(0)

            # Vérification que le tournoi est bien dans la liste des tournois
            if id_a_charger in list_tournoi:
                tournoi_a_charger = tournoi_a_charger + 1
                list_tournoi.remove(id_a_charger)
                id_tournoi_select = id_a_charger

                # Appel de la méthode vue du modèle VMC pour affichage de
                # la résultante de la base de données
                str_poubl = ("Le tournoi " + id_tournoi_select + " est sélectionné")
                ClassVueAffichage.Affichage(self=True, texte1="",
                                            texte2=str_poubl,
                                            texte3="")
                str_poubl = ""

            else:
                # Appel de la méthode vue du modèle VMC pour affichage de la
                # résultante de la base de données
                ClassVueAffichage.Affichage(self=True,
                                            texte1="Ce tournoi n'est pas dans la"
                                                   " liste des tournois existants,"
                                                   " re-saisir un tournoi de "
                                                   "la liste",
                                            texte2="",
                                            texte3="")
        return (id_tournoi_select)
