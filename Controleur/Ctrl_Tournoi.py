"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
#from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
import time
import json
from Vue.affichage import ClassVueAffichage
from tinydb import TinyDB, Query, where
from datetime import datetime
from Controleur.fonctions import creat_list,creat_dict,tournoi_exist
Todo = Query()

db_tournois = TinyDB('tournois.json')

def creat_new_tournois():
    # identifiant tournoi
    import json
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournoi = TinyDB('tournois.json')
    mode_ouv_fichier_json = "r"
    with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
        pass

    # Rechercher un id libre dans la base de donnée en incrémentant l'id de test jusqu'à trouver un ID libre
    tournoi_cherche = 1
    tournoi_trouve = 0
    id_libre = 0

    # Si l' id_tournoi_cherché n'est pas trouvé, on le prend pour le mettre à l'id du nouveau tournoi
    # sinon, on reboucle jusqu'a trouver un id libre. On commence par regarder si l'id 1 existe
    tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
    tournoi_trouv = str(tournoi_trouve)
    # recherche de la position de id_joueur dans la chaine
    char = 'id_tournoi'
    PositDebNbre = (tournoi_trouv.find(char))
    # recherche de la position de nom dans la chaine
    char = "nom"
    PositFinNbre = (tournoi_trouv.find(char))

    # Recherche de l'id à partir des positions précédentes et suivantes'
    id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

    # tant que l'id cherché existe, on recherche jusqu'à en trouver un libre en l'incrémentant
    while (id_tournoi != ""):
        tournoi_cherche = tournoi_cherche + 1
        tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
        tournoi_trouv = str(tournoi_trouve)
        char = 'id_tournoi'
        PositDebNbre = (tournoi_trouv.find(char))

        char = "nom"
        PositFinNbre = (tournoi_trouv.find(char))

        id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

    else:
        id_libre = tournoi_cherche

    id_tournoi = id_libre
    nom=ClassVueAffichage.Input(self=True, texte1="saisie nom :")

    if nom == "":
        nom = ("Tournoi " + str(id_tournoi))
        ClassVueAffichage.Affichage(self=True,texte1="en absence de nom, le nom par défaut est " + nom,texte2="",texte3="")

    if nom == "r":
        nom = ("Tournoi " + str(id_tournoi))
        ClassVueAffichage.Affichage(self=True, texte1="r est un nom interdit, cela correspond à une commande clavier, le nom par défaut est " + nom,
                                        texte2="", texte3="")
    if nom == "E":
        nom = ("Tournoi " + str(id_tournoi))
        ClassVueAffichage.Affichage(self=True,
                                        texte1="E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est " + nom,
                                        texte2="", texte3="")

    lieu = ClassVueAffichage.Input(self=True, texte1="saisie lieu :")

    if lieu == "":
            lieu = ("Lieu " + str(id_tournoi))

    date = ClassVueAffichage.Input(self=True, texte1="date (format DD/MM/YYYY): ")

    if date == "":
        date_heure = datetime.now()
        str_date_heure = str(date_heure)
        char = '.'
        PositChar = str_date_heure.find(char)
        str_date_heure = str_date_heure[0:(PositChar - 9)]
        date = str_date_heure

    nbr_rounds = ClassVueAffichage.Input(self=True, texte1="saisie nombre de rounds, 4 rounds si pas de saisie ou erreur de saisie: ")

    if nbr_rounds == "":
        nbr_rounds = "4"
    try:
        int_nbr_rounds = int(nbr_rounds)
    except ValueError:
        ClassVueAffichage.Affichage(self=True,texte1="Nombre de round max = 7, mini = 1, 4 par défaut",texte2="",texte3="")
        int_nbr_rounds = 4
        nbr_rounds = "4"

    if int_nbr_rounds > 7 or int_nbr_rounds < 1:
        ClassVueAffichage.Affichage(self=True, texte1="Nombre de round max = 7, mini = 1, 4 par défaut",
                                    texte2="", texte3="")
        nbr_rounds = "4"

    id_j1 = ""
    id_j2 = ""
    id_j3 = ""
    id_j4 = ""
    id_j5 = ""
    id_j6 = ""
    id_j7 = ""
    id_j8 = ""
    round_1=""
    round_2 = ""
    round_3 = ""
    round_4 = ""
    round_5 = ""
    round_6 = ""
    round_7 = ""

    # saisie du type de matchs, bullet, blitz, ou coup rapide
    temps_matchs=""
    saisie=""
    list_tps={1:"bullet",2:"blitz",3:"coup rapide"}

    while saisie!="1" and saisie!="2" and saisie!="3":

        saisie = ClassVueAffichage.Input(self=True,
                                               texte1="saisie type de match : \"1\" pour bullet, \"2\"pour blitz,\"3\"pour coup rapide. E pour stopper le programme")

        if saisie == "E":
                os._exit(0)
    else:
        temps_matchs = list_tps[int(saisie)]

    print (temps_matchs)
    print()

    # saisie des remarques générale organisateur tournoi
    remarque_tournoi = ClassVueAffichage.Input(self=True, texte1="saisie des remarques de l'organisateur du tournoi :")
    print()

    # Serialize l'instance tournoi
    tournoi = {"id_tournoi": id_tournoi, "nom": nom, "lieu": lieu, "date du tournoi": date,
               "nombre de rounds": nbr_rounds, "id_j1": id_j1, "id_j2": id_j2, "id_j3": id_j3, "id_j4": id_j4,
               "id_j5": id_j5, "id_j6": id_j6, "id_j7": id_j7, "id_j8": id_j8, "round_1+match":round_1,"round_2+match":round_2,"round_3+match":round_3,"round_4+match":round_4,"round_5+match":round_5,"round_6+match":round_6,"round_7+match":round_7,"Temps":temps_matchs,"Remarques de l'organisateur":remarque_tournoi}


    # Insertion du joueur saisi dans la base de donnée
    ClassTournoi.CreatNewTournois(self=True,tournoi=tournoi)
    ClassVueAffichage.Affichage(self=True,texte1="Tournoi "+ nom + ", avec comme identifiant tournoi "+"\""+str(id_tournoi) +"\""+ ", créé.",texte2= "Date du tournoi : "+str(date),texte3="")
    return ()

