import os


class ClassVueAffichage:
    def __init__(self):
        pass

    def Affichage(self, texte1, texte2, texte3):
        print(texte1)
        print(texte2)
        print(texte3)

    def Affichage1Ligne(self, texte1):
        print(texte1)

    def Affichage2Lignes(self, texte1, texte2):
        print(texte1)
        print(texte2)

    def Input(self, texte1):
        input_saisie = input(texte1 + "\n")
        return (input_saisie)

    def SaisieScore(self, joueur1, joueur2, texte_joueur1, texte_joueur2):
        saisie_score_paire = ""
        while saisie_score_paire != "111":
            saisie_score_paire = ""

            saisie_score1 = ClassVueAffichage.\
                Input(self=True, texte1=texte_joueur1 + " " + (joueur1))

            if saisie_score1 == "0" or \
               saisie_score1 == "0.5" or \
               saisie_score1 == "1":
                saisie_score_paire = saisie_score_paire + "1"
            else:
                print("Erreur saisie score, valeurs possibles, 0 ou 0.5 ou 1")
                if saisie_score1 == "E":
                    os._exit(0)

            saisie_score2 = ClassVueAffichage.\
                Input(self=True,
                      texte1=texte_joueur2 + " " + (joueur2))
            if saisie_score2 == "0" or \
               saisie_score2 == "0.5" or \
               saisie_score2 == "1":

                saisie_score_paire = saisie_score_paire + "1"
            else:
                print("Erreur saisie score, valeurs possibles, 0 ou 0.5 ou 1")
                if saisie_score1 == "E":
                    os._exit(0)

            if saisie_score1.isdigit() and saisie_score2.isdigit():
                pass

            try:
                float_saisie_score1 = float(saisie_score1)
                float_saisie_score2 = float(saisie_score2)
                if (float(saisie_score1) + float(saisie_score2) == 1):
                    saisie_score_paire = saisie_score_paire + "1"
                else:
                    print(
                        "Erreur saisie score, le total des deux scores doit "
                        "??tre ??gal ?? 1, et les scores possibles "
                        "sont 0 ou 0.5 ou 1")
                    saisie_score_paire = ""
                    if saisie_score1 == "E":
                        os._exit(0)
            except ValueError:
                print("Saisie d'un nombre uniquement 0, 0.5 et 1 en valeur"
                      " accept??es pour un total des deux scores de 1")
            # le try doit ??tre fait, mais la variable ??tant inutilis??e,
            # cela pose un probl??me ?? flake8, ces lignes sont inutiles dans le
            # programme, mais servent ?? tromper flake 8
            float_saisie_score1 = float_saisie_score1
            float_saisie_score2 = float_saisie_score2

        return (saisie_score1, saisie_score2)
