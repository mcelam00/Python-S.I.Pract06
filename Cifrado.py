import math #para logaritmos y funciones techo y suelo

    

 
def irTroceandoElMensaje(mensajeEnClaro, numeroDeBloque, k): 

    bloqueKLetras = ""

    for i in  range(numeroDeBloque, numeroDeBloque+k):
        bloqueKLetras = bloqueKLetras + mensajeEnClaro[i]

    return bloqueKLetras

def codifNcaEstandar(modulo):

    cne = []

    #el modulo es la longitud del alfabeto. La codificación numérica estándar empezaría en el 0 e iría hasta el N-1 incluido
    for i in range(modulo):
        cne.append(i)

    return cne

def calcularCodifNcaCadaBloque(bloqueKLetras, alfyCodNca):
    listaCN = []
    
    for simbolo in bloqueKLetras:
        for letra, numero in alfyCodNca.items():
            if simbolo == letra:
                listaCN.append(numero)

    return listaCN

def calcularEntero(codNcaBloque, N, k):
    m = 0
    contador = 1

    for Mi in codNcaBloque:
        m = m + (Mi*(N**(k-contador))) #contador++ de manera que resto 1 mas cada vez
        contador = contador+1
    return m
    
def RSASimple(m, e, n):
    return pow(m, e, n) #calcula la potencia modular m^e modulo n

def calcularExpresionBaseN(c, kMasUno, N):

    expresion = []
    dividendo = c
    divisor = N

    if(dividendo < divisor):
        expresion.append(dividendo)


    while (dividendo >= divisor):
     
        cociente = dividendo // divisor
        if(cociente < divisor):
            resto = dividendo % divisor
            expresion.append(resto)
            expresion.append(cociente)

            break

        resto = dividendo % divisor
        dividendo = cociente
        expresion.append(resto)
        
    #si no llega a longitud k el bloque, completamos por la izda con 0 hasta 
    #llegar a k+1 (faltarían (k+1)-long actual 0 por completar)
    if(len(expresion) != kMasUno):
        for i in range(kMasUno-len(expresion)):
            expresion.append(0)

   
    #doy vuelta a la lista porque fuí añadiendo al final
    return list(reversed(expresion))

def calcularSimbolosDeCadaBloque(bloqueLongKMasUno):
    C = ""
    
    for num in bloqueLongKMasUno:
        for letra, numero in alfyCodNca.items():
            if num == numero:
                C = C + letra


    return C









#Introducir la clave publica del receptor (n,e)
n = 9641865053
p = 98179
q = 98207
e = 70241161

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ÁÉÍÓÚ"
N = len(alfabeto) #numero de simbolos del alfabeto
mensajeEnClaro = "ENIGMA"


#Preparo la codificacion numerica asociada al alfabeto
codifNcaEstandar = codifNcaEstandar(N)

#Junto el alfabeto y la codificacion numerica en una misma estructura diccionario
alfyCodNca = {alfabeto[i]: codifNcaEstandar[i] for i in range(len(alfabeto))}




#1. Calculamos la longitud del bloque a cifrar K
k = math.floor(math.log(n,N)) #Log base N de n
kMasUno = k+1

#El mensaje cifrado debe tener una longitud divisible por k, sino habría que rellenar
if((len(mensajeEnClaro)%k) == 0): 
    print("Long. msjCifrado correcta") 
else: 
    print("rellenar msj no long correcta")
    exit()


numeroDeBloque = 0
mensajeCifrado = ""

#Dividimos el mensaje en bloques de k letras

for i in range(int(len(mensajeEnClaro)/k)): #el cociente será el num de secs completas

    bloqueKLetras = irTroceandoElMensaje(mensajeEnClaro, numeroDeBloque, k)
    numeroDeBloque = numeroDeBloque + k
    codNcaBloque = calcularCodifNcaCadaBloque(bloqueKLetras, alfyCodNca)
    m = calcularEntero(codNcaBloque, N, k)
    c = RSASimple(m, e, n)
    bloqueLongKMasUno = calcularExpresionBaseN(c, kMasUno, N)
    bloqueCifrado = calcularSimbolosDeCadaBloque(bloqueLongKMasUno)
    mensajeCifrado = mensajeCifrado + bloqueCifrado
    



print("\n======================================================================")
print("CLAVE CIFRADA K*:")
print(mensajeCifrado + "|FinMSJ")
print("======================================================================")

print("\nFIN DEL PROGRAMA")

