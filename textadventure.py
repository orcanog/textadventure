"""
Cours "Introduction 2" - Exercice "Text Adventure"
"""
personnage = {
    "PV": 70
}

mannequin = {
}

pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite"
]

lieux = [
    "Hall d'entrée",
    "Escalier",
    "Couloir du 1er étage",
    "Classe 1-A",
    "Couloir du 2e étage",
    "Caféteria",
    "Salle d'entraînement"
]

actions = [
    "Observer",
    "Quitter",
    "Manger",
    "Demander",
    "Montrer",
    "Combattre",
    "Attaquer",
    "Fuir"
]

plats = [
    "Ramen",
    "Onigiri",
    "Udon",
    "Curry"
]


plats_stock = {
    "Ramen": 2,
    "Onigiri": 2,
    "Udon": 2,
    "Curry": 2
}

objets_cles = ["smartphone"]
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************


def proposer_lieux(mots_cles):
    message = "|[Lieux]"
    print(message)
    mots_cles = [lieux[i] for i in mots_cles]
    print("", *mots_cles, sep="|")


def proposer_actions(action):
    message = "│[Actions] "
    print(message)
    action = [actions[i] for i in action]
    print("", *action, sep="|")


def combattre():
    while True:
        if mannequin["PV"] > 0:

            print("┌────────────────────────────────────────")
            proposer_actions([6, 7])
            print("|", personnage["PV"])
            print("|", mannequin["PV"])
            print("|(Utilise la première lettre de l'action pour choisir !)")
            reponse = (input("├─> "))
            print("└────────────────────────────────────────")

            if reponse == "A":
                print("J'attaque.")
                print("Tiens, prends ça !")
                mannequin["PV"] -= 15
                print("===============================")
                print("Le mannequin m'attaque...")
                personnage["PV"] -= 10
                print("Je suis encore debout, il t'en faudra plus que ça le mannequin !")
            elif reponse == "F":
                lieu_salle_entrainement()
            else:
                print("Hmm, je n'ai pas le droit de faire ça...")
        else:
            check_badge = bool("Badge" in inventaire)
            if check_badge == False:
                print("Félicitations, tu as gagné un badge !")
                inventaire["Badge"] = 1
                print("|", "Tu en as maintenant : ", inventaire["Badge"])
                lieu_salle_entrainement()
            elif check_badge == True:
                print("Félicitations, tu as gagné un badge !")
                inventaire["Badge"] += 1
                print("|", "Tu en as maintenant : ", inventaire["Badge"])
                lieu_salle_entrainement()
            elif (check_badge == True) and (inventaire["Badge"] == 3):
                print(
                    "Tu as déjà les 3 badges, le créateur du jeu tient quand même à saluer ta bravour !")
                lieu_salle_entrainement()


# ********************************************************************************
# INTRODUCTION
# ********************************************************************************


def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")

    # Nom du personnage et ajout dans le dictionnaire

    personnage["Nom"] = (input("\nComment t'appelles-tu ? "))

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"

    personnage["Age"] = int(input("\nQuel âge as-tu ? "))

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un

    print("\nVoici les pouvoirs disponibles : ")
    for key in pouvoirs:
        print("- {}, {}".format(key, pouvoirs.index(key)))

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"

    pouvoir_choisi = int(input("\nQuel pouvoir choisis-tu ? "))
    personnage["Pouvoir"] = pouvoirs[pouvoir_choisi]

    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"

    print("\nVoici votre personnage :")
    for key, values in personnage.items():
        print(key, ":", values)

    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************


def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([1])
        proposer_lieux([1])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "E":
            lieu_premier_etage()
        elif reponse == "Q":
            break
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