def lect_tournois():# Afficher la liste des tournois

    with open('tournois.json') as mon_fichier:
        dico = json.load(mon_fichier)
    serialised_tournois = db_tournois.all()

    index=0
    for i in serialised_tournois :
        print(serialised_tournois [index])
        print()
        index=index+1
    return ()

#supprimer un tournoi de la liste pour éventuellement le ressaisir
def sup_tournois(menu_niv_2):
    with open('tournois.json') as mon_fichier:
        dico = json.load(mon_fichier)
    db_tournois = TinyDB('tournois.json')
    id_tournoi_del = int(menu_niv_2)
    db_tournois.remove(Todo.id_tournoi == id_tournoi_del)

#purge de la base de donnée
def purge_tournois():
    db_tournois.truncate()

def select_tournoi():
    id_tournoi_select = ""
    from tinydb import TinyDB, Query, where
    list_tournoi = []
    #Todo = Query()
    db_joueurs = TinyDB('joueurs.json')
    mode_ouv_fichier_json = "r"

    # SELECTION DU TOURNOI
    serialised_tournoi = db_tournois.all()
    str_tournoi = str(serialised_tournoi)

    # faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
    serialised_joueurs = db_joueurs.all()
    str_joueurs = str(serialised_joueurs)

    char = "{"
    x = 0
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

    # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
    # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
    ClassVueAffichage.Affichage(self=True,
                                texte1="",
                                texte2="liste des numéros de tournois dans la base de donnée qu'il est possible de sélectionner :",
                                texte3=str_list_tournoi + "\n")

    tournoi_a_charger = 1
    while (tournoi_a_charger < 2):
        #saisie d'un Id de joueur existant pour le joueur
        id_a_charger=ClassVueAffichage.Input(self=True,texte1="saisie Id ou n° du tournoi existant à sélectionner")

        if id_a_charger == "E" or id_a_charger == "e":
            #print("E ou e = commande pour sortir du prog")
            os._exit(0)

        # Vérification que le tournoi est bien dans la liste des tournois
        if id_a_charger in list_tournoi:
            tournoi_a_charger = tournoi_a_charger + 1
            list_tournoi.remove(id_a_charger)
            time.sleep(0.2)
            id_tournoi_select = id_a_charger

            # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
            ClassVueAffichage.Affichage(self=True, texte1="",
                                        texte2="Le tournoi " + id_tournoi_select + " est sélectionné",
                                        texte3="")

        else:
            # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
            ClassVueAffichage.Affichage(self=True, texte1="Ce tournoi n'est pas dans la liste des tournois existants, re-saisir un tournoi de la liste",texte2="",texte3="")
    return (id_tournoi_select)

