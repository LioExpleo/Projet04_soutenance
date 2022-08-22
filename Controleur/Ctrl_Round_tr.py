import os
import re
#from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
#from Modele.Round import ClassRound
import time
import json
from Controleur.fonctions import creat_dict,creat_list
from datetime import datetime
from Controleur.fonctions import tournoi_exist

from tinydb import TinyDB, Query, where
Todo = Query()

#permet de mettre dans un ordre choisi les listes
from operator import itemgetter

db_round = TinyDB('round.json')

def creat_round():
    from Controleur.Ctrl_Tournoi import select_tournoi
    print("CreatRound_1")
    liste_liste_class_joueur = []
    # select_tournoi=""
    tournoi_select = select_tournoi()
    print("Prochain round tournoi selectionné : " + tournoi_select)

    # Affichage du tournoi
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')
    db_joueurs = TinyDB('joueurs.json')
    print("db_tournois.search(where('id_tournoi')==tournoi_select")
    int_tournoi_select = int(tournoi_select)

    # charger le tournoi selectionné à partir de la base de données dans tournoi
    tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
    print(tournoi)

    import json
    fileObject = open("tournois.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)

    id_t = (tournoi[0]['id_tournoi'])
    print("id tournoi : " + str(id_t))

    test_round =""
    try:
        Tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
        print("Round précédent : " + str(Tournoi_round_en_cours))
        #creat_round_2(tournoi_select)
    except KeyError:
        test_round = 1
        print("création du round 1")
        #creat_round_1(tournoi_select)
    # Si pas de round en cours présent dans la bdd, création round 1,
    # sinon, appel de la création des rounds supérieurs
    if  test_round == 1:
        creat_round_1(tournoi_select)
    else:
        creat_round_2(tournoi_select)


    return()




def creat_round_1(tournoi_select):
    print ("CREATION PROCHAIN ROUND EN COURS")
    from Controleur.Ctrl_Tournoi import select_tournoi
    print("CreatRound_1")
    liste_liste_class_joueur = []
    # select_tournoi=""
    # tournoi_select = select_tournoi()
    print("Prochain round tournoi selectionné : " + tournoi_select)

    # Affichage du tournoi
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')
    db_joueurs = TinyDB('joueurs.json')
    print("db_tournois.search(where('id_tournoi')==tournoi_select")
    int_tournoi_select = int(tournoi_select)

    # charger le tournoi selectionné à partir de la base de données dans tournoi
    tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
    print(tournoi)

    # Récupération des informations du fichier JSON du tournoi pour créer les rounds
    import json
    fileObject = open("tournois.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)

    id_t = (tournoi[0]['id_tournoi'])
    #print("id tournoi : " + str(id_t))

    nom_t =(tournoi[0]['nom'])
    #print("nom : " + nom_t)

    nb_r=(tournoi[0]['nombre de rounds'])
    #print(nb_r + " rounds")

    list_id_joueur=[]

    id_j1=(tournoi[0]['id_j1'])
    #print("id joueur 1 : " + id_j1)
    list_id_joueur.append(id_j1)

    id_j2 = (tournoi[0]['id_j2'])
    #print("id joueur 2 : " + id_j2)
    list_id_joueur.append(id_j2)

    id_j3 = (tournoi[0]['id_j3'])
    #print("id joueur 3 : " + id_j3)
    list_id_joueur.append(id_j3)

    id_j4 = (tournoi[0]['id_j4'])
    #print("id joueur 4 : " + id_j4)
    list_id_joueur.append(id_j4)

    id_j5 = (tournoi[0]['id_j5'])
    #print("id joueur 5 : " + id_j5)
    list_id_joueur.append(id_j5)

    id_j6 = (tournoi[0]['id_j6'])
    #print("id joueur 6 : " + id_j6)
    list_id_joueur.append(id_j6)

    id_j7 = (tournoi[0]['id_j7'])
    #print("id joueur 7 : " + id_j7)
    list_id_joueur.append(id_j7)

    id_j8 = (tournoi[0]['id_j8'])
    #print("id joueur 8 : " + id_j8)
    list_id_joueur.append(id_j8)

    #print("nombre de rounds")
    #print(nb_r)

    db_joueurs = TinyDB('joueurs.json')
    index_joueur = 0
    while (index_joueur < 8):
        id_jx = "id_j" + str(index_joueur)

        print("id_joueur " + str(index_joueur) + ": ")
        id_joueur_en_cours = ""
        int_id_joueur_en_cours = ""
        try:
            #id_joueur_en_cours = (dict_tournoi[id_jx])
            id_joueur_en_cours = list_id_joueur[index_joueur]
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

        #print("identifiant joueur :")
        round_id_joueur = (dict_joueur["id_joueur"])
        #print(round_id_joueur)

        #print("Nom :")
        #print(dict_joueur["Nom"])
        round_nom_joueur = (dict_joueur["Nom"])

        #print("Prénom :")
        #print(dict_joueur["Prenom"])
        round_prenom_joueur = (dict_joueur["Prenom"])

        #print("Né le :")
        #print(dict_joueur["date de naissance"])

        #print("Sexe :")
        #print(dict_joueur["sexe"])

        #print("Classement :")
        round_class_joueur = (dict_joueur["Classement"])
        #print(round_class_joueur)

        liste_class_joueur = [round_id_joueur, int(round_class_joueur), round_nom_joueur, round_prenom_joueur]
        #print("liste : id_joueur, classement joueur, nom, prenom")
        #print(liste_class_joueur)
        liste_liste_class_joueur.append(liste_class_joueur)
        #print(liste_liste_class_joueur)

        index_joueur = index_joueur + 1

#       print("FIN RECUPERATION DES DONNEES DU JOUEUR")

        #print("liste_liste_class_joueur : ")
        #print(liste_liste_class_joueur)

    #Mise des joueurs dans ordre décroissant
    from operator import itemgetter
    #print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True)))
    joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
    print(joueur_class_decroissant)

    # Mise en ordre des joueurs par classement, le classement étant la valeur en position "1" de la liste
    joueur_class_croissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=False))
    print("Affichage joueur par classement croissant")
    print(joueur_class_croissant)

    print("Affichage des paires de joueurs  du round 1 par identifiant \n")
    liste_paire_1 = []
    liste_paire_1.append(joueur_class_croissant[0])
    liste_paire_1.append(joueur_class_croissant[4])
    # print(liste_paire_1)
    print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
    print("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]) + " , Prénom : " + str(
        liste_paire_1[0][3]))
    print("VS")
    print("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]) + " , Prénom : " + str(
        liste_paire_1[1][3]))
    print()

    liste_paire_2 = []
    liste_paire_2.append(joueur_class_croissant[1])
    liste_paire_2.append(joueur_class_croissant[5])
    # print(liste_paire_2)
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
    # print(liste_paire_3)
    print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
    print("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]) + " , Prénom : " + str(
        liste_paire_3[0][3]))
    print("VS")
    print("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]) + " , Prénom : " + str(
        liste_paire_3[1][3]))
    print()

    liste_paire_4 = []
    liste_paire_4.append(joueur_class_croissant[3])
    liste_paire_4.append(joueur_class_croissant[7])
    # print(liste_paire_4)
    print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
    print("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]) + " , Prénom : " + str(
        liste_paire_4[0][3]))
    print("ID")
    print("ID: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]) + " , Prénom : " + str(
        liste_paire_4[1][3]))
    print()
    print("********** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ********************")

    nom = input("saisie nom du Round, Round 1 si pas de saisie:\n")
    if (nom == ""):
        nom = "Round 1"

    #mise de l'heure de depart dans la liste pour la mettre dans la base de donnée du tournoi
    date_heure_debut = datetime.now()
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
    #print ("Ctrl_Round - creat_round_1")
    #print("inst_creat_round_1 = ClassRound.CreatRound_1(x)")

    #inst_creat_round_1 = ClassRound.CreatRound_1(self=True)
    #Stocker les instances de Round dans le tournoi
    liste_round_1=[]
    liste_round_1.append(str_date_heure_debut)
    liste_round_1.append(liste_paire_1)
    liste_round_1.append(liste_paire_2)
    liste_round_1.append(liste_paire_3)
    liste_round_1.append(liste_paire_4)
    print()
    print("liste_round_1")
    print(liste_round_1)

    from tinydb import TinyDB, Query, where
    db_tournois = TinyDB('tournois.json')
    print()
    print("numéro de tournoi")
    print(int_tournoi_select)

    #FAIRE UNE METHODE DANS MODELE ET L'APPELER ICI POUR RESPECT MVC
    #La sélection du round 1 est sauvegardée dans la base de données du tournoi, il faudra écraser l'instance avec le résultat en plus des matchs
    #Si round_1+match n'existe pas dans la base de donnée, il est créé
    db_tournois.update({"round_1+match": liste_round_1}, Todo.id_tournoi == int_tournoi_select)
    #joueur_a_charger = joueur_a_charger + 1
    #Ecriture du round en cours dans la base de donnée du tournoi
    db_tournois.update({"round_en_cours": 1}, Todo.id_tournoi == int_tournoi_select)
    return()

