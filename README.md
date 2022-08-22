# Projet_4
#Gérer les tournois d'échecs et les joueurs au sein d'un club d'échec.
#Projet effectué par Lionel R. dans le cadre de la formation « Openclassroom »  - développeur d’applications python-.

Contexte :
Un club d'échec demande....

Le but général du programme est de gérer les scores et les joueurs en terme de performance au sein d'un club d'échec.

Que fait le programme :

1er : Création de tournoi. Nom, lieu, date de début et date de fin, nombre de tours (4 par défaut).

2ème : Ajout de 8 joueurs. Nom de famille, prénom, date de naissance, sexe, classement.

3ème : Création des rondes. Création des paires de joueurs pour chaque partie.

4ème : Saisie des résultats des matchs.

Reprise des points 3 et 4 jusqu'à la fin du nombre de rondes prévu.

A la fin du tournoi, une mise à jour du classement des joueurs est effectuée.

Ensuite, des rapports peuvent être sortis.

Pendant le tournoi, le tournoi en cours est sauvegardé. Possibilité d'en créer ou en récupérer d'anciens 
ou modifier les classements.
***
Installation et lancement du programme :

1 - travail effectué sous WSL2 : WSL2 est donc nécessaire pour ces lignes de commandes.

Création du répertoire de projet avec la commande mkdir:
Mon_repertoire:~/openclassrooms$ "mkdir projet4"

Aller sous le projet  :
Mon_repertoire:~/openclassrooms$ "cd projet 4"

Installer virtualenv si nécéssaire :
"pip install virtualenv" 

créer un environnement virtuel avec la commande virtualenv env
Mon_repertoire:~/openclassrooms/projet4$ "virtualenv env"

Activer l'environnement virtuel avec la commande "source env/bin/activate"
(env) Mon_repertoire:~/openclassrooms/projet4$

Récupération du programme via le lien ci dessous.
https://github.com/LioExpleo/OPC_Projet04.git

Mettre tous les 4 fichiers *.py sous le répertoire que l'on vient de créer.

Lancer la commande "pip install -r requirements.txt" pour installer les packages nécessaires.

Lancer la commande "python3 main.py


## Utilisation
Le menu permet différentes demandes.

### 1) Consulter la liste des tournois dans la base de données
### 2) Créer un nouveau tournoi
### 3) Charger un tournoi de la liste à partir de la base de donnée

### 4) Créer des joueurs pour le tournoi en cours

### 5) Création des rondes pour le tournoi en cours. 
        - l'ordinateur met dans une liste de liste les 8 joueurs selon leur classement
        - l'ordinateur génére les paires de joueurs. Génération différentes selon que ce soit le 1er tour ou un autre.

### 6) Saisie des résultats du match. 

### 7) Repassage aux étapes 5 et 6 automatiquement si pas de sortie du programme jusqu'à la fin du programme.

### 8) une fois tous les scores de toutes les rondes saisies, une mise à jour manuelle des classements des joueurs sera faite.

### 9) Les rapports
- différents rapports peuvent être sortis à partir de la base de données.
  - ●	Liste de tous les acteurs :
  ○	par ordre alphabétique ;
  ○	par classement.
  
  - ●	Liste de tous les joueurs d'un tournoi :
  ○	par ordre alphabétique ;
  ○	par classement.
  ●	Liste de tous les tournois.
  ●	Liste de tous les tours d'un tournoi.
  ●	Liste de tous les matchs d'un tournoi.

### 10) Flake8
- Installez flake8 avec la commande: 
```
pip intall flake8-html
```
- S'il n'existe pas, créer un fichier setup.cfg
- Ecrire le texte suivant dedans:
```
[flake8]
exclude = .git, env, __pycache__, .gitignore
max-line-length = 119
```
- Tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake.