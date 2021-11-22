import random

a = 0 #Bak 1
b = 0 #Bak 2

c = random.randint(15,35) #Willekeurig aantal knikkers tussen 15 en 35

def VerdeelKnikkers():

    global a
    global b

    print("Aantal knikkers om te verdelen: " + str(c))

    a = random.randint(1,c)
    print("Aantal knikkers in bak 1: " + str(a))


    d = c-a
    print("Aantal knikker over voor bak 2: " + str(d))
    b = d

    print("_______________________")


def KnikkersTrekken():
    #_________________Wiske_________________:
    global a
    global b

    print("Wiske trekt:")

    if (a>b):       #Bak 1 heeft meer knikkers dan Bak 2
        print(f"Wiske trekt {a-b+1} knikkers uit bak 1.")
        a = b-1     #Bak 1 = 1 knikker minder dan Bak 2
        print(f"In bak 1 zitten nog {a} knikkers.")
        print("Bak 2 blijft hetzelfde.")
    
    else:
        print(f"Wiske trekt {b-a+1} knikkers uit bak 2.")
        b = a-1     #Bak 2 = 1 knikker minder dan Bak 1
        print(f"In bak 2 zitten nog {b} knikkers.")
        print("Bak 1 blijft hetzelfe.")

    print("_______________________")

    #_________________Suske_________________:
    print("Suske trekt:")

    options = [1,2,3]
    choosenOption = random.choice(options)
    if choosenOption == 1:
        print("suskeOPTION1")
        suskeOPTION1 = random.randint(1, a) #kiest aantal knikkers om uit bak 1 te nemen
        a = a - suskeOPTION1
        #print wat over blijft

    elif choosenOption == 2:
        print("suskeOPTION2")
        suskeOPTION2 = random.randint(1, b) #kiest aantal knikkers om uit bak 2 te nemen
        b = b - suskeOPTION2
        #print wat over blijft

    elif choosenOption == 3:
        print("suskeOPTION3")
        hoogsteWaarde = max(a,b) #Welke bak heeft de hoogste waarde?
        i = random.randint(1, hoogsteWaarde) #kiest evenveel aantal knikkers om uit bak 1 en 2 te nemen
        a-i
        b-i
        #print wat over blijft

    

VerdeelKnikkers()
KnikkersTrekken()