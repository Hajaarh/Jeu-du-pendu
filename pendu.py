# Importation du module messagebox de Tkinter pour afficher des messages d'information
from tkinter import messagebox
# Importation du module random pour générer des nombres aléatoires
import random
# Importation du module Counter pour compter les occurrences dans une liste
from collections import Counter
# Importation de la chaîne ascii_lowercase pour obtenir toutes les lettres minuscules de l'alphabet anglais
from string import ascii_lowercase
# Importation du modèle de régression logistique de scikit-learn
from sklearn.linear_model import LogisticRegression
# Importation du module numpy pour les calculs numériques
import numpy as np
# Importation du module tkinter pour créer l'interface graphique
import tkinter as tk


# Définition de la classe PenduApp
class PenduApp:
    def __init__(self, root):
        # Initialisation de la fenêtre principale
        self.root = root
        self.root.title("Jeu du Pendu")
        self.root.configure(bg="lightblue")  # Couleur de fond

        # Liste des mots possibles pour le jeu
        self.mots = ["chat", "chien", "poisson", "oiseau", "lapin", "accessoire", "accusée", "affirmation",
                     "agences", "architecture", "archéologue", "ascendants", "bienvenue", "biométrique",
                     "bricoleuse", "bureautique", "casino", "chorizo", "conductibilité", "conservateur",
                     "dysfonctionnement", "fermeture", "café", "fast-food", "globe-trotter", "mathématiciens",
                     "parachutage", "bateau", "boîte", "bouchon", "bouteille", "consciences", "conscient",
                     "conscription", "conscrit", "conseil", "conseiller", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne",
                     "lac", "mer", "océan", "espace", "réservation", "parc", "national", "régional", "naturel",
                     "protection", "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage",
                     "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc",
                     "national", "régional", "naturel", "protection", "conservation", "gestion", "environnement",
                     "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer",
                     "océan", "espace", "réservation", "parc", "national", "régional", "naturel", "protection",
                     "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage", "naturel",
                     "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc", "national",
                     "régional", "naturel", "protection", "conservation", "gestion", "environnement", "écologie",
                     "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne",
                     "lac", "mer", "océan", "espace", "réservation", "parc", "national", "régional", "naturel",
                     "protection", "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage",
                     "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc",
                     "national", "régional", "naturel", "protection", "conservation", "gestion", "environnement",
                     "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer",
                     "océan", "espace", "réservation", "parc", "national", "régional", "naturel", "protection",
                     "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage", "naturel",
                     "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc", "national",
                     "régional", "naturel", "protection", "conservation", "gestion", "environnement", "écologie",
                     "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne",
                     "lac", "mer", "océan", "espace", "réservation", "parc", "national", "régional", "naturel",
                     "protection", "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage",
                     "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc",
                     "national", "régional", "naturel", "protection", "conservation", "gestion", "environnement",
                     "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer",
                     "océan", "espace", "réservation", "parc", "national", "régional", "naturel", "protection",
                     "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage", "naturel",
                     "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc", "national",
                     "régional", "naturel", "protection", "conservation", "gestion", "environnement", "écologie",
                     "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne",
                     "lac", "mer", "océan", "espace", "réservation", "parc", "national", "régional", "naturel",
                     "protection", "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage",
                     "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc",
                     "national", "régional", "naturel", "protection", "conservation", "gestion", "environnement",
                     "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer",
                     "océan", "espace", "réservation", "parc", "national", "régional", "naturel", "protection",
                     "conservation", "gestion", "environnement", "écologie", "biodiversité", "sauvage", "naturel",
                     "parc", "forêt", "montagne", "lac", "mer", "océan", "espace", "réservation", "parc", "national",
                     "régional", "naturel", "protection", "conservation", "gestion", "environnement", "écologie",
                     "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne", "lac", "mer", "océan", "espace",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt"]



if __name__ == "__main__":
    root = tk.Tk()
    app = PenduApp(root)
    root.mainloop()
