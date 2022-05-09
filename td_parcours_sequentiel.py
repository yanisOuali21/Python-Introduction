
def recherche1(liste,valeurs):
    for k in liste:
        if k == valeurs :
            return True
    return False

liste1=["a","b","c"]


def recherche2(liste,valeurs):
    trouve = False
    for element in liste:
        if element == valeurs :
            trouve = True
    return trouve
##
##
##liste1=[1,2,3,4,5,6]
##def recherche_indice(liste, valeur):
##    for k in liste  :
##        if k == valeur :
##            return liste.index(k)
        
def recherche_indice_v2(liste, valeur):
    """
    Description de la fonction : Renvoie l'indice de la valeur recherchée (None si valeur non présente)
    paramètre liste (list) : liste non vide
    paramètre valeur (type quelconque)
    Return (int ou Nonetype)
    """
    trouve = False
    k = 0
    while k < len(liste) and not trouve:
        trouve = liste[k] == valeur
        k = k + 1
    return trouve


def recherche_minimum(liste):
    """
    Description de la fonction : Renvoie la plus petite valeur de la liste
    paramètre liste (list) : liste non vide d'entiers(int), de nombres réels(float) ou de chaîne de caractères(str)
    Return (int)
    """
    min = liste[0]
    for element in liste:
        if element < min:
            min = element
    return min



def recherche_maximum(liste):
    """
    Description de la fonction : Renvoie la plus grande valeur de la liste
    paramètre liste (list) : liste non vide d'entiers(int), de nombres réels(float) ou de chaîne de caractères(str)
    Return (int)
    """
    max = liste[0]
    for element in liste:
        if element > max:
            max = element
    return max



def moyenne(liste):
    compteur_de_nombre=0
    addition=0
    for i in liste :
        addition=addition+i
        compteur_de_nombre=compteur_de_nombre+1
    moyenne_liste=addition/compteur_de_nombre
    return moyenne_liste
    

        
        

            
    
    