def charge_joueurs_tournoi():
    id_tournoi_select=select_tournoi()
    # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
    ClassVueAffichage.Affichage(self=True,
                                texte1="Chargment des joueurs dans le tournoi " + id_tournoi_select,
                                texte2="", texte3="")

    from tinydb import TinyDB, Query, where
    list_tournoi = []
    Todo = Query()
    list_joueurs=[]

    db_tournois = TinyDB('tournois.json')
    db_joueurs = TinyDB('joueurs.json')

    mode_ouv_fichier_json = "r"
    #JOUEURS A CHARGER
    with open('joueurs.json') as mon_fichier:
        dico = json.load(mon_fichier)
        # print("data dico")
    index = 0
    # faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
    serialised_joueurs = db_joueurs.all()
    str_joueurs = str(serialised_joueurs)

    char = "{"
    x=0
    joueur_cherche = 1
    joueur_trouve = 0
    #for x in range(len(str_joueurs)):
    index=1
    for i in serialised_joueurs:
        index = index +1

        #Extraction de l'id
        char = 'id_joueur'
        PositDebNbre = (str_joueurs.find(char))

        char = "Nom"
        PositFinNbre = (str_joueurs.find(char))

        id_joueur = str_joueurs[(PositDebNbre + 12): (PositFinNbre - 3)]

        #Supprimer le 1er joueur traité de la trame du dictionnaire car il ne peut être chargé deux fois
        char = '}'
        PositDebNbre = (str_joueurs.find(char))

        str_joueurs=str_joueurs[(PositDebNbre+2):-1]
        list_joueurs.append(id_joueur)
        joueur_cherche = joueur_cherche + 1

    # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
    ClassVueAffichage.Affichage(self=True,
                                texte1="liste Id joueurs",
                                texte2=list_joueurs, texte3="")

    #Faire input de l'id, comparer avec les id de la liste, si id de la liste, mettre
    #dans le tournoi à l'emplacement de l'id 1 au début, et supprimer l'élément de la liste
    #sinon, forcer à ressaisir jusqu'à un id correct
    # if id pas dans la liste, afficher messsage defaut et recommmencer
    #sinon le charger dans le Tournoi et le supprimer de la liste, puis reproposer la liste pour le prochain joueur à charger
    joueur_a_charger = 1
    while (joueur_a_charger < 9 ):
        #saisie d'un Id de joueur existant pour le joueur n°"
        id_a_charger = ClassVueAffichage.Input(self=True,
                                               texte1="saisie Id ou n° de joueur existant pour le joueur n°" + str(joueur_a_charger))

        if id_a_charger == "E" or id_a_charger == "e":
            os._exit(0)

        if id_a_charger in list_joueurs:
            # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
            ClassVueAffichage.Affichage(self=True, texte1="joueur n°"+ id_a_charger + " sélectionné pour le tournoi",
                                        texte2="",
                                        texte3="")

            list_joueurs.remove(id_a_charger)
            time.sleep(0.2)
            str_list_joueurs=str(list_joueurs)
            str_list_joueurs =str_list_joueurs.replace('[','')
            str_list_joueurs = str_list_joueurs.replace('\',', ' -')
            str_list_joueurs = str_list_joueurs.replace('\']', '')
            str_list_joueurs = str_list_joueurs.replace('\'', 'joueur n°')

            ClassVueAffichage.Affichage(self=True,
                                        texte1="liste des numéros des joueurs non sélectionnés :",
                                        texte2=str_list_joueurs,
                                        texte3="")

            serialised_tournoi = db_tournois.all()
            str_tournoi = str(serialised_tournoi)
            str_tournoi = str(serialised_tournoi)
            str_id_tournoi_select = str(id_tournoi_select)

            #Sélection du joueur de la table tournoi à charger
            id_jx=("id_j"+str(joueur_a_charger))

            #ClassVueAffichage.Affichage(self=True,
            #                            texte1="Chargement du joueur dans le tournoi : " +str(id_tournoi_select),
            #                            texte2="",
            #                            texte3="")

            db_tournois = TinyDB('tournois.json')
            id_tournoi_select=int(id_tournoi_select)
            db_tournois.update({id_jx: id_a_charger}, Todo.id_tournoi == id_tournoi_select)
            joueur_a_charger = joueur_a_charger + 1

        else:
            ClassVueAffichage.Affichage(self=True,
                                       texte1="n° de joueur absent de la liste des joueurs ou déjà sélectionné pour le tournoi",
                                       texte2="",
                                       texte3="")

