import random

a = 0 #Bak 1
b = 0 #Bak 2

c = random.randint(15,35) #Willekeurig aantal knikkers tussen 15 en 35

def VerdeelKnikkers():
    print("Aantal knikkers om te verdelen: " + str(c))

    a = random.randint(1,c)
    print("Aantal knikkers in bak 1: " + str(a))

    d = str(c-a)
    print("Aantal knikker over voor bak 2: " + d)
    b = d

# def KnikkersTrekken():


VerdeelKnikkers()