def lieu_premier_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("C'est le couloir du 1er étage.")
    print("On y trouve entre autres la classe 1-A.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([0])
        proposer_lieux([1, 3])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "O":
            print("Joli couloir mais on dirait qu'il reste encore quelques traces au sol, je peux apercevoir la classe 1-A d'ici !")
        elif reponse == "E":
            lieu_deuxieme_etage()
        elif reponse == "C":
            lieu_classe1A()
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


def lieu_classe1A():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es maintenant dans la salle de la classe 1-A")
    print("Le professeur te regarde fermer la porte.")
    print("Oh bonjour professeur !")
    print(f"Bonjour {personnage['Nom']} !")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([0, 3, 4])
        proposer_lieux([2])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "D":
            print("Pourrais-je avoir un passe s'il vous plaît ?")
            check_passe = bool("Passe" in objets_cles)
            if check_passe == False:
                print(
                    "- Voilà le passe, il te permettra d'accéder à la salle d'entraînement.")
                objets_cles.append("Passe")
            elif check_passe == True:
                print(
                    "- Désolé, je n'ai pas fait de copie du passe, le seul exemplaire existant est en ta possession...")
        elif reponse == "O":
            print("Tous mes camarades sont assis et attendent le début du cours, j'ai de la chance de pouvoir m'entraîner aujourd'hui !")
        elif reponse == "M":
            print("Professeur, regardez mes badges s'il vous plaît !")
            check_badge = bool("Badge" in inventaire)
            if check_badge == False:
                print(
                    "- Va te battre contre le mannequin qui se trouve dans la salle d'entraînement, faignant !")
            elif (check_badge == True) and (inventaire["Badge"] == 1):
                print("- Bravo, tu as un badge, tu es sur la bonne voie continue !")
            elif (check_badge == True) and (inventaire["Badge"] == 2):
                print(
                    "- Tu as deux badges. Aller, c'est la dernière étape, il te reste qu'un combat contre le mannequin, bon courage !")
            elif (check_badge == True) and (inventaire["Badge"] == 3):
                print("Tu as trois badges, félicitaitons, tu as gagné !")
                break
        elif reponse == "C":
            lieu_premier_etage()
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


def lieu_deuxieme_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("C'est le couloir du 2e étage.")
    print("Il est possible d'accéder à la cafétéria, à la salle d'entraînement ou de retourner au 1er étage.")
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([0])
        proposer_lieux([1, 5, 6])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "O":
            print("Joli couloir mais on dirait qu'il reste encore quelques traces au sol, je peux apercevoir la classe 1-A d'ici !")
        elif reponse == "E":
            lieu_premier_etage()
        elif reponse == "C":
            lieu_cafeteria()
        elif reponse == "S":
            check_passe = bool("Passe" in objets_cles)
            if check_passe == True:
                lieu_salle_entrainement()
            else:
                print(
                    "Hmm, la porte reste fermée, je crois que le professeur pourra m'aider.")
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


def lieu_cafeteria():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Te voilà dans la cafétéria, tu peux manger deux fois maximum chaque plat disponible.")
    print("Chaque plat consommé restaure 10 points de vie.")
    print("\nVoici la carte :")
    for key in plats:
        print(key)
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([0, 2])
        proposer_lieux([4])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "O":
            print(
                "La caféteria est bondée comme d'habitude... Oh, quelqu'un vient de faire tomber son plat, RIP.")
        elif reponse == "M":
            plat_choisi = input("Qu'est-ce que je mange ? ")
            check_plat = bool(plat_choisi in plats_stock)
            if check_plat == True :
                if plats_stock[plat_choisi] > 0:
                    personnage["PV"] += 10
                    print("Mes pv :", personnage["PV"])
                    plats_stock[plat_choisi] -= 1
                    print(f"Il me reste {plats_stock[plat_choisi]} de {plat_choisi}")
                else:
                        print("Impossible de manger ce plat.")
            else:
                print("Plat non proposé, relis la carte !")
                print("\nVoici la carte :")
                for key in plats:
                    print(key)
        elif reponse == "C":
            lieu_deuxieme_etage()
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


def lieu_salle_entrainement():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Te voici dans la salle d'entraînement, le lieu ultime où tu devras prouver ta valeur.")
    print("Le mannequin qui se trouve en face de toi possède 50 points de vie, ça devrait être un jeu d'enfant pour toi.")
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions([0, 5])
        proposer_lieux([4])
        print("|(Utilise la première lettre de l'action pour choisir !)")
        print("|(Utilise C2 pour le Couloir du 2e étage !)")
        reponse = (input("├─> "))
        print("└────────────────────────────────────────")

        if reponse == "O":
            print("Ça sent la transpiration dans cette salle, tous les héros sont passés par là c'est sûr, c'est à moi de briller aujourd'hui !")
        elif reponse == "C":
            mannequin["PV"] = 50
            combattre()
        elif reponse == "C2":
            lieu_deuxieme_etage()
        else:
            print("Hmm, je n'ai pas le droit de faire ça...")


# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
