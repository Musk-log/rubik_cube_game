import turtle
import random

taille = 50
couleurs = ["white", "yellow", "red", "orange", "blue", "green"]

turtle.width(3)

def carre(angle1, angle2):
    for i in [angle1, angle2, angle1 + 180, angle2 + 180]:
        turtle.setheading(i)
        turtle.forward(taille)

def face(angle1, angle2):
    for ligne in range(3):
        for colonne in range(3):
            turtle.penup()
            turtle.goto(0, 0)
            turtle.setheading(angle1)
            turtle.forward(ligne * taille)
            turtle.setheading(angle2)
            turtle.forward(colonne * taille)
            turtle.pendown()
            turtle.color("black", random.choice(couleurs))
            turtle.begin_fill()
            carre(angle1, angle2)
            turtle.end_fill()

face(30, 150)
face(150, 270)
face(30, 270)

turtle.done()