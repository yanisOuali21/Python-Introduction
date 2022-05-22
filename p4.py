ligne=6
colonne=7
tableau =[[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]

def afficheTableau():
    for l in range (ligne):
        for c in range (colonne) :
            print (tableau[l][c] , end = " " )
        print()
        
        
def diagonale():
    for i in range (ligne-3):
        cpt=0
        for c in range (colonne-1):
            if (tableau[l][c] == tableau[l+c][c]) and tableau[l][c] != '.':
                cpt = cpt+1
                if cpt ==3:
                    print (" c est gagner " )