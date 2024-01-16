import numpy as np #librería para operaciones numéricas
import matplotlib.pyplot as plt #librería para visualización de datos

#Función para calcular la distancia entre dos ciudades y calcular la distancia entre ellas
def calcular_distancia(ciudad1, ciudad2):
    return np.linalg.norm(np.array(ciudad1) - np.array(ciudad2))

#Función para encontrar la ciudad más cercana a la actual en la lista de ciudades
def encontrar_ciudad_mas_cercana(ciudad_actual, ciudades_restantes):
   #Calcula las distancias entre la ciudad actual y todas las ciudades restantes
    distancias = [calcular_distancia(ciudad_actual, ciudad) for ciudad in ciudades_restantes]
    #Encuentra el índice de la ciudad más cercana
    ciudad_mas_cercana_idx = np.argmin(distancias)
    #Devuelve la ciudad más cercana y su indice en la lista
    return ciudades_restantes[ciudad_mas_cercana_idx], ciudad_mas_cercana_idx

#Función para calcular la longitud total de una ruta
def calcular_longitud_ruta(ciudades, recorrido):
    longitud = 0
    #Suma las distancias entre ciudades consecutivas en el recorrido
    for i in range(len(recorrido) - 1):
        longitud += calcular_distancia(ciudades[recorrido[i]], ciudades[recorrido[i + 1]])
    return longitud

#Función que implementa la heurística del vecino más cercano para resolver el TSP
def tsp_heuristico(ciudades):
    num_ciudades = len(ciudades)
    mejor_ruta = None #Variable para almacenar la mejor ruta encontrada
    mejor_longitud = float('inf') #Inicializa la mejor longitud con infinito positivo

    for i in range(num_ciudades):
        recorrido = [i] #Inicia el recorrido desde la ciudad i
        ciudades_restantes = list(range(num_ciudades))
        ciudades_restantes.remove(i) #Remueve la ciudad de partida de la lista de las ciudades restantes

        while ciudades_restantes:
            ciudad_actual = ciudades[recorrido[-1]] #La ciudad actual es la última agregada al recorrido
            #Encuentra la ciudad más cercana y su índice en las ciudades restantes
            ciudad_mas_cercana, idx = encontrar_ciudad_mas_cercana(ciudad_actual, [ciudades[j] for j in ciudades_restantes])
            #Agrega la ciudad más cercana al recorrido y elimina las ciudades restantes
            recorrido.append(ciudades_restantes.pop(idx))

        recorrido.append(recorrido[0])  # Cierra el ciclo agregando la ciudad de inicio al final del recorrido
        longitud_actual = calcular_longitud_ruta(ciudades, recorrido) #Calcula la longitud del recorrido actual

#Compara la longitud actual con la mejor longitud encontrada hasta ahora
        if longitud_actual < mejor_longitud:
            mejor_longitud = longitud_actual
            mejor_ruta = recorrido #Actualiza la mejor ruta

    return mejor_ruta, mejor_longitud #Devuelve la mejor ruta y su longitud

#Función para graficar las ciudades y la mejor ruta encontrada
def graficar_tsp(ciudades, mejor_ruta, mejor_longitud):
    x = [ciudad[0] for ciudad in ciudades]
    y = [ciudad[1] for ciudad in ciudades]

    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, c='red', marker='o', label='Ciudades') #Grafica las ciudades

    ruta_x = [x[i] for i in mejor_ruta]
    ruta_y = [y[i] for i in mejor_ruta]
    plt.plot(ruta_x, ruta_y, linestyle='--', linewidth=1.5, label='Ruta más corta') #Gráfica la mejor ruta

    #Añade título y leyenda al gráfico
    plt.title(f'Problema del Viajante de Comercio (TSP) - Ruta más Corta\nDistancia Recorrida: {mejor_longitud:.2f}')
    plt.legend()
    plt.show()

# Coordenadas de 10 ciudades
ciudades = [(0, 7), (1, 4), (9, 4), (3, 3), (4, 7), (5, 2), (6, 5), (7, 9), (8, 6), (9, 8)]

# Aplica la heurística del vecino más cercano para obtener la ruta más corta y la distancia recorrida
mejor_ruta, mejor_longitud = tsp_heuristico(ciudades)

# Graficar la ruta más corta y muestra la distancia recorrida
graficar_tsp(ciudades, mejor_ruta, mejor_longitud)
