
   
n=0
while n<10:
    print(n," ", end="")
    n = n + 2
print(" ")
    

x=61
while x<100:
    print(x," ", end="")
    x = x + 2
print(" ")


def decroissant_for(n):
    k=n
    for i in range(n):
        print(k," ",end="")
        k=k-1
        
def decroissant_while(n):
    k=n
    while k!=0:
        print(k,end=" ")
        k=k-1


def somme1(n1, n2):
    S = 0
    k = n1
    while k < n2:
        S = S + k
        k = k + 1
    return(S)
print(somme1(1,5))

def somme2(n1, n2):
    S = 0
    k = n1
    while k < n2:
        k = k + 1
        S = S + k
    return(S)
print(somme2(1,5))

def somme1_for(n1, n2):
    S = 0
    k = n1
    for i in range(n2):
        S = S + k
        k = k + 1
    return(S)
print(somme1_for(1,5))

def somme2_for(n1,n2):
    S=0
    k = n1
    for i in range(n2):
        k = k + 1
        S = S + k
    return(S)
print(somme2_for(1,5))
print("exo5")

def nombre_alenvers(nombre):
    nombre_inverser=[]
    for i in nombre:
        nombre_inverser.append(i)
        nombre_inverser.reverse()
        print(nombre_inverser)
print(nombre_alenvers("1234"))
 
 
def is_palindrome(nombre):
    for i in range(len(nombre)//2):
        if nombre[i] != nombre[-i-1]:
            return False
    return True
   



    

    

    