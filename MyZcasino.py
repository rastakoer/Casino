import os
import pandas as pd
import requests
from random import randrange
from math import ceil
import seaborn as sns
import matplotlib.pyplot as plt

#----------------------------------------------------
#Information sur le temps exterieur
#---------------------------------------------------
print("-------------------------------------------")
print("----Point METEO avec api openweathermap----")
print("-------------------------------------------")

#requete du temps actuel sur Caen
req = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Caen,fr&units=metric&APPID=91b573c4dc059854aa81154c3210a185")

#on transforme la requête en dataframe
reponse = req.json()
df = pd.json_normalize(reponse)
#display(df)

#Selection dans la data frame des elements qui nous interesse
temperature = df.at[0, 'main.temp']
vent = df.at[0, 'wind.speed']

#affichage
print("\n\nla température à Caen est de", temperature,"degrés et le vent souffle à", vent, "km/h")
print("Installez vous confortablement pour une partie de Roulette !!!\n\n")

#---------------------------------------------------------
# Programme du jeu
#-------------------------------------------------------

#---------------------------------------------------------
# Creation de mille lancés pour avoir des statistiques de départ
#-------------------------------------------------------

df_stat = pd.DataFrame(columns=["result", "one", "parite"])


for i in range(1000):
    nbcroupier = randrange(39)
    nbcroupier=int(nbcroupier)
    if nbcroupier%2 == 0:
        parite = 1
    else:
        parite = 0
    df_stat.loc[len(df_stat.index)] = [nbcroupier, 1, parite]



print("------------------------------------------")
print("-----------JEU DE LA ROULETTE-------------")
print("------------------------------------------")
print("")
print("Pour gagner il faut avoir le même numéro que le croupier ou la même parité")
print("")


#Demander avec quel somme le joueur commencer la partie en verifiant le montant du prtefeuille
portefeuille = -1
while portefeuille < 50 or portefeuille>1000:
    portefeuille= input(" montant à mettre sur la table (entre 50 et 1000) :")
    try:
        portefeuille=int(portefeuille)
    except ValueError:
        print("vous n'avez pas saisie de nombre")
        print("")
        portefeuille=-1
        continue
    if portefeuille <0:
        print("Vous devez mettre entre 50 et 1000$")
        print("")
    if portefeuille >1000:
        print("Vous ne pouvez pas vous installer à la table avec plus de 1000$")
        print("")
print("")
print("Vous vous installez à la table de roulette avec", portefeuille, "$.")
print("")


#Boucle de la partie 
finDePartie= 1
while portefeuille>0 and finDePartie==1:
    print("")
    print("----------------------------------")
    print("")
    nbjoueur = -1
    while nbjoueur < 0 or nbjoueur>38:
        nbjoueur= input(" sur quel numero voulez-vous miser (de 0 à 38) :")
        try:
            nbjoueur=int(nbjoueur)
        except ValueError:
            print("vous n'avez pas saisie un numero entre 0 et 38\n")
            nbjoueur=-1
            continue
        if nbjoueur <0 or nbjoueur >38:
            print("Vous devez mettre entre 1 et 38\n")
            

    mise = -1
    while mise <0 or mise > portefeuille:
        mise=input("combien voulez vous miser pour ce tour :")
        try:
            mise=int(mise)
        except ValueError:
            print("vous n'avez pas saisie un chiffre\n\n")
            continue
        if mise < 0 or mise >portefeuille:
            print("vous devez miser minimum 1$ et le montant maximum de votre portefeuille qui est de", portefeuille, "$\n\n")
            

    nbcroupier = randrange(39)
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
        print("Bravo vous gagner 0.5 x votre mise votre portefeuille est maintenant de ", portefeuille , "$\n")
    else:
        portefeuille+= -mise
        print("vous avez perdu, il vous reste", portefeuille,"$ à jouer\n")
        
        
#----------------------------------------------------------------------------------------
#           statistiques a l'aide de dataframe
#----------------------------------------------------------------------------------------
    if nbcroupier%2 == 0:
        parite = 1
    else :
        parite = 0
    df_stat.loc[len(df_stat.index)] = [nbcroupier, 1, parite]

    #affichage de tous les reultats
    #display(df_stat)

    #affichage du nombre de sortie par numéro
    df_nb_sortie_par_numero = df_stat.groupby("result").sum()
    #display(df_nb_sortie_par_numero)

    #affichage de pair impair
    df_parite = df_stat.groupby("parite").sum()
    #display(df_parite)

    #calcul du nombre de lancés effectués
    nb_jeu = len(df_stat.index)
    nb_jeu

    #calcul de pourcentage de parité
    pair = round((df_parite.iloc[0,1] * 100 / nb_jeu), 2)
    print("il y a", pair, "% de sorties impaire")

    #Affichage d'un tableau
    sns.barplot(data=df_nb_sortie_par_numero, x=df_nb_sortie_par_numero.index, y='one')
    plt.show()
    #display(df_stat.groupby("result").sum())


#------------------------------------------------------------------------
#    Fin de la boucle ? demander au jouer s'il a toujours envie de jouer
#-------------------------------------------------------------------------
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

