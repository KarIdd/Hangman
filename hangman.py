#importation du module random
from random import *
# liste des mots du dictionnaire
mots=[]
# chargement du fichier dico.txt dans une variable nommé file
with open('dico.txt') as file:
    # extraction des mots du dictionnaire 
    for ligne in file:
        ligne=ligne.replace("\n","")
        mots.append(ligne)
# choix d'un mot du dictionnaire au hasard
mot_choisi=mots[randint(0,len(mots))]


#Definition de la longueur du mot
long_mot=len(mot_choisi)
#Création d'une variable où placer les lettres corrrectement devinées
mot_tiret=""
for i in range (long_mot):
    mot_tiret=mot_tiret+"-"
    
#Affectation de nombreuses variables qui seront utiles dans la suite du programme
mot_choisi2=mot_choisi
essai=6
end=0
dessin=0
win=0
lose=0

###################################################################################

#Fonction servant à stocker les dessins des différentes parties du pendu
def dessinPendu(nb):
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

###################################################################################

#Début de la recherche du pendu
while end < 1 :
    print(mot_tiret)
    print()
    #Demande de la lettre
    lettre=str(input("Donnez une lettre : "))
    #Conversion de la lettre en majuscule
    lettre=lettre.upper()
    #Nombre de fois qu'apparaît la lettre que l'on a choisi dans le mot à deviner
    nb_lettre=mot_choisi.count(lettre)
    #Le programme execute cette partie si la lettre choisi est présente dans le mot
    if nb_lettre >= 1 :
        #Mise à jour de la variable mot_tiret créé précedemment avec les lettres trouvées
        for i in range (nb_lettre):
            indice=mot_choisi.find(lettre)
            mot_tiret = mot_tiret[ : indice] + lettre + mot_tiret[indice + 1 : ]
            mot_choisi = mot_choisi[ : indice] + "-" + mot_choisi[indice + 1 : ]
    #Le programme execute cette partie si la lettre choisi n'est pas présente dans le mot
    else :
        #Le programme affiche un pendu différent en fonction du nombre d'erreur
        dessin=dessin+1
        print(dessinPendu(dessin))
        #Définition du nombre d'échecs restant avant de perdre
        essai=essai-1
    #Condition de victoire ou de défaite
    if mot_choisi2 == mot_tiret :
        end=end+1
        win=1
    elif essai==0:
        end=end+1
        lose=1

#Affichage de fin différent en fonction de la réussite ou de la défaite
if win==1:
    print()
    print("Bravo, vous avez trouvé le mot, il s'agissait en effet de",mot_choisi2)
elif lose ==1:
    print()
    print("Echec, vous n'avez pas trouvé le mot, il s'agissait de",mot_choisi2)
