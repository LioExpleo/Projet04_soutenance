from Controleur.Ctrl_Tournoi import select_tournoi
from Controleur.fonctions import creat_dict
from datetime import datetime
import os

class ClassRound:
    def __init__(self, nom="Num_round", date_heure_debut="",date_heure_fin="", id_j1="", id_j2="", id_j3="", id_j4="", id_j5="", id_j6="", id_j7="", id_j8=""):
        #nom entré à la main Round numero de round sinon
        #date et heure de début récupéré automatiquement à la création du tour
        #date et heure de fin récupéré automatiquement quand l'utilisateur indique le tour terminé
        self.nom = nom
        self.date_heure_debut=date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.id_tournoi = id_tournoi
        self.id_j1 = id_j1
        self.id_j2 = id_j2
        self.id_j3 = id_j3
        self.id_j4 = id_j4
        self.id_j5 = id_j5
        self.id_j6 = id_j6
        self.id_j7 = id_j7
        self.id_j8 = id_j8

    def DonneesRound1(self, liste_paire_1,liste_paire_2,liste_paire_3,liste_paire_4):






      # Permet la création de tous les joueurs un par un, ils seront mis dans la bd par le contrôleur ou directement ici
'''
    def CreatRound_1(self):
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatRound_1")
        liste_liste_class_joueur = []
        #select_tournoi=""
        tournoi_select=select_tournoi()
        print ("Prochain round tournoi selectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        #charger le tournoi selectionné à partir de la table dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        #transformation de tournoi en dictionnaire pour aller chercher les éléments voulus
        #nombre de rounds et id des 8 joueurs
        dict_tournoi=creat_dict(tournoi)
        print("nombre de rounds")
        print(dict_tournoi["nombre de rounds"])

        db_joueurs = TinyDB('joueurs.json')
        index_joueur=1
        while (index_joueur<9):
            id_jx = "id_j" + str(index_joueur)
            print("id_joueur " + str(index_joueur)+ ": ")
            id_joueur_en_cours=""
            int_id_joueur_en_cours=""
            try:
                id_joueur_en_cours = (dict_tournoi[id_jx])
            except ValueError:
                print("Vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit()

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                print("Erreur, vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit(0)

            joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
            dict_joueur = creat_dict(joueur)
            #print(dict_joueur)
            print ("identifiant joueur :")
            round_id_joueur=(dict_joueur["id_joueur"])
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
            round_class_joueur=(dict_joueur["Classement"])
            print(round_class_joueur)

            liste_class_joueur =[round_id_joueur,int(round_class_joueur), round_nom_joueur,round_prenom_joueur]
            print ("liste : id_joueur, classement joueur, nom, prenom")
            print(liste_class_joueur)
            liste_liste_class_joueur.append(liste_class_joueur)
            print (liste_liste_class_joueur)


            index_joueur = index_joueur + 1


            print("FIN RECUPERATION DES DONNEES DU JOUEUR")
        print("liste_liste_class_joueur : ")
        print(liste_liste_class_joueur)

        from operator import itemgetter
        print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur, key=itemgetter(1),reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
        print(joueur_class_decroissant)

        #Mise en ordre des joueurs par classment, le classment étant la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=False))
        print("Affichage joueur par classement croissant")
        print(joueur_class_croissant)

        print("Affichage des paires de joueurs par identifiant du round 1 \n")
        liste_paire_1=[]
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])
        #print(liste_paire_1)
        print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
        print("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]) + " , Prénom : " + str(liste_paire_1[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]) + " , Prénom : " + str(liste_paire_1[1][3]))
        print()

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        #print(liste_paire_2)
        print("Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        print("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]) + " , Prénom : " + str(
            liste_paire_2[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]) + " , Prénom : " + str(
            liste_paire_2[1][3]))
        print()

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        #print(liste_paire_3)
        print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        print("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]) + " , Prénom : " + str(liste_paire_3[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]) + " , Prénom : " + str(
            liste_paire_3[1][3]))
        print()

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        #print(liste_paire_4)
        print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        print("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]) + " , Prénom : " + str(
            liste_paire_4[0][3]))
        print("ID")
        print("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]) + " , Prénom : " + str(
            liste_paire_4[1][3]))
        print()
        print("********** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ********************")


        nom = input("saisie nom du Round, Round 1 si pas de saisie:\n")
        if (nom == ""):
            nom = "Round 1"

        date_heure_debut = datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print ("début heure round : " + str_date_heure_debut)

        print("********* FIN CREATION ROUND 1 *************************")

    def CreatRound_1(self):
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatRound_1")
        liste_liste_class_joueur = []
        #select_tournoi=""
        tournoi_select=select_tournoi()
        print ("Prochain round tournoi selectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        #charger le tournoi selectionné à partir de la table dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        #transformation de tournoi en dictionnaire pour aller chercher les éléments voulus
        #nombre de rounds et id des 8 joueurs
        dict_tournoi=creat_dict(tournoi)
        print("nombre de rounds")
        print(dict_tournoi["nombre de rounds"])

        db_joueurs = TinyDB('joueurs.json')
        index_joueur=1
        while (index_joueur<9):
            id_jx = "id_j" + str(index_joueur)
            print("id_joueur " + str(index_joueur)+ ": ")
            id_joueur_en_cours=""
            int_id_joueur_en_cours=""
            try:
                id_joueur_en_cours = (dict_tournoi[id_jx])
            except ValueError:
                print("Vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit()

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                print("Erreur, vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit(0)

            joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
            dict_joueur = creat_dict(joueur)
            #print(dict_joueur)
            print ("identifiant joueur :")
            round_id_joueur=(dict_joueur["id_joueur"])
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
            round_class_joueur=(dict_joueur["Classement"])
            print(round_class_joueur)

            liste_class_joueur =[round_id_joueur,int(round_class_joueur), round_nom_joueur,round_prenom_joueur]
            print ("liste : id_joueur, classement joueur, nom, prenom")
            print(liste_class_joueur)
            liste_liste_class_joueur.append(liste_class_joueur)
            print (liste_liste_class_joueur)


            index_joueur = index_joueur + 1


            print("FIN RECUPERATION DES DONNEES DU JOUEUR")
        print("liste_liste_class_joueur : ")
        print(liste_liste_class_joueur)

        from operator import itemgetter
        print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur, key=itemgetter(1),reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
        print(joueur_class_decroissant)

        #Mise en ordre des joueurs par classment, le classment étant la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=False))
        print("Affichage joueur par classement croissant")
        print(joueur_class_croissant)

        print("Affichage des paires de joueurs par identifiant du round 1 \n")
        liste_paire_1=[]
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])
        #print(liste_paire_1)
        print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
        print("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]) + " , Prénom : " + str(liste_paire_1[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]) + " , Prénom : " + str(liste_paire_1[1][3]))
        print()

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        #print(liste_paire_2)
        print("Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        print("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]) + " , Prénom : " + str(
            liste_paire_2[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]) + " , Prénom : " + str(
            liste_paire_2[1][3]))
        print()

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        #print(liste_paire_3)
        print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        print("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]) + " , Prénom : " + str(liste_paire_3[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]) + " , Prénom : " + str(
            liste_paire_3[1][3]))
        print()

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        #print(liste_paire_4)
        print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        print("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]) + " , Prénom : " + str(
            liste_paire_4[0][3]))
        print("ID")
        print("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]) + " , Prénom : " + str(
            liste_paire_4[1][3]))
        print()
        print("********** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ********************")


        nom = input("saisie nom du Round, Round 1 si pas de saisie:\n")
        if (nom == ""):
            nom = "Round 1"

        date_heure_debut = datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print ("début heure round : " + str_date_heure_debut)

        print("********* FIN CREATION ROUND 1*************************")

    def CreatRound_xx(self):
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatRound_1")
        liste_liste_class_joueur = []
        #select_tournoi=""
        tournoi_select=select_tournoi()
        print ("Prochain round tournoi selectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        #charger le tournoi selectionné à partir de la table des tournois
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        #transformation de tournoi en dictionnaire pour aller chercher les éléments voulus
        #nombre de rounds et id des 8 joueurs
        dict_tournoi=creat_dict(tournoi)
        print("nombre de rounds")
        print(dict_tournoi["nombre de rounds"])

        db_joueurs = TinyDB('joueurs.json')
        index_joueur=1
        while (index_joueur<9):
            id_jx = "id_j" + str(index_joueur)
            print("id_joueur " + str(index_joueur)+ ": ")
            id_joueur_en_cours=""
            int_id_joueur_en_cours=""
            try:
                id_joueur_en_cours = (dict_tournoi[id_jx])
            except ValueError:
                print("Vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit()

            try:
                int_id_joueur_en_cours = int(id_joueur_en_cours)
            except ValueError:
                print("Erreur, vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                os._exit(0)

            joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
            dict_joueur = creat_dict(joueur)
            #print(dict_joueur)
            print ("identifiant joueur :")
            round_id_joueur=(dict_joueur["id_joueur"])
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
            round_class_joueur=(dict_joueur["Classement"])
            print(round_class_joueur)

            liste_class_joueur =[round_id_joueur,int(round_class_joueur), round_nom_joueur,round_prenom_joueur]
            print ("liste : id_joueur, classement joueur, nom, prenom")
            print(liste_class_joueur)
            liste_liste_class_joueur.append(liste_class_joueur)
            print (liste_liste_class_joueur)

            index_joueur = index_joueur + 1

            print("FIN RECUPERATION DES DONNEES DU JOUEUR")
        print("liste_liste_class_joueur : ")
        print(liste_liste_class_joueur)

        from operator import itemgetter
        print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur, key=itemgetter(1),reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
        print(joueur_class_decroissant)

        #Mise en ordre des joueurs par classment, le classment étant la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=False))
        print("Affichage joueur par classement croissant")
        print(joueur_class_croissant)

        print("Affichage des paires de joueurs par identifiant du round 1 \n")

        #Récupérer le nombre total de point des joueurs, et l'ajouter à la liste des listes des joueurs 
        #La liste d'un joueur contiendra donc ID, classement, Nom, Prenom, nombre total des points.
        #En prenant la liste croissante, le prochain tri sur le nombre total de points devrait mettre les joueurs 
        #dans un ordre croissant total de points et ensuite classement, ce qui reste à vérifier, mais si c'est le cas, les paires seront à choisir selon l'ordre des places dans la liste
        
        liste_paire_1=[]
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])
        #print(liste_paire_1)
        print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
        print("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]) + " , Prénom : " + str(liste_paire_1[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]) + " , Prénom : " + str(liste_paire_1[1][3]))
        print()

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        #print(liste_paire_2)
        print("Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        print("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]) + " , Prénom : " + str(
            liste_paire_2[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]) + " , Prénom : " + str(
            liste_paire_2[1][3]))
        print()

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        #print(liste_paire_3)
        print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        print("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]) + " , Prénom : " + str(liste_paire_3[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]) + " , Prénom : " + str(
            liste_paire_3[1][3]))
        print()

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        #print(liste_paire_4)
        print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        print("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]) + " , Prénom : " + str(
            liste_paire_4[0][3]))
        print("ID")
        print("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]) + " , Prénom : " + str(
            liste_paire_4[1][3]))
        print()
        print("********** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ********************")


        nom = input("saisie nom du Round, Round 1 si pas de saisie:\n")
        if (nom == ""):
            nom = "Round 1"

        date_heure_debut = datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print ("début heure round : " + str_date_heure_debut)

        print("********* FIN CREATION ROUND *************************")


"""Appel du modele de creation de l'instance du tournoi """




"""Appel ou creation de l instance des creations des 8 joueurs"""


"""Recuperation des joueurs pour les mettre dans le bon ordre au 1er tour"""


'''
"""Recuperation des joueurs pour les mettre dans le bon ordre aux tours suivants"""