def lecture_match_tournoi():
    # Récupération des informations du fichier JSON du tournoi pour créer les rounds
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')

    tournoi_select = ClassVueAffichage.Input(self=True,
                                           texte1="saisie Id du tournoi pour lequel on veut le résultat des matchs" )
    tournoi_trouv = tournoi_exist(tournoi_select)
    if tournoi_trouv == []:
        print("Numéro de tournoi introuvable")
        os._exit(0)
    int_tournoi_select = int(tournoi_select)

    # charger le tournoi selectionné à partir de la base de données dans tournoi
    tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

    try:
        score_round1 = (tournoi[0]['ScoreMatchRound1'])
        print("Score des joueurs round 1 - ID joueur + score : " + str(score_round1[0]) + str(score_round1[1]))
        print("Score des joueurs round 1 - ID joueur + score : " + str(score_round1[2]) + str(score_round1[3]))
        print("Score des joueurs round 1 - ID joueur + score : " + str(score_round1[4]) + str(score_round1[5]))
        print("Score des joueurs round 1 - ID joueur + score : " + str(score_round1[6]) + str(score_round1[7]))
        print()
    except KeyError:
        print("pas de score pour le round 1")

    try:
        score_round2 = (tournoi[0]['ScoreMatchRound2'])
        print("Score des joueurs round 2 - ID joueur + score : " + str(score_round2[0])+ str(score_round2[1]))
        print("Score des joueurs round 2 - ID joueur + score : " + str(score_round2[2]) + str(score_round2[3]))
        print("Score des joueurs round 2 - ID joueur + score : " + str(score_round2[4]) + str(score_round2[5]))
        print("Score des joueurs round 2 - ID joueur + score : " + str(score_round2[6]) + str(score_round2[7]))
        print()
    except KeyError:
        print("pas de score pour le round 2")

    try:
        score_round3 = (tournoi[0]['ScoreMatchRound3'])
        print("Score des joueurs round 3 - ID joueur + score : " + str(score_round3[0]) + str(score_round3[1]))
        print("Score des joueurs round 3 - ID joueur + score : " + str(score_round3[2]) + str(score_round3[3]))
        print("Score des joueurs round 3 - ID joueur + score : " + str(score_round3[4]) + str(score_round3[5]))
        print("Score des joueurs round 3 - ID joueur + score : " + str(score_round3[6]) + str(score_round3[7]))
        print()
    except KeyError:
        print("pas de score pour le round 3")

    try:
        score_round4 = (tournoi[0]['ScoreMatchRound4'])
        print("Score des joueurs round 4 - ID joueur + score : " + str(score_round4[0]) + str(score_round4[1]))
        print("Score des joueurs round 4 - ID joueur + score : " + str(score_round4[2]) + str(score_round4[3]))
        print("Score des joueurs round 4 - ID joueur + score : " + str(score_round4[4]) + str(score_round4[5]))
        print("Score des joueurs round 4 - ID joueur + score : " + str(score_round4[6]) + str(score_round4[7]))
        print()
    except KeyError:
        print("pas de score pour le round 4")

    try:
        score_round5 = (tournoi[0]['ScoreMatchRound5'])
        print("Score des joueurs round 5 - ID joueur + score : " + str(score_round5[0]) + str(score_round5[1]))
        print("Score des joueurs round 5 - ID joueur + score : " + str(score_round5[2]) + str(score_round5[3]))
        print("Score des joueurs round 5 - ID joueur + score : " + str(score_round5[4]) + str(score_round5[5]))
        print("Score des joueurs round 5 - ID joueur + score : " + str(score_round5[6]) + str(score_round5[7]))
        print()
    except KeyError:
        print("pas de score pour le round 5")
        print()

