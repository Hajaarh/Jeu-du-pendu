# Jeu-du-pendu
Ce code développe le jeu du Pendu en Python avec Tkinter. Le joueur doit deviner un mot en proposant des lettres. Le jeu se termine lorsque le mot est deviné ou que le joueur perd toutes ses vies. Le programme utilise un modèle de régression logistique pour suggérer la prochaine lettre à deviner.

Lorsque le joueur lance le jeu, une instance de la classe JeuDuPendu est créée, prenant en paramètres la fenêtre principale et une liste de mots à deviner.

Dans la méthode __init__, l'interface utilisateur est configurée avec des boutons, des étiquettes et une zone de saisie de texte. Le jeu initialise le nombre de vies, crée une liste pour stocker les lettres déjà saisies, choisit un mot aléatoire à deviner, et configure l'apparence de l'interface.

La méthode choisir_mot sélectionne aléatoirement un mot à partir de la liste de mots fournie.

Dans mon jeu du pendu, j'ai créé ma propre liste de mots que j'ai stockée dans un fichier texte que j'ai appelé "mots.txt". J'ai sélectionné des mots que je voulais inclure dans le jeu et je les ai simplement ajoutés à ce fichier. Ensuite, dans mon code, j'ai écrit une fonction appelée lire_mots qui lit les mots à partir de ce fichier et les stocke dans une liste. Cela me permet de facilement ajouter, modifier ou supprimer des mots du jeu en les modifiant dans le fichier texte.

Voici comment cela fonctionne : lorsque le jeu démarre, il charge cette liste de mots à partir du fichier texte en utilisant la fonction lire_mots. Ensuite, ces mots sont utilisés par le jeu pour choisir aléatoirement le mot à deviner. Cette approche me permet de personnaliser le jeu en choisissant les mots que je veux inclure, ce qui rend l'expérience de jeu plus unique et amusante pour moi et pour les joueurs.

La méthode suggerer_lettre propose une lettre au joueur en se basant sur une analyse probabiliste des lettres restantes à deviner. Elle calcule la probabilité de chaque lettre en fonction des mots possibles et suggère celle avec la probabilité la plus élevée.

La méthode calculer_proba_lettre calcule la probabilité qu'une lettre soit dans le mot à deviner en se basant sur les lettres déjà devinées et les mots possibles à deviner.

La méthode verifier_lettre vérifie si la lettre saisie par le joueur est dans le mot à deviner. Si c'est le cas, elle met à jour l'affichage du mot et vérifie si le joueur a gagné. Sinon, elle réduit le nombre de vies et affiche un message indiquant que la devinette était incorrecte.

La méthode mettre_a_jour_affichage met à jour l'affichage du mot à deviner en remplaçant les lettres non devinées par des tirets.

Ces méthodes sont essentielles pour le fonctionnement du jeu du pendu, fournissant une expérience interactive au joueur à travers une interface graphique conviviale.

Dans le code du jeu du pendu, la classification est implicitement utilisée pour deviner le mot caché et suggérer des lettres au joueur.

Choix du mot à deviner : Un mot est choisi aléatoirement parmi une liste de mots disponibles, chaque mot représentant une classe potentielle.

Suggestion de lettre : Le jeu suggère une lettre en se basant sur une analyse probabiliste des lettres déjà saisies et des mots possibles restants, classant ainsi chaque lettre comme la plus probable à apparaître dans le mot.

Vérification de la lettre saisie : Lorsque le joueur entre une lettre pour deviner le mot, le jeu vérifie si cette lettre est présente dans le mot à deviner, classant ainsi la lettre comme correcte ou incorrecte.

Mise à jour de l'affichage du mot : L'affichage du mot est mis à jour pour montrer les lettres correctement devinées et les tirets pour les lettres encore inconnues, classant ainsi chaque lettre comme devinée ou non devinée.

Bien que le code n'utilise pas explicitement des algorithmes de classification, il utilise les principes de classification pour implémenter le jeu du pendu, où chaque lettre est classée dans le contexte du mot à deviner.
