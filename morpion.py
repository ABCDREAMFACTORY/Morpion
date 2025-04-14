morpion = ["","","","","","","","",""]
Erreur = 0


def Morpion(morpion, Joueur):
    if morpion[int(réponse)] == "":
        morpion[int(réponse)] = Joueur
        print(" |", morpion[0] , "|", morpion[1] , "|", morpion[2] , "|","\n"
            "----------","\n",
            "|", morpion[3] , "|", morpion[4] , "|", morpion[5] , "|","\n",
            "----------","\n",
            "|", morpion[6] , "|", morpion[7], "|" , morpion[8] , "|","\n") #Grille
        return True  # Move was valid
    else:
        print("La case est prise") 
        return False  # Move was invalid

Game = "NotFinish"
Joueur = 1
print(" |", morpion[0] , "|", morpion[1] , "|", morpion[2] , "|","\n"
       " ----------","\n",
       "|", morpion[3] , "|", morpion[4] , "|", morpion[5] , "|","\n",
        "----------","\n",
        "|", morpion[6] , "|", morpion[7], "|" , morpion[8] , "|","\n")
cpt = 0
while Game == "NotFinish":
    réponse = input("Au tour du joueur " + str(Joueur) + " ")
    while Erreur == 0:
        try:
            réponse = int(réponse)
            Erreur = 1
        except:
            print("Mettez un chiffre")
            réponse = input("Au tour du joueur " + str(Joueur) + " ")
    Erreur = 0
    while int(réponse) > 8 or int(réponse) < 0:
        print("Mettez une valeur entre 0 et 8")
        réponse = input("Au tour du joueur " + str(Joueur) + " ")

    if Morpion(morpion, Joueur):  # If the move was valid
        if morpion[0] == morpion[1] == morpion[2] != "" or morpion[4] == morpion[5] == morpion[6] != "" or morpion[6] == morpion[7] == morpion[8] != "" or morpion[0] == morpion[3] == morpion[6] != "" or morpion[1] == morpion[4] == morpion[7] != "" or morpion[2] == morpion[5] == morpion[8] != "" or morpion[0] == morpion[4] == morpion[8] != "" or morpion[2] == morpion[4] == morpion[6] != "":
            print("Le joueur " + str(Joueur) + " a gagné")
            Game = "Finish"
        cpt += 1
        if cpt == 9:
            print("Il y'a eu égalité")
            Game = "Finish"
        if Joueur == 1:
            Joueur = 2
        else:
            Joueur = 1
