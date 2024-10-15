Jeu du Pendu avec Tkinter
Ce projet implémente le classique jeu du pendu à l'aide de l'interface graphique Python Tkinter. Le joueur doit deviner un mot en proposant des lettres avant d'épuiser ses vies.

Fonctionnalités
Interface graphique : Utilisation de Tkinter pour une interface interactive.
Saisie des lettres : L'utilisateur peut saisir une lettre pour deviner le mot.
Système de vies : Le joueur commence avec 7 vies, et perd une vie à chaque mauvaise devinette.
Suggestion de lettres : Une fonctionnalité de suggestion de lettres basée sur une analyse probabiliste.
Affichage dynamique : Le mot à deviner est mis à jour au fur et à mesure que l'utilisateur propose des lettres.
Fin du jeu : Le jeu indique si le joueur a gagné ou perdu et affiche le mot final.


Prérequis
Avant de pouvoir exécuter ce programme, vous devez installer Python sur votre machine. Assurez-vous également que le fichier contenant les mots (mots.txt) est accessible.

Python 3.x
Tkinter (inclus avec Python)
Installation
1. Cloner le dépôt
Commencez par cloner ce dépôt sur votre machine locale :


git clone https://github.com/votre-utilisateur/jeu-du-pendu.git
cd jeu-du-pendu
2. Préparer le fichier mots.txt
Créez un fichier texte nommé mots.txt contenant une liste de mots (un mot par ligne) dans le répertoire du projet. 

Utilisation
1. Lancer l'application
Exécutez le fichier Python pendu.py (ou autre nom choisi) pour démarrer l'application :


python pendu.py
Cela ouvrira une fenêtre graphique dans laquelle vous pourrez jouer au jeu du Pendu.

2. Interface du jeu
Entrez une lettre dans la zone de saisie et cliquez sur "Devinez" pour proposer une lettre.
Vous pouvez également demander une suggestion de lettre basée sur une analyse probabiliste.
Vous commencez avec 7 vies. Chaque mauvaise devinette vous fait perdre une vie.

Dépendances
Ce projet repose principalement sur Tkinter, qui est une bibliothèque graphique intégrée à Python. Aucune installation supplémentaire n'est nécessaire si vous utilisez Python standard.

Problèmes connus
Gestion des erreurs d'entrée :

Si l'utilisateur entre plus d'une lettre ou un caractère non alphabétique, le programme le signale mais ne gère pas toutes les entrées erronées de manière optimale.
Suggestion d'optimisation : Ajouter une validation plus stricte des entrées pour limiter l'utilisateur à une seule lettre à chaque essai.
Performances lors de la suggestion de lettres :

La fonctionnalité de suggestion de lettres peut être lente lorsque la liste de mots est très longue, car elle effectue une analyse probabiliste sur chaque mot restant.
Suggestion d'optimisation : Améliorer l'efficacité de l'algorithme de suggestion pour les grandes listes de mots.
Absence de persistance des données :

L'historique des parties n'est pas conservé. Le jeu redémarre à chaque nouvelle exécution.
Suggestion d'optimisation : Ajouter une fonctionnalité pour sauvegarder l'état du jeu ou enregistrer les scores des joueurs.
Affichage limité pour les longues listes de lettres saisies :

La zone d'affichage des lettres déjà saisies devient rapidement encombrée si beaucoup de lettres sont proposées.
Suggestion d'optimisation : Ajouter un défilement ou agrandir la zone d'affichage pour mieux gérer les longues listes de lettres.
