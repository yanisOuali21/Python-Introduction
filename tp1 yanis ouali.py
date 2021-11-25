def bowling(boule1,boule2):
    if boule1 == 10 :
        print ("x")
    elif boule1+boule2 == 10 :
        print ("/")
    elif boule1+boule2 < 10 :
        print ("total")


    
    
def molky ( score, gain ):
    if score + gain == 50 :
        print ("victoire")
    elif score +gain >=50:
        print("25")
    else:
        print(score+gain)
        

def molko(score,gain,nbzerro):
     if score + gain == 50 :
        print ("victoire")
    elif score +gain >=50:
        print("25")
    elif nbzerros >= 2:
        print("perdu")
    else:
        print(score+gain)