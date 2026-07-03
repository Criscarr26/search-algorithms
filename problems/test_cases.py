"""Casos de prueba para los algoritmos de búsqueda."""

from .graph import Grafo


def obtener_grafo_ciudades() -> tuple:
    """
    Crea un grafo de ciudades conectadas.
    
    Estructura:
        Madrid ---200--- Barcelona
          |                |
         310             180
          |                |
        Valencia ---260--- Tarragona
          |
         250
          |
        Alicante
    
    Returns:
        (Grafo, inicio, objetivo)
    """
    grafo = Grafo("Ruta de Ciudades")
    
    # Agregar ciudades (nodos)
    ciudades = ["Madrid", "Barcelona", "Valencia", "Alicante", "Tarragona"]
    for ciudad in ciudades:
        grafo.adyacencia[ciudad] = []
    
    # Agregar conexiones (aristas) con distancias
    conexiones = [
        ("Madrid", "Barcelona", 630),
        ("Madrid", "Valencia", 310),
        ("Barcelona", "Tarragona", 180),
        ("Valencia", "Tarragona", 260),
        ("Valencia", "Alicante", 250),
    ]
    
    for origen, destino, distancia in conexiones:
        grafo.agregar_arista(origen, destino, distancia, dirigido=False)
    
    return grafo, "Madrid", "Alicante"


def obtener_mapa_costos() -> tuple:
    """
    Crea un grafo con nodos y costos variables.
    
    Estructura tipo árbol con pesos:
            A
           / \
          B   C
         /|   |\
        D E   F G
    
    Returns:
        (Grafo, inicio, objetivo)
    """
    grafo = Grafo("Mapa con Costos")
    
    # Definir aristas con costos
    aristas = [
        ("A", "B", 2),
        ("A", "C", 3),
        ("B", "D", 4),
        ("B", "E", 1),
        ("C", "F", 2),
        ("C", "G", 5),
        ("D", "H", 1),
        ("E", "H", 2),
        ("F", "I", 3),
    ]
    
    for origen, destino, costo in aristas:
        grafo.agregar_arista(origen, destino, costo, dirigido=False)
    
    return grafo, "A", "H"


def obtener_laberinto() -> tuple:
    """
    Crea un grafo que representa un laberinto en matriz 3x4.
    
    Celda válida (1), muro (0):
    
        1 1 0 1
        0 1 1 1
        1 1 0 1
    
    El grafo conecta celdas válidas adyacentes (4-direcciones).
    
    Returns:
        (Grafo, inicio, objetivo)
    """
    grafo = Grafo("Laberinto 3x4")
    
    # Matriz del laberinto: 1 = camino, 0 = muro
    laberinto = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 1]
    ]
    
    # Crear nodos como coordenadas (fila, columna)
    nodos_validos = []
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 1:
                nodo = f"({i},{j})"
                nodos_validos.append((i, j, nodo))
                grafo.adyacencia[nodo] = []
    
    # Conectar nodos adyacentes
    # Direcciones: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i, j, nodo_actual in nodos_validos:
        for di, dj in direcciones:
            ni, nj = i + di, j + dj
            
            # Verificar si la celda vecina es válida
            if (0 <= ni < len(laberinto) and 
                0 <= nj < len(laberinto[0]) and 
                laberinto[ni][nj] == 1):
                
                nodo_vecino = f"({ni},{nj})"
                if nodo_vecino not in grafo.adyacencia[nodo_actual]:
                    grafo.agregar_arista(nodo_actual, nodo_vecino, costo=1, dirigido=False)
    
    return grafo, "(0,0)", "(2,3)"


def obtener_grafo_simple() -> tuple:
    """
    Crea un grafo simple para pruebas rápidas.
    
    Estructura:
        A --- B --- D
        |     |     |
        C --- E --- F
    
    Returns:
        (Grafo, inicio, objetivo)
    """
    grafo = Grafo("Grafo Simple")
    
    aristas = [
        ("A", "B", 1),
        ("A", "C", 2),
        ("B", "D", 1),
        ("B", "E", 3),
        ("C", "E", 1),
        ("D", "F", 2),
        ("E", "F", 1),
    ]
    
    for origen, destino, costo in aristas:
        grafo.agregar_arista(origen, destino, costo, dirigido=False)
    
    return grafo, "A", "F"
