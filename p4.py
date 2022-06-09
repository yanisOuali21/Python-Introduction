def genere_grille():
    grille = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    return grille
    
def affiche_grille(grille):
    for k in range(6):
        print(grille[5-k])
    print (' 0  1  2  3  4  5  6 ')
    print (21* '_')
    

def grille_pleine(grille):
    
    grille_remplie = True
    for k in grille :
        for valeur in k :
            if valeur == 0 :
                grille_remplie = False
                break
        return grille_remplie
    

def alignement_horizontal(grille,position,joueur):
    lst = position[0]
    i = position [1]
    nbc = len(grille[lst])
    cpt = 0
    alignement = False
    while cpt != 4 and nbc > 0:
        for k in grille [lst]:
            if cpt == 4:
                alignement = True
            elif k == joueur :
                cpt += 1
                nbc -=1
            else :
                cpt = 0
                nbc -=1
        return alignement
            



