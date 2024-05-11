from tkinter import *
from random_word import RandomWords
import random

class JeuDuPendu:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Pendu")

        # Initialise le nombre de vies du joueur à 7.
        self.nb_vies = 7

        # Liste pour stocker les lettres saisies
        self.lettres_saisies = []

        # Fonction pour choisir un mot aléatoire dans le dictionnaire
        self.mot_a_deviner = self.choisir_mot()

        # Définir la couleur de fond de la fenêtre principale
        self.root.configure(bg="#FFDAB9")

        # Crée une étiquette pour afficher le titre du jeu centré en gros caractères et avec une couleur de fond et de texte spécifiée.
        self.label_titre = Label(root, text="Jeu du Pendu", font=("Arial", 36, "bold"), bg="#FFDAB9", fg="#8B0000")  # Titre centré, couleur rouge foncé
        self.label_titre.pack()

        # Crée une étiquette pour afficher le mot à deviner (masqué au début) avec une couleur de texte spécifiée.
        self.mot_affiche = StringVar()
        self.label_mot = Label(root, textvariable=self.mot_affiche, font=("Arial", 24), bg="#FFDAB9", fg="#8B0000")  # Couleur de texte rouge foncé
        self.label_mot.pack()

        # Crée une étiquette pour afficher le nombre de vies restantes du joueur avec une couleur de texte spécifiée.
        self.label_vies = Label(root, text=f"Vies restantes : {self.nb_vies}", font=("Arial", 14), bg="#FFDAB9", fg="#8B0000")  # Couleur de texte rouge foncé
        self.label_vies.pack()

        # Crée une zone de saisie de texte où l'utilisateur peut entrer une lettre.
        self.entree_lettre = Entry(root, font=("Arial", 14), bg="#FFA07A", state="normal")  # Couleur de fond saumon clair
        self.entree_lettre.pack()

        # Crée un bouton avec le texte "Devinez" qui déclenche la fonction
        self.bouton_deviner = Button(root, text="Devinez", command=self.verifier_lettre, bg="#CD5C5C", fg="white", state="normal")  # Couleurs de fond rouge indien et de texte blanc
        self.bouton_deviner.pack()

        # Crée une zone pour afficher les lettres saisies
        self.liste_lettres_saisies = Listbox(root, width=10, height=5, font=("Arial", 14), bg="#FFA07A", bd=0)  # Couleur de fond saumon clair, pas de bordure
        self.liste_lettres_saisies.pack()

        self.mettre_a_jour_affichage()

    # Fonction pour choisir un mot aléatoire dans le dictionnaire
    def choisir_mot(self):
        r = RandomWords()
        return r.get_random_word()

    # Fonction pour vérifier si une lettre est dans le mot
    def verifier_lettre(self):
        lettre_saisie = self.entree_lettre.get().lower()
        self.entree_lettre.delete(0, END)  # Effacer le contenu de l'entrée après la saisie
        if len(lettre_saisie) != 1 or not lettre_saisie.isalpha():
            resultat = "Veuillez entrer une seule lettre."
        elif lettre_saisie in self.mot_a_deviner:
            resultat = "Bonne devinette!"
            self.lettres_saisies.append(lettre_saisie)  # Ajouter la lettre saisie à la liste
            if set(self.mot_a_deviner).issubset(set(self.lettres_saisies)):
                resultat = "Félicitations, vous avez gagné !"
                self.entree_lettre.config(state="disabled")  # Désactiver la zone de saisie
                self.bouton_deviner.config(state="disabled")  # Désactiver le bouton de devinette
        else:
            resultat = "Mauvaise devinette!"
            self.nb_vies -= 1
        self.liste_lettres_saisies.insert(END, lettre_saisie)  # Afficher la lettre saisie dans la liste
        self.mettre_a_jour_affichage()
        if self.nb_vies <= 0:
            resultat += f" Vous avez perdu ! Le mot était : {self.mot_a_deviner}"
            self.entree_lettre.config(state="disabled")  # Désactiver la zone de saisie
            self.bouton_deviner.config(state="disabled")  # Désactiver le bouton de devinette
            self.label_mot_final = Label(root, text=f"Le mot était : {self.mot_a_deviner}", font=("Arial", 16), bg="#FFDAB9", fg="#8B0000")
            self.label_mot_final.pack()
        self.label_vies.config(text=f"Vies restantes : {self.nb_vies}")
        self.label_mot.config(text=resultat)

    # Fonction pour mettre à jour l'affichage du mot
    def mettre_a_jour_affichage(self):
        mot_affiche = ""
        for lettre in self.mot_a_deviner:
            mot_affiche += "_" if lettre not in self.lettres_saisies else lettre
        self.mot_affiche.set(mot_affiche)


# Création de la fenêtre principale
root = Tk()

# Création de l'instance du jeu
jeu = JeuDuPendu(root)

# Lancement de la boucle principale
root.mainloop()
