import turtle
import random

taille = 50 #ici j'ai définis la taille que devrais avoir chaque carré
couleurs = ["white", "yellow", "red", "orange", "blue", "green"] #j'ai utilisé une liste de couleur qui va me servir choisir une couleur au hasard plus tar

turtle.width(3) #ici j'ai définis l'épaisseur de la tortue

def carre(angle1, angle2): #les paramètre angle1 et angle2 me permettra de définir l'angle de d'inclinaison des côtés du carré de manière dynamique
    for i in [angle1, angle2, angle1 + 180, angle2 + 180]:
        turtle.setheading(i) #la fonction setheading permet d'orienter la tortue sous un angle indépendament de sa position précédent si vous comprenez pas trop, vous pouvez demander à chat ou consulter la documentation de python.org
        turtle.forward(taille)
#en gros la fonction cidessus permet de désinner une carrée par plusieurs, ne vous aissez pas berner par la boucle for

#j'ai utiliser des boucles imbriqué dans la fonction ci-dessous qui me permettra d'avoir des ligne et colonnes 
#c'est la fonction qui me permettra de déssiner une face du rubik et en l'appellant 3 fois avec différnt angle dans les paramètre me permettra d'avoir les différent
#face du rubik et tous assembler
def face(angle1, angle2):
    for ligne in range(3):
        for colonne in range(3):
            turtle.penup()
            turtle.goto(0, 0) #les 2 premières instruction de cete boucle permet de ramener la tortue à sa position de départ après chaque exécution sans pour autant désinner une ligne
            turtle.setheading(angle1) #ici on oriente la tortule sous une certaines angle qui sera déninis à l'appel de la fonction
            turtle.forward(ligne * taille) #on fait avancer la tortue à une distance égal à la ligne qui sera comprise entre 0 et 3 multiplier par sa tailler
            turtle.setheading(angle2)
            turtle.forward(colonne * taille) #c'est 2 instuction fait la même chose que les 2 qui les précédes mais avec des angles différente
            turtle.pendown() #puis on abaisse la tortue pour pouvoir déssiner
            turtle.color("black", random.choice(couleurs)) #là on défnis les bord de chaque carré avec du noir et on le remplis avec une couleur au hasa parmis les couleurs qu'on avait défnis dans notre liste
            turtle.begin_fill() #là on défnis la figure en remplir de couleur
            carre(angle1, angle2)
            turtle.end_fill()

face(30, 150) #appelle de la fonction pour désinner la face haut du rubik
face(150, 270) #celle pour déssiner celle de gauche
face(30, 270)#celle pour définir la face de droite
#NB: j'avais du mal à trouver les bons angles pour chaque face alors j'ai eu recours à chatgpt !!!

turtle.done() #cette instruction permet seulement de maintir la fenêtre ouvert jusqu'à ce qu'on le ferme manuellemen
