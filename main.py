from fonctions import *

def menu():
    bibliotheque = charger_bibliotheque()
    while True:
        print("\n  MA BIBLIOTHÈQUE  ")
        print("1 Afficher tous les livres")
        print("2 Ajouter un livre")
        print("3 Supprimer un livre")
        print("4 Rechercher un livre")
        print("5 Marquer un livre comme lu")
        print("6 Afficher les livres lus")
        print("7 Afficher les livres non lus")
        print("8 Trier les livres")
        print("9 Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_comme_lu(bibliotheque)
        elif choix == "6":
            afficher_par_etat(bibliotheque, True)
        elif choix == "7":
            afficher_par_etat(bibliotheque, False)
        elif choix == "8":
            trier_livres(bibliotheque)
        elif choix == "9":
            sauvegarder_bibliotheque(bibliotheque)
            print(" Bibliothèque sauvegardée. À bientôt !")
            break
        else:
            print(" Choix invalide.")
            

if __name__ == "__main__":
    menu()
