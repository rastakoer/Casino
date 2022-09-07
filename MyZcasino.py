import os
from random import randrange
from math import ceil
print("------------------------------------------")
print("-----------JEU DE LA ROULETTE-------------")
print("------------------------------------------")
print("")
print("Pour gagner il faut avoir le même numéro que le croupier ou la même parité")
print("")
#Demander avec quel somme le joueur commencer la partie
portefeuille = -1
while portefeuille < 0 or portefeuille>1000:
    portefeuille= input(" montant à mettre sur la table :")
    try:
        portefeuille=int(portefeuille)
    except ValueError:
        print("vous n'avez pas saisie de nombre")
        print("")
        portefeuille=-1
        continue
    if portefeuille <0:
        print("Vous devez mettre entre 0 et 1000$")
        print("")
    if portefeuille >1000:
        print("Vous ne pouvez pas vous installer à la table avec plus de 1000$")
        print("")
print("")
print("Vous vous installez à la table de roulette avec", portefeuille, "$.")
print("")

finDePartie= 1
while portefeuille>0 and finDePartie==1:
    print("")
    print("----------------------------------")
    print("")
    nbjoueur = -1
    while nbjoueur < 1 or nbjoueur>50:
        nbjoueur= input(" sur quel numero voulez-vous miser :")
        try:
            nbjoueur=int(nbjoueur)
        except ValueError:
            print("vous n'avez pas saisie un numero entre 1 et 50")
            print("")
            nbjoueur=-1
            continue
        if nbjoueur <1 or nbjoueur >50:
            print("Vous devez mettre entre 1 et 50")
            print("")

    mise = -1
    while mise <0 or mise > portefeuille:
        mise=input("combien voulez vous miser pour ce tour :")
        try:
            mise=int(mise)
        except ValueError:
            print("vous n'avez pas saisie un chiffre")
            print("")
            continue
        if mise < 0 or mise >portefeuille:
            print("vous devez miser minimum 1$ et le montant maximum de votre portefeuille qui est de", portefeuille, "$")
            print("")

    nbcroupier = randrange(50)
    nbcroupier=int(nbcroupier)
    print("                  -----------------")
    print("votre numéro est le", nbjoueur , "celui du croupier est le", nbcroupier)
    print("                  -----------------")

    if nbcroupier == nbjoueur:
        portefeuille+=mise*3
        print("Bravo vous gagner 3 x votre mise votre portefeuille est maintenant de ", portefeuille , "$")
        print("")
    elif nbjoueur%2 == nbcroupier%2:
        portefeuille+=mise*0.5
        print("Bravo vous gagner 0.5 x votre mise votre portefeuille est maintenant de ", portefeuille , "$")
        print("")
    else:
        portefeuille+= -mise
        print("vous avez perdu, il vous reste", portefeuille,"$ à jouer")
        print("")
        


    condition=0
    while condition<1 or condition>2:
        condition=input("voulez-vous continuer 1:oui 2:non :")
        try:
            condition=int(condition)
        except ValueError:
            print("Vous devez saisair 1 pour continuer ou 2 pour arrêter")
            print("")
            continue
        if condition<1 or condition>2:
            print("Vous devez saisair 1 pour continuer ou 2 pour arrêter")
            print("")

    finDePartie=condition


if portefeuille==0:
    print("-----------------------------------")
    print("-------Vous êtes fauché !!!!-------")
    print("-----------------------------------")
else :
    print("---------------------------------------------")
    print("-----Vous quittez la table avec ", portefeuille,"$------")
    print("---------------------------------------------")




# On met en pause le système (Windows)
os.system("pause")

