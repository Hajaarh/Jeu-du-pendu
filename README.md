# Jeu-du-pendu
Ce code développe le jeu du Pendu en Python avec Tkinter. Le joueur doit deviner un mot en proposant des lettres. Le jeu se termine lorsque le mot est deviné ou que le joueur perd toutes ses vies. Le programme utilise un modèle de régression logistique pour suggérer la prochaine lettre à deviner.


Ce script Python implémente le jeu du Pendu avec une interface graphique construite grâce à la bibliothèque Tkinter. Voici une présentation détaillée des différentes sections du code :

Importation de modules :
Le script débute par l'importation des modules essentiels :

messagebox de Tkinter permettant d'afficher des messages d'information.
random pour la génération de nombres aléatoires.
Counter de la bibliothèque collections pour compter les occurrences dans une liste.
ascii_lowercase de string pour obtenir l'ensemble des lettres minuscules de l'alphabet anglais.
LogisticRegression de scikit-learn pour le modèle de régression logistique.
numpy pour les calculs numériques.
tkinter pour la création de l'interface graphique.
Définition de la classe PenduApp :
Cette classe encapsule toutes les fonctionnalités du jeu :

Le constructeur __init__ initialise la fenêtre principale, les composants de l'interface utilisateur, le mot secret, etc.
Interface utilisateur :
Le jeu est présenté dans une fenêtre Tkinter contenant un titre, une zone pour deviner les lettres, un bouton pour soumettre une lettre, etc.

Logique de jeu :

La méthode deviner_lettre gère la logique pour deviner une lettre. Elle vérifie si la lettre est correcte ou non, met à jour les vies restantes, affiche des messages appropriés, etc.
cacher_mot masque les lettres non devinées du mot secret.
predict_next_letter prédit la prochaine lettre à deviner.
Entraînement du modèle de régression logistique :

Les données d'entraînement sont générées via la méthode generate_training_data.
Pour chaque lettre de l'alphabet, des échantillons positifs et négatifs sont créés.
Les échantillons sont ensuite fusionnés et utilisés pour entraîner le modèle de régression logistique.
Exécution principale :

La condition if __name__ == "__main__": assure que le code est exécuté uniquement lorsque le script est lancé directement et non lorsqu'il est importé comme module.
Une instance de PenduApp est créée et la boucle principale Tkinter est démarrée avec root.mainloop().
