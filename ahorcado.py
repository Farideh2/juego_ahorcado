import random

letra = " "
letras_bien = 0
oport = 6
letras_usa = []
palabra_act = []
letras_sr = []
palabras = ["ventana", "libreria", "sonido", "universidad", "elefante"]
letras_correctas = ""

rand = random.randint(0,len(palabras)-1)
pal_esco = palabras[rand]
largo = len(pal_esco)
word = []

print("Bienvenido al juego de el ahorcado")
print("El largo de la palabra es:", largo)

for contador in range(largo):
    word.append("_")

def imprimir(letra, palabra):
    for cont in range(len(palabra)):
        if letra in palabra[cont]:
            word.insert(cont,letra)
            del word[cont+1]
    print("la palabra actual es",word)
        
def hombre(intentos):
    if intentos == 6:
        print("+---+")
        print("|   |")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("=========)")
    
    elif intentos == 5:
        print("+---+")
        print("|   |")
        print ("O   |")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("=========)")
    
    elif intentos == 4:
        print("+---+")
        print("|   |")
        print ("O   |")
        print ("|   |")
        print ("    |")
        print ("    |")
        print ("=========)")
    
    elif intentos == 3:
        print(" +---+")
        print(" |   |")
        print (" O   |")
        print ("/|   |")
        print ("     |")
        print ("     |")
        print (" =========)")

    elif intentos == 2:    
        print(" +---+")
        print(" |   |")
        print (" O   |")
        print ("/|\  |")
        print ("     |")
        print ("     |")
        print (" =========)")
        
    elif intentos == 1:    
        print(" +---+")
        print(" |   |")
        print (" O   |")
        print ("/|\  |")
        print ("/    |")
        print ("     |")
        print (" =========)")

    elif intentos == 0:
        print(" +---+")
        print(" |   |")
        print (" O   |")
        print ("/|\  |")
        print ("/ \  |")
        print ("     |")
        print (" =========)")

for cont in range(0, largo):
    if pal_esco[cont] not in letras_sr:
        letras_sr.append(pal_esco[cont])

while True:
    #escoger()
    letra = input()
    if letra in letras_usa:
        print("ya usaste esta letra")

    elif letra in letras_sr:
        print("le atinaste")
        letras_usa.append(letra)
        letras_bien += 1
        hombre(oport)
        imprimir(letra,pal_esco)
        if letras_bien == len(letras_sr):
            print("ganaste")
            break

    else:
        print("esta letra no es")
        letras_usa.append(letra)
        oport -= 1
        print("te quedan:",oport,"intentos")
        imprimir(letra,pal_esco)
        hombre(oport)
        if oport== 0:
            print("perdiste")
            break