# Documentation du Projet

## Jeu du Pendu avec Tkinter

Ce projet implémente le classique jeu du pendu à l'aide de l'interface graphique Python Tkinter. Le joueur doit deviner un mot en proposant des lettres avant d'épuiser ses vies. Il inclut des fonctionnalités avancées comme la suggestion de lettres basée sur une analyse probabiliste.

---

## Table des matières

- Structure de l'application
- Fonctionnalités principales
- Prérequis
- Étapes d'installation et de configuration
  - Cloner le projet
  - Préparer le fichier mots.txt
  - Installer les dépendances
  - Lancer l'application
- Structure du projet
- Dépendances
- Problèmes connus et optimisations

---

## Structure de l'application

### 1. Interface graphique

- **Développée avec Tkinter**, elle offre une interface interactive et intuitive.
- Permet la saisie de lettres pour deviner le mot.
- Affiche l'état actuel du mot à deviner, les vies restantes et les lettres déjà proposées.
- Inclut un bouton pour **suggérer une lettre** basée sur une analyse probabiliste.

### 2. Système de jeu

- Gère la logique du jeu, y compris le calcul des vies restantes et la mise à jour dynamique du mot à deviner.
- Intègre une **fonctionnalité de suggestion de lettres** basée sur une probabilité calculée en fonction des mots restants.

---

## Fonctionnalités principales

1. **Interface graphique interactive**
   - Utilisation de Tkinter pour créer une expérience utilisateur agréable.

2. **Saisie des lettres**
   - L'utilisateur peut proposer une lettre pour deviner le mot.

3. **Système de vies**
   - Le joueur commence avec 7 vies et en perd une à chaque mauvaise devinette.

4. **Suggestion de lettres**
   - Une fonctionnalité avancée propose des lettres basées sur une analyse probabiliste des mots restants.

5. **Affichage dynamique**
   - Le mot à deviner est mis à jour à mesure que l'utilisateur propose des lettres.

6. **Fin du jeu**
   - Le jeu indique si le joueur a gagné ou perdu et affiche le mot final.

---

## Prérequis

Avant de pouvoir exécuter ce programme, vous devez :

- Avoir **Python 3.x** installé.
- Assurez-vous que le fichier contenant les mots (`mots.txt`) est accessible dans le répertoire du projet.

---

## Étapes d'installation et de configuration

### 1. Cloner le dépôt

Téléchargez le projet depuis GitHub :

```bash
git clone https://github.com/votre-utilisateur/jeu-du-pendu.git
cd jeu-du-pendu
```

### 2. Préparer le fichier mots.txt

- Créez un fichier texte nommé `mots.txt` contenant une liste de mots (un mot par ligne) dans le répertoire du projet.
- Exemple de contenu :
  ```
mot1
mot2
mot3
```

### 3. Installer les dépendances

Aucune bibliothèque externe n'est nécessaire pour ce projet. Cependant, si vous souhaitez garantir que toutes les dépendances standards sont à jour, exécutez :

```bash
pip install -r requirements.txt
```

Si le fichier `requirements.txt` n'est pas fourni, le projet repose uniquement sur **Tkinter**, inclus avec Python standard.

### 4. Lancer l'application

Exécutez le fichier Python principal (`pendu.py`) pour démarrer l'application :

```bash
python pendu.py
```

Cela ouvrira une fenêtre graphique dans laquelle vous pourrez jouer au jeu du Pendu.

---

## Structure du projet

- **`pendu.py`** : Code principal pour l'application.
- **`mots.txt`** : Fichier contenant les mots à deviner.
- **`README.md`** : Documentation détaillée du projet.

---

## Dépendances

Ce projet repose principalement sur :

- **Tkinter** : Bibliothèque graphique intégrée à Python.

Aucune installation supplémentaire n'est nécessaire si vous utilisez Python standard.

---

## Problèmes connus et optimisations

### Gestion des erreurs d'entrée

- Si l'utilisateur entre plus d'une lettre ou un caractère non alphabétique, le programme le signale mais ne gère pas toutes les entrées erronées de manière optimale.
- **Suggestion** : Ajouter une validation plus stricte des entrées pour limiter l'utilisateur à une seule lettre à chaque essai.

### Performances lors de la suggestion de lettres

- La fonctionnalité de suggestion de lettres peut être lente lorsque la liste de mots est très longue.
- **Suggestion** : Améliorer l'efficacité de l'algorithme de suggestion pour les grandes listes de mots.

### Absence de persistance des données

- L'historique des parties n'est pas conservé. Le jeu redémarre à chaque nouvelle exécution.
- **Suggestion** : Ajouter une fonctionnalité pour sauvegarder l'état du jeu ou enregistrer les scores des joueurs.

### Affichage limité pour les longues listes de lettres saisies

- La zone d'affichage des lettres déjà saisies devient rapidement encombrée si beaucoup de lettres sont proposées.
- **Suggestion** : Ajouter un défilement ou agrandir la zone d'affichage pour mieux gérer les longues listes de lettres.
