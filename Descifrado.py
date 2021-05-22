import math #para logaritmos y funciones techo y suelo

    



def calcularClavePrivada(e,p,q): #Zmod(fi(n)) y fi(n) = (p-1)*(q-1)
    fiDen = ((p-1)*(q-1))
    if(math.gcd(e, fiDen) == 1):
        print("e tiene inverso modulo fi(n)")
    else:
        print("e no tiene inverso modulo fi(n)")
    
    eInv = pow(e, -1, fiDen) #AEE 

    return eInv
  
def irTroceandoElMensaje(mensajeCifrado, numeroDeBloque, kMasUno): 

    bloqueKMasUnaLetras = ""

    for i in  range(numeroDeBloque, numeroDeBloque+kMasUno):
        bloqueKMasUnaLetras = bloqueKMasUnaLetras + mensajeCifrado[i]

    return bloqueKMasUnaLetras

def codifNcaEstandar(modulo):

    cne = []

    #el modulo es la longitud del alfabeto. La codificación numérica estándar empezaría en el 0 e iría hasta el N-1 incluido
    for i in range(modulo):
        cne.append(i)

    return cne

def calcularCodifNcaCadaBloque(bloqueKMasUnaLetras, alfyCodNca):
    listaCN = []
    
    for simbolo in bloqueKMasUnaLetras:
        for letra, numero in alfyCodNca.items():
            if simbolo == letra:
                listaCN.append(numero)

    return listaCN

def calcularEntero(codNcaBloque, N, kMasUno):
    c = 0
    contador = 1

    for Mi in codNcaBloque:
        c = c + (Mi*(N**(kMasUno-contador))) #contador++ de manera que resto 1 mas cada vez
        contador = contador+1
    return c
    
def RSASimple(c, d, n):
    return pow(c, d, n) #calcula la potencia modular c^d modulo n

def calcularExpresionBaseN(m, k, N):

    expresion = []
    dividendo = m
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
    #llegar a k (faltarían k-long actual 0 por completar)
    if(len(expresion) != k):
        for i in range(k-len(expresion)):
            expresion.append(0)

   
    #doy vuelta a la lista porque fuí añadiendo al final
    return list(reversed(expresion))

def calcularSimbolosDeCadaBloque(bloqueLongK):
    M = ""
    
    for num in bloqueLongK:
        for letra, numero in alfyCodNca.items():
            if num == numero:
                M = M + letra


    return M









#Introducir la clave publica del receptor (n,e)
n = 21962054407
p = 148193
q = 148199
e = 80263681

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYX ÁÉÍÓÚ"
N = len(alfabeto) #numero de simbolos del alfabeto
mensajeCifrado = "CÉQUANL"


#Preparo la codificacion numerica asociada al alfabeto
codifNcaEstandar = codifNcaEstandar(N)

#Junto el alfabeto y la codificacion numerica en una misma estructura diccionario
alfyCodNca = {alfabeto[i]: codifNcaEstandar[i] for i in range(len(alfabeto))}




#1. Calculamos la longitud del bloque a cifrar K
k = math.floor(math.log(n,N)) #Log base N de n
kMasUno = k+1

#El mensaje cifrado debe tener una longitud divisible por k+1, sino habría que rellenar
if((len(mensajeCifrado)%kMasUno) == 0): 
    print("Long. msjCifrado correcta") 
else: 
    print("rellenar msj no long correcta")
    exit()

#calculamos la clave privada del receptor (d =  e^-1 mod(fi(n)))
d = calcularClavePrivada(e,p,q)

numeroDeBloque = 0
mensajeDescifrado = ""

#Dividimos el mensaje en bloques de k+1 letras

for i in range(int(len(mensajeCifrado)/kMasUno)): #el cociente será el num de secs completas

    bloqueKMasUnaLetras = irTroceandoElMensaje(mensajeCifrado, numeroDeBloque, kMasUno)
    numeroDeBloque = numeroDeBloque + kMasUno
    codNcaBloque = calcularCodifNcaCadaBloque(bloqueKMasUnaLetras, alfyCodNca)
    c = calcularEntero(codNcaBloque, N, kMasUno)
    m = RSASimple(c, d, n)
    bloqueLongK = calcularExpresionBaseN(m, k, N)
    bloqueDescifrado = calcularSimbolosDeCadaBloque(bloqueLongK)
    mensajeDescifrado = mensajeDescifrado + bloqueDescifrado
    




mensajeDescifrado = mensajeDescifrado.replace("  ", "\n")

print("\n======================================================================")
print("MENSAJE DESCIFRADO:")
print(mensajeDescifrado)
print("======================================================================")

print("\nFIN DEL PROGRAMA")