def creat_round_2(tournoi_select):
        print("CREATION PROCHAIN ROUND >2 EN COURS")
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatRound_2 et plus")
        liste_liste_class_joueur = []
        # select_tournoi=""
        #tournoi_select = select_tournoi()
        print("Prochain round tournoi selectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        # charger le tournoi selectionné à partir de la base de données dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        #Récupération des informations du fichier JSON du tournoi pour créer les rounds
        import json
        fileObject = open("tournois.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)

        id_t = (tournoi[0]['id_tournoi'])
        #print("id tournoi : " + str(id_t))

        Tournoi_round_en_cours = (tournoi[0]['round_en_cours'])
        #print("Round précédent : " + str(Tournoi_round_en_cours))

        nom_t =(tournoi[0]['nom'])
        #print("nom : " + nom_t)

        nb_r=(tournoi[0]['nombre de rounds'])
        #print(nb_r + " rounds")

        list_id_joueur=[]

        id_j1=(tournoi[0]['id_j1'])
        #print("id joueur 1 : " + id_j1)
        list_id_joueur.append(id_j1)

        id_j2 = (tournoi[0]['id_j2'])
        #print("id joueur 2 : " + id_j2)
        list_id_joueur.append(id_j2)

        id_j3 = (tournoi[0]['id_j3'])
        #print("id joueur 3 : " + id_j3)
        list_id_joueur.append(id_j3)

        id_j4 = (tournoi[0]['id_j4'])
        #print("id joueur 4 : " + id_j4)
        list_id_joueur.append(id_j4)

        id_j5 = (tournoi[0]['id_j5'])
        #print("id joueur 5 : " + id_j5)
        list_id_joueur.append(id_j5)

        id_j6 = (tournoi[0]['id_j6'])
        #print("id joueur 6 : " + id_j6)
        list_id_joueur.append(id_j6)

        id_j7 = (tournoi[0]['id_j7'])
        #print("id joueur 7 : " + id_j7)
        list_id_joueur.append(id_j7)

        id_j8 = (tournoi[0]['id_j8'])
        #print("id joueur 8 : " + id_j8)
        list_id_joueur.append(id_j8)

        #print("nombre de rounds")
        #print(nb_r)

        db_joueurs = TinyDB('joueurs.json')
        index_joueur = 0
        list_jx = []
        while (index_joueur < 8):
                id_jx = "id_j" + str(index_joueur)

                #print("id_joueur " + str(index_joueur) + ": ")
                id_joueur_en_cours = ""
                int_id_joueur_en_cours = ""
                try:
                        #id_joueur_en_cours = (dict_tournoi[id_jx])
                        id_joueur_en_cours = list_id_joueur[index_joueur]
                except IndexError:
                        print("Vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds X")
                        os._exit(1)

                try:
                        int_id_joueur_en_cours = int(id_joueur_en_cours)
                except ValueError:
                        print("Erreur, vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds Y")
                        os._exit(0)

                joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
                dict_joueur = creat_dict(joueur)


                #print("identifiant joueur :")
                round_id_joueur = (dict_joueur["id_joueur"])
                #print(round_id_joueur)

                #print("Nom :")
                #print(dict_joueur["Nom"])
                round_nom_joueur = (dict_joueur["Nom"])

                #print("Prénom :")
                #print(dict_joueur["Prenom"])
                round_prenom_joueur = (dict_joueur["Prenom"])

                #print("Né le :")
                #print(dict_joueur["date de naissance"])

                #print("Sexe :")
                #print(dict_joueur["sexe"])

                #print("Classement :")
                round_class_joueur = (dict_joueur["Classement"])
                #print(round_class_joueur)

                liste_class_joueur = [round_id_joueur, int(round_class_joueur), round_nom_joueur, round_prenom_joueur]
                #print("liste : id_joueur, classement joueur, nom, prenom")
                #print(liste_class_joueur)
                liste_liste_class_joueur.append(liste_class_joueur)
                #print(liste_liste_class_joueur)

                #Liste avec id joueur et classement pour construction round > 1
                #Liste contient l'id, le classement, et un score à 0 pour le moment'
                #Attention, il ne faudra pas réécraser le score avec 0 lors des prochains rounds

                #SI TOURNOI ROUND EN COURS = 1 FAIRE
                list_ja = [round_id_joueur, int(round_class_joueur),0]
                list_jx.append(list_ja)
                index_joueur = index_joueur + 1

#                print("FIN RECUPERATION DES DONNEES DU JOUEUR")

        #print("liste_liste_class_joueur : ")
        #print(liste_liste_class_joueur)
        #print("Liste_jx***************************************************")
        #print(list_jx)

        #Récupération des scores des joueurs dans le tournoi pour les mettre dans une liste
        #de joueur qui contient, l'id du joueur, son score, son classement
        #les scores s'incrémentent des scores des matchs précédents en utilisant le round en cours
        #pour savoir combien de scores à aller chercher, attention, les joueurs ne sont pas dans le même ordre
        #print("")
        #print("Tournoi_round_en_cours : " + str(Tournoi_round_en_cours))

        #Récupération des scores des joueurs dans les rounds précédents
        #donc on enlève 1 au round en cours
        ScoreMatchRound_temp=[] #New
        joueur_score_class_id=[]
        joueur_score_class_id_temp=[]
        if Tournoi_round_en_cours >1:
                Tournoi_round_en_cours_temp = Tournoi_round_en_cours #- 1
        else:
                Tournoi_round_en_cours_temp = Tournoi_round_en_cours

        list_id_j_score=[]

        joueur_class_score = []
        joueur_score_class_id_new=[["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]]
        from operator import itemgetter
        while Tournoi_round_en_cours_temp >0:
                #print(" # debut ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                # recuperation des précedents scores scores

                score_match_round_temp = "ScoreMatchRound" + str(Tournoi_round_en_cours_temp)  # New
                # Mise en ordre des joueurs par classement, le classement étant la valeur en position "1" de la liste
                try:
                    score_matchRx_temp = (tournoi[0][score_match_round_temp])
                except KeyError:
                    print("Erreur, il faut d'abord entrer les scores du précédent round avant d'en créer un nouveau")
                    os._exit(0)

                print("score_matchRx_temp 1")
                print(score_matchRx_temp)
                joueur_score_class_id_temp = (sorted(score_matchRx_temp, key=itemgetter(0), reverse=True))
                joueur_score_class_id.append(joueur_score_class_id_temp)
                print("mise en ordre alphabetique par id du score")
                print(joueur_score_class_id_temp)

                index=0
                score_matchRx_temp_new=[]
                while index<8:
                        joueur_score_class_id_new[index][0]= joueur_score_class_id_temp[index][0]
                        id_en_cours = joueur_score_class_id_temp[index][0]
                        print(id_en_cours)

                        score_en_cours =float(joueur_score_class_id_temp[index][1])
                        print(score_en_cours)

                        print(joueur_score_class_id_new)
                        score_enreg= float(joueur_score_class_id_new[index][1])
                        print(score_enreg)

                        joueur_score_class_id_new[index][1] = score_en_cours + score_enreg
                        index=index+1
                        print(joueur_score_class_id_new)

                Tournoi_round_en_cours_temp = Tournoi_round_en_cours_temp - 1
                print(joueur_score_class_id_new)

        print("Affichage joueur par classement d'id")
        list_jx_class_id = (sorted(list_jx, key=itemgetter(0), reverse=True))
        print(joueur_score_class_id)
        print(list_jx_class_id)

        index_0=0
        index_1=1
        index_2=2
        while index_1 <16 :
                print(joueur_score_class_id_new)
                score_total= float(joueur_score_class_id_new[index_0][1])
                list_jx_class_id[index_0][2] = score_total
                index_0=index_0 + 1
                index_1=index_1+2
                index_2 = index_2 + 3
        print(list_jx_class_id)

        print("List_jx_**************************************************")
        print(list_jx)

        #Mise des joueurs dans ordre décroissant
        from operator import itemgetter
        print("LISTE CLASSEMENT JOUEUR" % (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
        print(joueur_class_decroissant)

        # Mise en ordre des joueurs par classement, le classement étant la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(list_jx, key=itemgetter(1), reverse=False))
        print("Affichage joueur par classement croissant et score à faire")
        print(joueur_class_croissant)

        joueur_class_score_croissant = (sorted(joueur_class_croissant, key=itemgetter(2), reverse=True))
        print("Affichage joueur par classement croissant et score -joueur_class_score_croissant-")
        print(joueur_class_score_croissant)

        #Faire une liste de joueurs déjà affronté par joueur;
        joueur_1=[joueur_class_score_croissant[0][0]]
        joueur_2 = [joueur_class_score_croissant[1][0]]
        joueur_3 = [joueur_class_score_croissant[2][0]]
        joueur_4 = [joueur_class_score_croissant[3][0]]
        joueur_5 = [joueur_class_score_croissant[4][0]]
        joueur_6 = [joueur_class_score_croissant[5][0]]
        joueur_7 = [joueur_class_score_croissant[6][0]]
        joueur_8 = [joueur_class_score_croissant[7][0]]

        list_jy=[]
        list_jy.append(joueur_1)
        list_jy.append(joueur_2)
        list_jy.append(joueur_3)
        list_jy.append(joueur_4)
        list_jy.append(joueur_5)
        list_jy.append(joueur_6)
        list_jy.append(joueur_7)
        list_jy.append(joueur_8)

        #faire une boucle sur tous les rounds joués
        #donc enlever 1 au tournoi en cours temp
        #Rechercher les scores de chaque joueur dont l'emplacment est différent selon le round

        if Tournoi_round_en_cours > 1:
                Tournoi_round_en_cours_temp = Tournoi_round_en_cours - 1
        else:
                Tournoi_round_en_cours_temp = Tournoi_round_en_cours

        print(joueur_class_score_croissant[0])

        # Recherche joueurs déjà affrontés ROUND 2 ET PLUS
        list_j_opp=[[joueur_class_score_croissant[0][0]],[joueur_class_score_croissant[1][0]],[joueur_class_score_croissant[2][0]],[joueur_class_score_croissant[3][0]],[joueur_class_score_croissant[4][0]],[joueur_class_score_croissant[5][0]],[joueur_class_score_croissant[6][0]],[joueur_class_score_croissant[7][0]]]

        print("list_j_opp - joueurs triés en fonction de leur score en priorité et de leur classement")
        print(list_j_opp)



        while Tournoi_round_en_cours_temp > 0:
                nom_donnees = "ScoreMatchRound" + str(Tournoi_round_en_cours_temp)

                score_matchRx = (tournoi[0][nom_donnees])
                print(score_matchRx)

                # Faire une boucle avec les 4 paires, et faire une liste de liste de joueur ayant déjà joué ensemble
                index_id_jy = 0
                index_list_jy = 0

                while (index_id_jy < 8):
                        index_paire = 0
                        index_position_paire = 1
                        index_position_impaire = 0
                        # faire une boucle des 4 paires des scores
                        # Faire une boucle pour vérifier que l'id du joueur se trouve dans les 4 paires
                        #print(score_matchRx[index_position_impaire][0])
                        #print(list_j_opp[index_id_jy][0])
                        #print(list_jy)
                        #print(score_matchRx)
                        #print(list_j_opp)
                        # Construction de la liste des joueurs déjà opposés
                        while index_position_impaire<7:
                                if list_j_opp[index_id_jy][0]==score_matchRx[index_position_impaire][0]:
                                        #print()
                                        print(list_j_opp[index_id_jy][0])
                                        print("=")
                                        print(score_matchRx[index_position_impaire][0])
                                        index = index_position_impaire +1
                                        list_jy[index_id_jy].append(score_matchRx[index][0])
                                        print(score_matchRx[index_position_impaire+1][0])

                                if list_j_opp[index_id_jy][0] == score_matchRx[index_position_paire][0]:
                                        index = index_position_paire -1
                                        list_jy[index_id_jy].append(score_matchRx[index][0])

                                        print(score_matchRx[index_position_impaire - 1][0])

                                index_position_impaire = index_position_impaire +2
                                index_position_paire = index_position_paire + 2
                        index_id_jy =index_id_jy + 1
                        print(list_jy)

                Tournoi_round_en_cours_temp = Tournoi_round_en_cours_temp - 1
                print("list_jy - ok, ça fonctionne")
                print("list_jy_joueurs deja affrontés - ok pour 1 round verifier pour les rounds suivants")
                print(list_jy)
        print()

        liste_paire_1 = []
        liste_paire_1.append(joueur_class_score_croissant[0])
        liste_paire_1.append(joueur_class_score_croissant[1])
        print(liste_paire_1)

        print("Paire 1, par ordre de classement et score, 1er joueur contre 2ème si pas déjà rencontré le 2ème")
        print("ID: " + str(joueur_class_score_croissant[0][0]))#
        print("VS")

        #A SUPPRIMER

        import time
        #While 4 paires non crées, reboucler
                # Tester joueur suivant liste temporaire triée [0] avec liste des joueurs déjà rencontrée [x] jusqu'à ce que x égal nbre de round
                # Si pas joueur rencontré, et liste parcourue, mettre le joueur suivant testé dans la paire
                # Sinon, refaire le test avec le joueur suivant
                # Supprimer les joueurs de la liste triée temporaire et de l'autre liste les joueurs mis dans la paire
                # et faire le test encore pour le joueur 1, puisqu'en supprimant les joueurs de la liste, le deuxième joueur testé est remonté en haut de la liste

        # Tant qu'on n'a pas créé les 4 paires, on reboucle

        ###############################################################################################################

        index_4paire = 1
        joueur_class_score_croissant_temp = joueur_class_score_croissant
        list_jy_temp = list_jy

        print("liste des joueurs déjà rencontrés temporaire pour triture programme")
        print(list_jy_temp)

        index_partenaire = 1
        liste_paire1=[]
        liste_paire2 = []
        liste_paire3 = []
        liste_paire4 = []
        index_paire_trouv=0
        nbr_part_renc = Tournoi_round_en_cours

        print("index nombre de partenaire déjà joués : " + str(nbr_part_renc))
        print("Création des paires pour la manche suivante en vérifiant que les joueurs ne se sont pas rencontrés")

        #Tant que les 4 paires ne sont pas testées
        part_trouv = 0
        index_joueur_renc = 1
        nbre_partenaire_test =1
        while (index_4paire <4):
                #test du 1er joueur qui suit celui à appairer avec ceux déjà rencontrés
                #index_joueur_renc = 1
                #print ("index_joueur_renc "+ str(index_joueur_renc))
                print(Tournoi_round_en_cours_temp + 1)
                print("index paires trouvées" + str(index_paire_trouv))

                #while (index_joueur_renc < (Tournoi_round_en_cours_temp + 1)) and (index_paire_trouv < 4):
                # Tant que les 4 paires ne sont pas trouvées ou
                # que les joueurs affrontés précédemment n'ont pas été testés

                #Tant que les 7 partenaires ne sont pas testés et qu'un partenaire n'a pas été trouvé, on reteste
                while (nbre_partenaire_test <7) and part_trouv == 0 :
                        print("joueurs classement et score croissant : " + str(joueur_class_score_croissant_temp))
                        joueur_1_test = joueur_class_score_croissant_temp[0][0]
                        print("joueurs à qui trouver un partenaire le mieux classé selon le système suisse : " + str((joueur_1_test)))

                        joueur_1_test = joueur_class_score_croissant_temp[index_partenaire][0]
                        print("joueur testé si déjà rencontré " + str(joueur_1_test))

                        print("liste des joueurs déjà rencontrés" + str(list_jy_temp))
                        print(index_joueur_renc)
                        print(list_jy_temp[0][index_joueur_renc])
                        print("joueur testé" + str(list_jy_temp[0][index_joueur_renc]))

                        #Tester tous les partenaires rencontrés, si joueur testé jamais rencontré,
                        #ok pour l'appairé, sinon regarder le joueur suivant
                        nbre_joueur_test_ok = 0
                        nbre_tour=0
                        index_joueur_renc = 1
                        while (nbre_tour < nbr_part_renc):
                            print(joueur_class_score_croissant_temp[index_partenaire][0])
                            print(list_jy_temp[0][index_joueur_renc])
                            if (joueur_class_score_croissant_temp[index_partenaire][0]) != (list_jy_temp[0][index_joueur_renc]):
                                nbre_joueur_test_ok = nbre_joueur_test_ok + 1
                                nbre_tour = nbre_tour + 1
                            else :
                                nbre_tour = nbre_tour + 1
                            index_joueur_renc = index_joueur_renc + 1

                        if nbre_joueur_test_ok == nbre_tour:
                            print("partenaire trouvé")
                            part_trouv = 1
                            index_paire_trouv = index_paire_trouv + 1
                        else:
                            nbre_partenaire_test = nbre_partenaire_test +1


                        if part_trouv == 1 :
                                print("JOUEUR A QUI TROUVER UN PARTENAIRE " + str(joueur_class_score_croissant_temp[0][0]))
                                print("PARTENAIRE TROUVE :" + str(joueur_class_score_croissant_temp[index_partenaire][0]))
                                index_paire_trouv = index_paire_trouv +1
                                if index_paire_trouv == 1:
                                        liste_paire1.append(joueur_class_score_croissant_temp[0][0])
                                        liste_paire1.append(joueur_class_score_croissant_temp[index_partenaire][0])

                                if index_paire_trouv == 2:
                                        liste_paire2.append(joueur_class_score_croissant_temp[0][0])
                                        liste_paire2.append(joueur_class_score_croissant_temp[index_partenaire][0])

                                if index_paire_trouv == 3:
                                        liste_paire3.append(joueur_class_score_croissant_temp[0][0])
                                        liste_paire3.append(joueur_class_score_croissant_temp[index_partenaire][0])

                                if index_paire_trouv == 4:
                                        liste_paire4.append(joueur_class_score_croissant_temp[0][0])
                                        liste_paire4.append(joueur_class_score_croissant_temp[index_partenaire][0])

                                print("suppression du joueur à qui on a trouvé un partenaire de la base de donnée et du partenaire trouvé")
                                print(joueur_class_score_croissant_temp)
                                joueur_class_score_croissant_temp.pop(0)
                                index = index_partenaire - 1
                                joueur_class_score_croissant_temp.pop(index)

                                index = index_joueur_renc - 1
                                print(joueur_class_score_croissant_temp)
                                print()
                                print("suppression du joueur à qui on a trouvé un partenaire et du partenaire de la base de donnée des joueurs rencontrés" )
                                print(str(list_jy_temp))
                                list_jy_temp.pop(0)

                                index = index_partenaire -1
                                list_jy_temp.pop(index)
                                print(list_jy_temp)
                                print()
                                index_partenaire =1
                        else :
                                print("tester joueur suivant")
                                index_partenaire=index_partenaire+1
                                test = ""


                print(liste_paire1)
                print(liste_paire2)
                print(liste_paire3)
                print(liste_paire4)

                index_4paire = index_4paire + 1

        print("********* FIN CREATION ROUND *************************")

        #print ("Ctrl_Round - creat_round_1")
        #print("inst_creat_round_1 = ClassRound.CreatRound_1(x)")

        #inst_creat_round_1 = ClassRound.CreatRound_1(self=True)
        #Stocker les instances de Round dans le tournoi
        date_heure_debut = datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print("début heure round : " + str_date_heure_debut)

        liste_round_x=[]
        liste_round_x.append(str_date_heure_debut)
        liste_round_x.append(liste_paire1)
        liste_round_x.append(liste_paire2)
        liste_round_x.append(liste_paire3)
        liste_round_x.append(liste_paire4)
        print()
        print("liste_round_x")
        print(liste_round_x)

        from tinydb import TinyDB, Query, where
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)

        # La sélection du round 1 est sauvegardée dans la base de données du tournoi, il faudra écraser l'instance avec le résultat en plus des matchs
        # Si round_1+match n'existe pas dans la nase de donnée, il est créé

        if Tournoi_round_en_cours < int(nb_r):
                Tournoi_round_en_cours = Tournoi_round_en_cours + 1
        else:
                print("Nombre maxi de round atteint !")

        if Tournoi_round_en_cours <= int(nb_r):
                update_round = ("round_"+str(Tournoi_round_en_cours)+"+match")
                db_tournois.update({update_round: liste_round_x},
                                   Todo.id_tournoi == int_tournoi_select)
                print("nouveau round")
                print(Tournoi_round_en_cours)
                db_tournois.update({"round_en_cours": Tournoi_round_en_cours},
                                   Todo.id_tournoi == int_tournoi_select)

        return ()
