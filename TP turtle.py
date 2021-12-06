#exercice1

import turtle
turtle.forward(100)
turtle.left (90)
turtle.forward(100)
turtle.left (90)
turtle.forward(100)
turtle.left (90)
turtle.forward(100)
turtle.left (90)


#exercice2

for Turtle in range(4):
    turtle.forward(100)
    turtle.left(90)
    
#exercice3
    

 
def carre(pas):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine un carré
                                 et revienne au point de départ (même position et orientation)
    pas(int) : côté du carré
    return : None
    """
    for Turtle in range (4):
        turtle.forward(pas)
        turtle.left(90)
        

#exercice4

import turtle

def carreEmboite(pas,nb):
    for i in range(nb):
        turtle.forward(pas)
        turtle.left(90)
 