def lecture_round_tournoi():
    # Récupération des informations du fichier JSON du tournoi pour créer les rounds
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')

    tournoi_select = ClassVueAffichage.Input(self=True,
                                           texte1="saisie Id du tournoi pour lequel on veut afficher les rounds" )
    tournoi_trouv = tournoi_exist(tournoi_select)
    if tournoi_trouv == []:
        print("Numéro de tournoi introuvable")
        os._exit(0)

    int_tournoi_select = int(tournoi_select)

    # charger le tournoi sélectionné à partir de la base de données dans tournoi
    tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))

    #ROUND 1
    #Extraction de round 1 de la base de donnée
    round1=""
    try:
        round1 = (tournoi[0]['round_1+match'])
        try:
            print("Round 1 - Date du tournoi : " + str(round1[0]))
            print()
        except IndexError:
            print("pas de round 1 créé")
        index=1
        if round1!="":
            while index<5 :
                print("Round 1 - Paire" +str(index) + " - Joueur 1 : " + "ID : " + str(round1[index][0][0]) + " - "+ str(round1[index][0][2]) + " - : "+ str(round1[index][0][3]))
                print("Round 1 - Paire" +str(index) + " - Joueur 2 : " + "ID : " + str(round1[index][1][0]) + " - " + str(round1[index][1][2]) + " - : " + str(round1[index][1][3]))
                index = index +1
                print()
    except KeyError:
        print("pas de round créé pour le round 1")

    # ROUND 2 ET PLUS
    index_round = 2
    while index_round<6:
        round_bd = "round_" + str(index_round) + "+match"
        roundx = (tournoi[0][round_bd])
        try:
            print("Round" + str(index_round) + " - Date du tournoi : " + str(roundx[0]))

            index = 1
            while index < 5:
                print("Round" + str(index_round) + " - Paire" + str(index) + " - Joueur 1 : " + "ID : " + str(roundx[index][0]))#
                print("Round" + str(index_round) + " - Paire" + str(index) + " - Joueur 2 : " + "ID : " + str(roundx[index][1]))
                index = index + 1
                print()
        except IndexError:
            print("pas de round " + str(index_round) + "créé")
        index_round = index_round +1
    print()

def lecture_joueur_tournoi():
    # Récupération des informations du fichier JSON du tournoi pour créer les rounds
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')


    tournoi_select = ClassVueAffichage.Input(self=True,
                                           texte1="saisie Id du tournoi pour lequel on veut afficher les joueurs" )

    tournoi_trouv=tournoi_exist(tournoi_select)
    if tournoi_trouv ==[]:
        print("Numéro de tournoi introuvable")
        os._exit(0)

    int_tournoi_select = int(tournoi_select)

    # charger le tournoi sélectionné à partir de la base de données dans tournoi
    tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
    #print(tournoi)
    #print()
    id_j1 = (tournoi[0]['id_j1'])
    id_j2 = (tournoi[0]['id_j2'])
    id_j3 = (tournoi[0]['id_j3'])
    id_j4 = (tournoi[0]['id_j4'])
    id_j5 = (tournoi[0]['id_j5'])
    id_j6 = (tournoi[0]['id_j6'])
    id_j7 = (tournoi[0]['id_j7'])
    id_j8 = (tournoi[0]['id_j8'])

    db_joueurs = TinyDB('joueurs.json')
    #print(db_joueurs)
    # charger le tournoi sélectionné à partir de la base de données dans tournoi

    joueur_charge=False
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
        joueur_charge = True
    except ValueError:
        print("pas de joueur 8 chargé dans le tournoi")
        joueur_chargé = False

    if joueur_charge == True:
        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur1)
        print("JOUEUR 1 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(
             prenom_j) + " - " + str(
                    date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j,nom_j,prenom_j,date_j,sexe_j,classement_j =liste_joueur_tournoi(joueur2)
        print("JOUEUR 2 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur3)
        print("JOUEUR 3 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur4)
        print("JOUEUR 4 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur5)
        print("JOUEUR 5 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur6)
        print("JOUEUR 6 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur7)
        print("JOUEUR 7 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

        id_j, nom_j, prenom_j, date_j, sexe_j, classement_j = liste_joueur_tournoi(joueur8)
        print("JOUEUR 8 DU TOURNOI : Identifiant n°" + str(id_j) + " - " + str(nom_j) + " - " + str(prenom_j) + " - " + str(
                date_j) + " - " + str(sexe_j) + " - Classé," + str(classement_j))

print()


def lecturetournoi():
    # Récupération des informations du fichier JSON du tournoi pour créer les rounds
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')


    with open('tournois.json') as mon_fichier:
        dico = json.load(mon_fichier)

    serialised_tournois = db_tournois.all()
    print()
    index=0
    for i in serialised_tournois:
        print(("ID tournoi n°" + str(serialised_tournois[index]['id_tournoi']))+(",   appelé "+ str(serialised_tournois[index]['nom']))+(", qui s'est passé à "+ str(serialised_tournois[index]['lieu']))+(", en date du "+ str(serialised_tournois[index]['date du tournoi'])))
        print()
        index=index+1

def liste_joueur_tournoi(joueur):
    dict_joueur1 = creat_dict(joueur)
    id_j = (dict_joueur1["id_joueur"])
    nom_j = (dict_joueur1["Nom"])
    prenom_j = (dict_joueur1["Prenom"])
    date_j = (dict_joueur1["date de naissance"])
    sexe_j = (dict_joueur1["sexe"])
    classement_j = (dict_joueur1["Classement"])
    return(id_j,nom_j,prenom_j,date_j,sexe_j,classement_j)
