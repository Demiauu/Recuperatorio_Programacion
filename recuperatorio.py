"""
1. Cargar Votos: Se reali|za una carga secuencial de todos los votos de cada una de las cinco listas (Debe ser una matriz)
NOTA: Validar todos los ingresos de datos, evitar votos negativos o nro de lista que no sean números de tres cifras.

2. Mostrar Votos: Muestra en un lindo formato los siguientes datos: Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche

3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de votos que tuvieron en el turno mañana.

4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos los votos

5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos fueron a votar.

6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.

7. Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
a votar en cada turno en la segunda vuelta y de manera random se calculan los votos del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
final de cada lista y se muestra al ganador de las elecciones.
NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar que no hubo segunda vuelta.
"""
import random

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int)-> list:
    matriz = []
    
    for _ in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]
    return matriz

matriz_votos = inicializar_matriz(2,4)

def mostrar_matriz(matriz:list)-> None:
    """
    Esta funcion te muestra la matriz con un formato lindo con los datos ingresados
    """
    for i in range(len(matriz)):
        print(f"\nLista: {matriz[i][0]}\n------------------------\nVotos turno Mañana: {matriz[i][1]}\n------------------------\nVotos turno Tarde: {matriz[i][2]}\n------------------------\nVotos turno Noche: {matriz[i][3]}\n")

def cargar_datos()-> None:
    """
    Esta funcion se encarga de pidir datos para despues cargarlos en la matriz inicializada anteriormente
    """
    for i in range(len(matriz_votos)):
        for j in range(len(matriz_votos[i])):
            if j == 0:
                numero = int(input("Ingrese el numero de lista: "))
                while numero > 999  or numero < 100:
                    numero = int(input("Porfavor ingrese solo numeros de 3 digitos: "))
            else:
                while True:
                    if j == 1:
                        numero = int(input("Cantidad de votos para turno mañana: "))
                    elif j == 2:
                        numero = int(input("Cantidad de votos para turno tarde: "))
                    else:
                        numero = int(input("Cantidad de votos para turno noche: "))
                    if numero > 0:
                        break
                    else:
                        print("No se permiten votos negativos.")
            matriz_votos[i][j] = numero

def ordenar_votos_turno_mañana(matriz:list)-> None:
    """
    Esta funcion se encarga de comparar todas las matrices y ordenarlas de forma que se muestren de mayor a menor por orden los votos del turno mañana
    """
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][1] < matriz[j][1]:
                for k in range(len(matriz[0])):
                    aux = matriz[i][k]
                    matriz[i][k] = matriz[j][k]
                    matriz[j][k] = aux

def encontrar_lista_5porciento(matriz:list)-> None:
    """
    Esta funcion se encarga de buscar la lista que tenga menos del 5% de los votos entre todas las matrices
    """
    total = 0
    suma_votos_lista = 0
    bandera = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j != 0:
                total += matriz[i][j]
    cinco_porciento = (total * 5) / 100
    cinco_porciento = round(cinco_porciento,2)

    for i in range(len(matriz)):
        suma_votos_lista = 0
        for j in range(len(matriz[i])):
            if j != 0:
                suma_votos_lista += matriz[i][j]
        if suma_votos_lista < cinco_porciento:
            if bandera == False:
                print("\nLas listas con menos del 5% de los votos son las siguientes: \n")
                print(f"Lista: {matriz[i][0]}\n")
                bandera = True
            else:
                print(f"Lista: {matriz[i][0]}\n")
    if bandera == False:
        print("\nNo se encontró una lista con menos del 5% de los votos\n")

def encontrar_turno_mas_votos(matriz:list)-> None:
    """
    Esta funcion se encarga de buscar la entre todas las matrices el turno con mas votos de lista
    """
    turno_mañana = 0
    turno_tarde = 0
    turno_noche = 0
    for i in range(len(matriz)):
        turno_mañana += matriz[i][1]
        turno_tarde += matriz[i][2]
        turno_noche += matriz[i][3]
    if turno_mañana > turno_tarde and turno_mañana > turno_noche:
        mensaje = "turno mañana"
    elif turno_tarde > turno_noche:
        mensaje = "turno tarde"
    else:
        mensaje = "turno noche"
    print(f"\nel turno en el que más alumnos fueron a votar es: {mensaje}\n")

def verificar_ballotage(matriz:list)-> bool:
    """
    Esta funcion verifica si hay posible ballotage devuelve si hay ballotage(True) o si no hay(False)
    """
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j != 0:
                total += matriz[i][j]
    cincuenta_por_ciento = (total * 50) / 100
    cincuenta_por_ciento = round(cincuenta_por_ciento,2)

    for i in range(len(matriz)):
        suma_votos_lista = 0
        for j in range(len(matriz[i])):
            if j != 0:
                suma_votos_lista += matriz[i][j]
        if suma_votos_lista > cincuenta_por_ciento:
            print(f"\nNo hay ballotage\n")
            return False
        else: 
            print(f"\nHay ballotage\n")
            return True

def realizar_ballotage(matriz,hay_ballotage):
    """
    Una vez verificado si hay ballotage esta funcion se encarga de realizar el ballotage
    """
    if hay_ballotage == True:
        lista1 = 0
        lista2 = 0
        for j in range(len(matriz[0])):
            if j != 0:
                lista1 += matriz[0][j]
                lista2 += matriz[1][j]

        listas = [lista1,lista2]
        
        for i in range(len(listas)-1):
            for j in range(i +1, len(listas)):
                if listas[i] < listas[j]:
                    aux = listas[i]
                    listas[i] = listas[j]
                    listas[j] = aux

        candidato1 = listas[0]
        candidato2 = listas[1]

        votos_turno_mañana = int(input("Ingrese la cantidad de alumnos que votaron en el turno mañana en ballotage: "))
        votos_turno_tarde = int(input("Ingrese la cantidad de alumnos que votaron en el turno tarde en ballotage: "))
        votos_turno_noche = int(input("Ingrese la cantidad de alumnos que votaron en el turno noche en ballotage: "))

        votos_candidato1_mañana = random.randint(0, votos_turno_mañana)
        votos_candidato2_mañana = votos_turno_mañana - votos_candidato1_mañana

        votos_candidato1_tarde = random.randint(0, votos_turno_tarde)
        votos_candidato2_tarde = votos_turno_tarde - votos_candidato1_tarde

        votos_candidato1_noche = random.randint(0, votos_turno_noche)
        votos_candidato2_noche = votos_turno_noche - votos_candidato1_noche

        candidato1 = votos_candidato1_mañana + votos_candidato1_tarde + votos_candidato1_noche
        candidato2 = votos_candidato2_mañana + votos_candidato2_tarde + votos_candidato2_noche

        total_votos = candidato1 + candidato2

        porcentaje_candidato1 = (candidato1 / total_votos) * 100
        porcentaje_candidato2 = (candidato2 / total_votos) * 100

        print(f"\nResultados del ballotage:")
        print(f"Candidato 1: {candidato1} votos ({porcentaje_candidato1:.2f}%)")
        print(f"Candidato 2: {candidato2} votos ({porcentaje_candidato2:.2f}%)")

        if porcentaje_candidato1 > porcentaje_candidato2:
            mensaje = print("El ganador de las elecciones es el Candidato 1.")
        else:
            mensaje = print("El ganador de las elecciones es el Candidato 2.")
    elif hay_ballotage == False:
        mensaje = print("No se puede realizar segunda vuelta si no empataron los candidatos")
    else:
        mensaje = print("no se puede realizar la segunda vuelta sin antes verificarlo.")
    return mensaje