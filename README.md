# Projet_4
#Gérer les tournois d'échecs et les joueurs au sein d'un club d'échec.
#Projet effectué par Lionel R. dans le cadre de la formation « Openclassroom »  - développeur d’applications python-.

Contexte :
Cahier des charges, création d'un programme qui gère les joueurs et les tournois d'échec.

Que fait le programme :

1 : Principe général du programme, 
  - permet d'inscrire les joueurs dans une base de donnée. Nom de famille, prénom, date de naissance, sexe, classement.
  - Créer des tournois. Nom, lieu, date de début et date de fin, nombre de tours.
  - Ajout de 8 joueurs dans un tournoi.
  - Création des rounds. Création des paires de joueurs pour chaque partie. (utilisation dy système Suisse pour création des rounds)
  - Lorsqu'un round est terminé, l'organisateur saisi les résultats.
  - Tant que les résultats du round précédent ne sont pas saisis, le round suivant ne peut être créé.
  - les étapes de création des rounds et de saisie des scores se fait jusqu'à la fin du tournoi.

Une mise à jour du classement des joueurs peut être effectuée par le directeur du tournoi.
Des rapports peuvent être affichés.
Plusieurs tournois peuvent être gérés simultanément.
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
https://github.com/LioExpleo/Projet04_soutenance.git

Mettre tous le contenu de ce qui vient d'être récupéré sous le répertoire que l'on vient de créer.

De mon côté, j'ai effectué la commande " pip freeze > requirements.txt", vous pouvez donc
Lancer la commande "pip install -r requirements.txt" pour installer les packages nécessaires.

Lancer la commande "python3 main.py

## Utilisation
Au lancement, la commande help permet d'afficher tous les menus.

### 1) Consulter la liste des tournois dans la base de données
### 2) Créer un nouveau tournoi
### 3) Charger un tournoi de la liste à partir de la base de donnée

### 4) Créer des joueurs

### 5) Création des rounds pour le tournoi en cours. 
        - l'ordinateur met dans une liste de liste les 8 joueurs selon leur classement
        - l'ordinateur génére les paires de joueurs. Génération différentes selon que ce soit le 1er tour ou un autre.

### 6) Saisie des résultats du match. 

### 7) Repassage aux étapes 5 et 6 automatiquement si pas de sortie du programme jusqu'à la fin du programme.

### 8) une fois tous les scores de toutes les rondes saisies, une mise à jour manuelle des classements des joueurs sera faite.

### 9) Les rapports
- différents rapports peuvent être sortis à partir de la base de données.
  - ●	Liste de tous les acteurs :
  ○	par ordre alphabétique (JCN);
  ○	par classement (JCC).
  
  - ●	Liste de tous les joueurs d'un tournoi :
  ○	par ordre alphabétique et classmeent (TJ).
  ●	Liste de tous les tournois (TT).
  ●	Liste de tous les tours d'un tournoi (TR).
  ●	Liste de tous les matchs d'un tournoi (TM).

### 10) Flake8
- Installez flake8 avec la commande: 
```
pip intall flake8-html
```
- tapez la commande suivante pour générer le fichier flake8
```
flake8 --format=html --htmldir=flake-report --max-line-length=119 --exclude=env/
Si cela fonctionne, tant mieux, sinon, pour mon cas, et après de multiples tentatives avec mon mentor ça ne fonctionne pas.

Il donc a été décidé de faire comme suit :
flake8 --format=html --htmldir=flake-report --max-line-length=119 --ignore=env/
fonctionne, mais il faudra supprimer les fichiers généré env à la main et pas de page générale html de génération ok 
flake8 --format=html --htmldir=flake-report --max-line-length=119 --ignore=env/
```
- la commande qui fonctione a été :
```
flake8 --format=html --htmldir=flake-report --max-line-length=119 --ignore=env/
```
- Cela fonctionne, après correction des programmes *.py, plus de trace d'erreur de fichiers du programme.
- Le rapport généré dans le dossier flake ne contient pas de page générale sans erreur, mais cela fonctionne.