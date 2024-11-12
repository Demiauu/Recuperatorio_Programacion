from recuperatorio import *

def menu():
    print (f"\n****Elecciones centro de estudiante!!!!! ****")
    while True:
        print("\nMenu de Opciones:\n")
        print("1. Cargar Votos")
        print("2. Mostrar Votos")
        print("3. Ordenar Votos Turno Mañana")
        print("4. Encontrar la lista con menos del 5% de los votos")
        print("5. Encontrar turno al que más alumnos fueron a votar")
        print("6. Verificar si hay segunda vuelta")
        print("7. Realizar el ballotage")
        print("8. Salir")

        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            cargar_datos()
        elif opcion == 2:
            mostrar_matriz(matriz_votos)
        elif opcion == 3:
            ordenar_votos_turno_mañana(matriz_votos)
        elif opcion == 4:
            encontrar_lista_5porciento(matriz_votos)
        elif opcion == 5:
            encontrar_turno_mas_votos(matriz_votos)
        elif opcion == 6:
            verificar_ballotage(matriz_votos)
        elif opcion == 7:
            realizar_ballotage(matriz_votos,verificar_ballotage(matriz_votos))
        elif opcion == 8:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

menu()