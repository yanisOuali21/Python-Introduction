#exercice 1

def surface_disque(r):
    aire=(2*3.14*r)                        #code source de la fonction
    return aire

aire=surface_disque(2)       # ce n est pas un code source

#exercice 2

def acceuil2020 (nom,prenom,age):
    
    print("Bonjour",nom, prenom," vous avez ",age,"ans" )#code source de la fonction
    
#exercice 4
     
def tailleFichier(kio):
    taille_bits=(1024*8)*kio             # code source
    taille_octets=(1024)*kio  
    
    print("La taille de votre fichier est de",taille_octets,"octets et ",taille_bits,"bits") # ce n est pas un code source
    

#exercice 5

"""
réalise une conversion en °f eb °c
"""
def farenheigtToCelsius(tF):   # code source de la fonction
    tC=(tF-32)*5/9
    
    print (tF,"°F équivaut a ",tC,"°C") #ce n est pas un code source
    
    
#exercice 6
    
def calcul_cle(codesecuritersociale):  
    cle=codesecuritersociale % 97                    #code source de la fonction
    cle=97-cle
    
    print (cle)                                  
    