# Importation du module tkinter pour créer l'interface graphique
import tkinter as tk


# Définition de la classe PenduApp
class PenduApp:
    def __init__(self, root):
        # Initialisation de la fenêtre principale
        self.root = root
        self.root.title("Jeu du Pendu")
        self.root.configure(bg="#FFDAB9")  # Couleur de fond pêche clair

        # Liste des mots possibles pour le jeu
        self.mots = ["chat", "chien", "poisson", "oiseau", "lapin", "accessoire", "accusée", "affirmation",
                     "agences", "architecture", "archéologue", "ascendants", "bienvenue", "biométrique",
                     "bricoleuse", "bureautique", "casino", "chorizo", "conductibilité", "conservateur",
                     "dysfonctionnement", "fermeture", "café", "fast-food", "globe-trotter", "mathématiciens",
                     "parachutage", "bateau", "boîte", "bouchon", "bouteille", "consciences", "conscient",
                     "conscription", "conscrit", "conseil", "conseiller", "voiture", "livre", "fenêtre", "ordinateur",
                     "jardin", "maison", "route", "montagne", "plage", "vacances", "argent", "banque", "amour", "famille",
                     "fleurs", "soleil", "lune", "étoile", "oiseaux", "poèmes", "médecin", "hôpital", "maladie", "remède",
                     "blessure", "sport", "football", "basket-ball", "tennis", "vélo", "cheval", "voile", "piano",
                     "guitare", "violon", "danse", "peinture", "sculpture", "musée", "théâtre", "cinéma", "télévision",
                     "journal", "radio", "ordinateur", "internet", "téléphone", "mail", "message", "amitié", "rencontre",
                     "discussion", "rire", "joie", "pleur", "tristesse", "colère", "désir", "espoir", "rêve", "aventure",
                     "voyage", "découverte", "courage", "peur", "danger", "magie", "mystère", "fantôme", "monstre", "dragon",
                     "fée", "superhéros", "superpuissance", "invention", "découverte", "exploration", "conquête",
                     "science", "technologie", "espace", "planète", "galaxie", "univers", "histoire", "géographie",
                     "français", "mathématiques", "sciences", "physique", "chimie", "biologie", "langue", "grammaire",
                     "orthographe", "vocabulaire", "lecture", "écriture", "poésie", "théâtre", "musique", "peinture",
                     "sculpture", "architecture", "religion", "philosophie", "politique", "économie", "sociologie",
                     "psychologie", "éducation", "formation", "emploi", "chômage", "salaire", "travail", "entreprise",
                     "industrie", "commerce", "marketing", "publicité", "management", "leadership", "motivation",
                     "productivité", "efficacité", "performance", "stratégie", "gestion", "finance", "comptabilité",
                     "audit", "contrôle", "taxe", "budget", "investissement", "crédit", "dette", "épargne", "retraite",
                     "assurance", "immobilier", "location", "propriété", "achat", "vente", "marché", "concurrence",
                     "consommation", "énergie", "environnement", "climat", "pollution", "développement", "durabilité",
                     "écologie", "agriculture", "alimentation", "santé", "hygiène", "nutrition", "médecine", "maladie",
                     "prévention", "traitement", "pharmacie", "hôpital", "soins", "patients", "médecin", "infirmier",
                     "psychologue", "psychiatre", "dentiste", "ophtalmologue", "chirurgien", "anesthésiste", "radiologue",
                     "biologiste", "vétérinaire", "pharmacien", "recherche", "découverte", "expérimentation", "laboratoire",
                     "thèse", "publi", "conférence", "réunion", "formation", "éducation", "apprentissage", "enseignement",
                     "professeur", "élève", "étudiant", "école", "collège", "lycée", "université", "formation", "diplôme",
                     "baccalauréat", "licence", "master", "doctorat", "ingénieur", "mécanique", "électrique", "informatique",
                     "chimique", "aérospatial", "civil", "industriel", "ingénierie", "construction", "conception", "projet",
                     "développement", "fabrication", "production", "maintenance", "système", "réseau", "logiciel", "application",
                     "site", "web", "internet", "donnée", "information", "programmation", "langage", "algorithmique",
                     "structure", "donnée", "base", "données", "SQL", "NoSQL", "big", "data", "analyse", "statistique",
                     "machine", "apprentissage", "intelligence", "artificiel", "réalité", "virtuel", "augmenté", "image",
                     "vidéo", "son", "audio", "texte", "traitement", "langage", "naturel", "traduction", "interprétation",
                     "synthèse", "voix", "synthétique", "robotique", "automatisation", "capteur", "actionneur", "microcontrôleur",
                     "arduino", "raspberry", "pi", "domotique", "maison", "intelligente", "sécurité", "surveillance",
                     "alarme", "contrôle", "accès", "automobile", "véhicule", "autonome", "voiture", "conduite",
                     "assistée", "navigation", "GPS", "cartographie", "guidage", "parcours", "système", "information",
                     "transport", "mobil", "route", "rail", "aérien", "maritime", "logistique", "gestion", "flux",
                     "stock", "supply", "chain", "achat", "approvisionnement", "distribution", "commerce", "électronique",
                     "m", "commerce", "paiement", "sécurisé", "livraison", "client", "relation", "service", "clientèle",
                     "satisfaction", "fidélisation", "expérience", "utilisateur", "marketing", "digital", "réseaux",
                     "sociaux", "promotion", "campagne", "communication", "publicitaire", "relation", "presse", "événement",
                     "salon", "exposition", "foire", "manifestation", "concert", "spectacle", "sport", "culture",
                     "divertissement", "loisir", "jeu", "casino", "pari", "loterie", "jeu", "vidéo", "console",
                     "ordinateur", "mobile", "smartphone", "tablette", "application", "web", "jeu", "société", "carte",
                     "plateau", "figurine", "rôle", "jeu", "éducatif", "pédagogique", "simulation", "stratégie",
                     "réflexion", "adresse", "chance", "hasard", "logique", "observation", "mémoire", "réflexe",
                     "concentration", "créativité", "imagination", "détente", "amusant", "amusement", "plaisir",
                     "passion", "intérêt", "fascinant", "captivant", "enthousiasme", "excitant", "adrenaline",
                     "émotion", "suspense", "aventure", "exploration", "découverte", "émerveillement", "curiosité",
                     "interrogation", "étonnement", "surprise", "question", "réponse", "énigme", "devinette", "mystère",
                     "secret", "défi", "challenge", "objectif", "but", "réussite", "victoire", "échec", "défaite",
                     "opportunité", "chance", "risque", "danger", "obstacle", "difficulté", "problème", "erreur",
                     "faute", "confusion", "malentendu", "problème", "mésentente", "controverse", "débat", "dispute",
                     "discussion", "argument", "critique", "jugement", "opinion", "point", "vue", "perspective",
                     "position", "interprétation", "compréhension", "analyse", "raisonnement", "logique", "principe",
                     "théorie", "hypothèse", "méthode", "technique", "approche", "stratégie", "plan", "action", "solution",
                     "alternative", "compromis", "adaptation", "ajustement", "révision", "réforme", "innovation", "changement",
                     "transformation", "transition", "adaptation", "évolution", "mutation", "révolution", "progression",
                     "développement", "croissance", "expansion", "amélioration", "optimisation", "perfectionnement",
                     "efficacité", "performance", "rendement", "qualité", "excellence", "standard", "norme", "valeur",
                     "mérite", "récompense", "reconnaissance", "satisfaction", "bien-être", "bonheur", "joie", "plaisir",
                     "sérénité", "équilibre", "harmonie", "paix", "tranquillité", "calme", "santé", "bien-être",
                     "fitness", "forme", "vitalité", "énergie", "force", "endurance", "résistance", "robustesse",
                     "souplesse", "agilité", "mobilité", "coordination", "équilibre", "puissance", "force", "musculaire",
                     "masse", "graisse", "perte", "poids", "régime", "alimentaire", "nutrition", "hygiène", "soin",
                     "beauté", "apparence", "image", "style", "mode", "tendance", "élégance", "charme", "attrait",
                     "sex-appeal", "séduction", "flirt", "romance", "relation", "sentimentale", "couple", "amour",
                     "passion", "engagement", "mariage", "relation", "amicale", "amitié", "complicité", "confiance",
                     "loyauté", "sincérité", "solidarité", "entraide", "support", "écoute", "attention", "compréhension",
                     "conseil", "aide", "assistance", "réconfort", "affection", "tendresse", "douceur", "attention",
                     "gentillesse", "respect", "courtoisie", "politesse", "gentillesse", "bienveillance", "tolérance",
                     "patience", "compréhension", "acceptation", "adaptation", "ouverture", "flexibilité", "adaptabilité",
                     "apprentissage", "éducation", "curiosité", "découverte", "expérience", "connaissance", "savoir",
                     "culture", "tradition", "coutume", "valeurs", "croyance", "spiritualité", "religion", "philosophie",
                     "sagesse", "principe", "éthique", "morale", "justice", "droit", "égalité", "liberté", "fraternité",
                     "solidarité", "paix", "harmonie", "union", "coopération", "collaboration", "association", "alliance",
                     "coalition", "partenariat", "équipe", "groupe", "collectif", "société", "communauté", "population",
                     "peuple", "nation", "état", "gouvernement", "administration", "autorité", "pouvoir", "régime",
                     "politique", "politicien", "diplomatie", "affaire", "relation", "internationale", "conflit", "crise",
                     "guerre", "terrorisme", "paix", "sécurité", "défense", "armée", "soldat", "force", "intervention",
                     "mission", "opération", "stratégie", "tactique", "arme", "munition", "bombe", "explosion", "attaque",
                     "défense", "résistance", "victime", "blessé", "mort", "sécurité", "prévention", "protection",
                     "sécurité", "sécuritaire", "risque", "danger", "alerte", "alarme", "catastrophe", "accident",
                     "incendie", "inondation", "tempête", "cataclysme", "catastrophe", "sauvetage", "aide", "humanitaire",
                     "solidarité", "secours", "volontaire", "bénévole", "association", "ONG", "organisation", "mondiale",
                     "agence", "internationale", "coopération", "développement", "aide", "étranger", "étranger",
                     "tourisme", "voyage", "visite", "découverte", "exploration", "aventure", "détente", "plaisir",
                     "divertissement", "loisir", "découverte", "émerveillement", "culture", "tradition", "coutume",
                     "patrimoine", "monument", "site", "historique", "nature", "faune", "flore", "biodiversité",
                     "environnement", "forêt", "jungle", "montagne", "mer", "océan", "plage", "désert", "paysage",
                     "panorama", "vue", "coucher", "soleil", "lever", "lune", "étoile", "ciel", "nuage", "pluie",
                     "neige", "vent", "tempête", "orage", "foudre", "tonnerre", "arc-en-ciel", "éclair", "énergie",
                     "solaire", "éolienne", "hydroélectrique", "nucléaire", "fossile", "charbon", "pétrole", "gaz",
                     "renouvelable", "propre", "écologique", "économie", "énergie", "électricité", "gaz", "carburant",
                     "essence", "diesel", "éthanol", "biogaz", "biocarburant", "hydrogène", "moteur", "combustion",
                     "pollution", "émission", "gaz", "effet", "serre", "climat", "changement", "réchauffement",
                     "glacier", "banquise", "fonte", "dégel", "froid", "gèle", "gel", "température", "minimum",
                     "maximum", "météo", "climat", "tempête", "cyclone", "ouragan", "tornade", "tremblement", "terre",
                     "volcan", "séisme", "tsunami", "inondation", "avalanche", "catastrophe", "danger", "alerte",
                     "prévention", "sécurité", "risque", "sécuritaire", "séisme", "glissement", "terrain", "érosion",
                     "dégradation", "désertification", "déforestation", "déboisement", "pollution", "eau", "air",
                     "sol", "déchet", "ordure", "détritus", "poubelle", "recyclage", "tri", "sélectif", "environnement",
                     "écologie", "nature", "biodiversité", "écosystème", "espèce", "animale", "végétale", "faune",
                     "flore", "milieu", "naturel", "sauvage", "forêt", "jungle", "marécage", "lac", "étang", "rivière",
                     "torrent", "cascade", "chute", "mer", "océan", "plage", "désert", "montagne", "volcan", "terre",
                     "sable", "pierre", "roche", "sol", "minéral", "montagne", "colline", "vallée", "plaine", "plateau",
                     "prairie", "herbe", "pelouse", "parc", "jardin", "forêt", "bois", "arbre", "tronc", "branche",
                     "feuille", "fleur", "fruit", "racine", "tige", "écorce", "sève", "nature", "animal", "végétal",
                     "champignon", "herbivore", "carnivore", "omnivore", "prédateur", "proie", "insecte", "arachnide",
                     "invertébré", "vertébré", "poisson", "oiseau", "mammifère", "reptile", "amphibien", "espèce",
                     "sauvage", "menacée", "protégée", "disparue", "extinction", "faune", "flore", "biodiversité",
                     "réservation", "parc", "national", "régional", "naturel", "protection", "conservation", "gestion",
                     "environnement", "écologie", "biodiversité", "sauvage", "naturel", "parc", "forêt", "montagne",
                     "lac", "mer", "océan", "espace", "réservation", "parc", "national", "régional", "naturel", "protection",
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

        # Sélectionne aléatoirement un mot parmi une liste prédéfinie de mots.
        self.mot_secret = random.choice(self.mots)

        # Initialise un ensemble vide pour stocker les lettres devinées par le joueur.
        self.lettres_devinées = set()

        # Initialise le nombre de vies du joueur à 7.
        self.nb_vies = 7

        # Crée une étiquette pour afficher le titre du jeu centré en gros caractères et avec une couleur de fond et de texte spécifiée.
        self.label_titre = tk.Label(root, text="Jeu du Pendu", font=("Arial", 36, "bold"), bg="#FFDAB9", fg="#8B0000")  # Titre centré, couleur rouge foncé
        self.label_titre.pack()

        # Crée une étiquette pour afficher le mot à deviner (masqué au début) avec une couleur de texte spécifiée.
        self.label_mot = tk.Label(root, text=self.cacher_mot(), font=("Arial", 24), bg="#FFDAB9", fg="#8B0000")  # Couleur de texte rouge foncé
        self.label_mot.pack()

        # Crée une étiquette pour afficher le nombre de vies restantes du joueur avec une couleur de texte spécifiée.
        self.label_vies = tk.Label(root, text=f"Vies restantes : {self.nb_vies}", font=("Arial", 14), bg="#FFDAB9", fg="#8B0000")  # Couleur de texte rouge foncé
        self.label_vies.pack()

        # Crée une zone de saisie de texte où l'utilisateur peut entrer une lettre.
        self.entree_lettre = tk.Entry(root, font=("Arial", 14), bg="#FFA07A")  # Couleur de fond saumon clair
        self.entree_lettre.pack()

        # Crée un bouton avec le texte "Devinez" qui déclenche la fonction
        self.bouton_deviner = tk.Button(root, text="Devinez", command=self.deviner_lettre, bg="#CD5C5C", fg="white")  # Couleurs de fond rouge indien et de texte blanc
        self.bouton_deviner.pack()

        # Création du modèle de régression logistique
        self.alphabet = ascii_lowercase
        self.model = LogisticRegression()

        # Génération des données pour le modèle
        self.X_train, self.y_train = self.generate_training_data()

        # Ajustement du modèle
        self.model.fit(self.X_train, self.y_train)

    def cacher_mot(self):
        """Masque les lettres non devinées du mot secret."""
        return ' '.join(char if char in self.lettres_devinées else '_' for char in self.mot_secret)  # Espaces entre chaque lettre

    def deviner_lettre(self):
        """Gère la logique pour deviner une lettre."""
        if self.nb_vies <= 0:
            # Affichage du message de fin de partie si les vies sont épuisées
            messagebox.showinfo("Fin de partie", "Le jeu est terminé. Vous avez épuisé toutes vos vies.")
            return

        lettre = self.entree_lettre.get().lower()
        self.entree_lettre.delete(0, tk.END)

        if lettre in self.lettres_devinées:
            # Affichage du message si la lettre a déjà été devinée
            messagebox.showinfo("Déjà deviné", f"Vous avez déjà deviné la lettre {lettre}.")
            return

        self.lettres_devinées.add(lettre)

        if lettre in self.mot_secret:
            if all(char in self.lettres_devinées for char in self.mot_secret):
                # Affichage du message de félicitations si le mot complet est deviné
                messagebox.showinfo("Félicitations", f"Vous avez deviné le mot : {self.mot_secret}")
            else:
                # Affichage du mot avec les lettres devinées
                self.label_mot.config(text=self.cacher_mot())
        else:
            # Décrémentation du nombre de vies et affichage du message si le joueur se trompe
            self.nb_vies -= 1
            self.label_vies.config(text=f"Vies restantes : {self.nb_vies}")
            if self.nb_vies == 0:
                messagebox.showinfo("Vies épuisées", "Vos vies sont épuisées. Peut-être une prochaine fois !")
                # Désactivation des éléments de l'interface à la fin de la partie
                self.entree_lettre.config(state="disabled")
                self.bouton_deviner.config(state="disabled")
                # Affichage du mot secret à la fin de la partie
                messagebox.showinfo("Mot à deviner", f"Le mot à deviner était : {self.mot_secret}")

        # Prédiction de la prochaine lettre à deviner
        prochaine_lettre = self.predict_next_letter()
        messagebox.showinfo("Prochaine lettre à deviner", f"Prochaine lettre à deviner : {prochaine_lettre}")

    def generate_training_data(self):
        """Génère les données d'entraînement pour le modèle."""
        X_train = []
        y_train = []

        for letter in self.alphabet:
            # Génération des échantillons positifs et négatifs pour chaque lettre
            X_positive = self.generate_sample(letter, positive=True)
            y_positive = [1] * len(X_positive)

            X_negative = self.generate_sample(letter, positive=False)
            y_negative = [0] * len(X_negative)

            # Fusion des échantillons positifs et négatifs
            X_train.extend(X_positive)
            X_train.extend(X_negative)
            y_train.extend(y_positive)
            y_train.extend(y_negative)

        return np.array(X_train), np.array(y_train)

    def generate_sample(self, letter, positive=True):
        """Génère un échantillon pour une lettre donnée."""
        sample = []

        for _ in range(100):
            # Ajout de la lettre actuelle comme lettre devinée
            guessed_letters = [0] * 26
            guessed_letters[ord(letter) - ord('a')] = 1

            # Si l'échantillon est négatif, ajout de lettres aléatoires comme lettres devinées
            if not positive:
                for _ in range(3):
                    random_index = random.randint(0, 25)
                    guessed_letters[random_index] = 1

            sample.append(guessed_letters)

        return sample

    def predict_next_letter(self):
        # Prédit la prochaine lettre à deviner.
        return random.choice(self.alphabet)  # Choix aléatoire d'une lettre

if __name__ == "__main__":
    root = tk.Tk()
    app = PenduApp(root)
    root.mainloop()
