import json
import os

# Fonction pour créer la bibliothèque initiale avec 5 livres

##########CREATION DE MON DICTIONNAIRE###############
# Fonction qui crée une bibliothèque de base 
# contenant 5 livres  sous forme de dictionnaires

def creer_bibliotheque_initiale():
    return [
        {"ID": 1, "Titre": "Nations Nègres et Culture", "Auteur": "Cheikh Anta Diop", "Année": 1954, "Lu": False, "Note": None},
        {"ID": 2, "Titre": "Une si longue lettre", "Auteur": "Mariama Bâ", "Année": 1979, "Lu": False, "Note": None},
        {"ID": 3, "Titre": "Le Vieux Nègre et la Médaille", "Auteur": "Ferdinand Oyono", "Année": 1956, "Lu": True, "Note": 8.5, "Commentaire": "Un classique poignant."},
        {"ID": 4, "Titre": "L'Aventure ambiguë", "Auteur": "Cheikh Hamidou Kane", "Année": 1961, "Lu": False, "Note": None},
        {"ID": 5, "Titre": "Les Soleils des Indépendances", "Auteur": "Ahmadou Kourouma", "Année": 1968, "Lu": True, "Note": 9, "Commentaire": "Très percutant sur l'Afrique post-coloniale."}
    ]

    
#########FIN DE MA CREATION DICTIONNAIRE######

##CHARGEMENT DE MA BIBLIOTHEQUE AVEC UN FICHIER JSON########
# Fonction qui charge la bibliothèque depuis le fichier JSON si disponible
def charger_bibliotheque():
    # Vérifie si le fichier bibliotheque.json existe
    if os.path.exists("bibliotheque.json"):
    # Si oui, ouvre le fichier en lecture et charge son contenu dans une liste Python
        with open("bibliotheque.json", "r") as f:
            return json.load(f)
    else:
        bibliotheque = creer_bibliotheque_initiale()
        # Sauvegarde cette nouvelle bibliothèque dans le fichier JSON
        sauvegarder_bibliotheque(bibliotheque)
        return bibliotheque
    
################SAUVEGARDE DANS MON DICTIONNAIRE##########
# Fonction qui sauvegarde la bibliothèque actuelle dans le fichier JSON
def sauvegarder_bibliotheque(bibliotheque):
    with open("bibliotheque.json", "w") as f:
        json.dump(bibliotheque, f, indent=4)
        
#######GENERER DES CLES UNIQUES #################
# Fonction qui génère un nouvel ID unique pour chaque livre ajouté
def generer_id(bibliotheque):
    return max((livre["ID"] for livre in bibliotheque), default=0) + 1

##############MA FONCTIONNE QUI AFFICHE MES LIVRES#############
# Fonction qui affiche la liste des livres de la bibliothèque
def afficher_livres(bibliotheque):
     # Si la bibliothèque est vide, affiche un message
    if not bibliotheque:
        print(" La bibliothèque est vide.")
         # Parcourt chaque livre de la bibliothèque et affiche ses informations
    for livre in bibliotheque:
        print(f"\nID: {livre['ID']}\nTitre: {livre['Titre']}\nAuteur: {livre['Auteur']}\nAnnée: {livre['Année']}\nLu: {'Oui' if livre['Lu'] else 'Non'}")
        if livre["Lu"]:
            print(f"Note: {livre['Note']}\nCommentaire: {livre.get('Commentaire', '')}")

###############FONCTION QUI AJOUTE UN LIVRE DANS MON DICTIONNAIRE #############
def ajouter_livre(bibliotheque):
    # Demande les informations du livre à l'utilisateur
     # Crée un dictionnaire pour le nouveau livre avec les entrées
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = int(input("Année de publication : "))
    livre = {
        "ID": generer_id(bibliotheque),# Appelle la fonction pour générer un nouvel ID
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,# Par défaut le livre est non lu
        "Note": None # Pas de note pour l'instant
    }
     # Ajoute ce livre à la bibliothèque
    bibliotheque.append(livre)
    # Affiche un message 
    print(" Livre ajouté avec succès !")
    
################FONCTION POUR SUPPRIMER UN LIVRE DANS MON DICTIONNAIRE#########
# Fonction qui permet de supprimer un livre de la bibliothèque
def supprimer_livre(bibliotheque):
    # Demande à l'utilisateur l'ID du livre à supprimer
    id_livre = int(input("Entrez l'ID du livre à supprimer : "))
    for livre in bibliotheque:
        # Parcourt la bibliothèque pour trouver le livre avec cet ID
        if livre["ID"] == id_livre:
            # Demande confirmation à l'utilisateur par ce que l'operation est irreversible
            confirmation = input(f"Confirmer la suppression de '{livre['Titre']}' ? (o/n) : ").lower()
            if confirmation == 'o':
                bibliotheque.remove(livre)
                print("🗑️ Livre supprimé.")
                return
            # Si aucun livre ne correspond à cet ID 
    print(" Livre introuvable.")
    
##################FONCTION QUI RECHERCHE UN LIVRE DANS MON DICTIONNAIRE###########
# Fonction qui permet de rechercher des livres par titre ou auteur
 # Demande à l'utilisateur un mot-clé pour la recherche
def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé pour la recherche : ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]
    afficher_livres(resultats) if resultats else print("Aucun livre trouvé.")
    
#########MARQUER LU UN LIVRE et METTRE COMMENTAIRE #################
# Fonction qui permet de marquer un livre comme lu et d'ajouter une note et un commentaire
def marquer_comme_lu(bibliotheque):
    # Demande l'ID du livre à l'utilisateur
    id_livre = int(input("ID du livre à marquer comme lu : "))
     # Parcourt la bibliothèque pour trouver le livre correspondant
    for livre in bibliotheque:
        if livre["ID"] == id_livre:
             # Marque le livre comme lu
            livre["Lu"] = True
             # Demande une note sur 10
            livre["Note"] = float(input("Attribuez une note sur 10 : "))
            livre["Commentaire"] = input("Commentaire : ")
            print("Livre mis à jour.")
            return
         # Si l'ID n'existe pas, affiche un message
    print(" Livre introuvable.")
    
# Fonction qui affiche uniquement les livres lus ou non lus selon l'option choisie    
 # Filtre la liste des livres selon s'ils sont lus ou non
def afficher_par_etat(bibliotheque, lu=True):
    livres = [livre for livre in bibliotheque if livre["Lu"] == lu]
    afficher_livres(livres) if livres else print("Aucun livre correspondant.")
    

# Fonction qui trie les livres selon un critère choisi par l'utilisateur
def trier_livres(bibliotheque):
    # Fonction qui trie les livres selon un critère choisi par l'utilisateur
    print("1 Année\n2 Auteur\n3 Note")
    choix = input("Votre choix : ")
    if choix == "1":
        bibliotheque.sort(key=lambda x: x["Année"])
    elif choix == "2":
        bibliotheque.sort(key=lambda x: x["Auteur"].lower())
    elif choix == "3":
        bibliotheque.sort(key=lambda x: (x["Note"] is None, x["Note"]))
    else:
        # Si le choix est invalide, affiche un message et quitte la fonction
        print(" Choix invalide.")
        return
    print(" Liste triée :")
    afficher_livres(bibliotheque)
