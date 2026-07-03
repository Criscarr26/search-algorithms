"""
Búsqueda Primero en Amplitud (BFS - Breadth-First Search)

Explora el grafo nivel por nivel, visitando todos los nodos a distancia k
antes de visitar nodos a distancia k+1.

Características:
- Completa: encontrará solución si existe
- Óptima: encuentra la solución con menos aristas (si todos los costos son iguales)
- Complejidad espacial: O(b^d) donde b es el factor de ramificación y d es la profundidad
"""

from collections import deque
from typing import List, Tuple, Dict, Set, Optional


def busqueda_amplitud(grafo: Dict, inicio: str, objetivo: str) -> Tuple[Optional[List[str]], Set[str], int]:
    """
    Implementa Búsqueda en Amplitud (BFS).
    
    Args:
        grafo: Diccionario con estructura {nodo: [nodos_vecinos]}
        inicio: Nodo de partida
        objetivo: Nodo objetivo a alcanzar
    
    Returns:
        Tuple con:
        - Lista de nodos que forman el camino (None si no existe)
        - Conjunto de nodos explorados
        - Número de nodos explorados
    """
    
    # Inicializar estructuras
    cola = deque([inicio])  # Cola para implementar FIFO
    visitados = {inicio}
    padres = {inicio: None}
    nodos_explorados = set()
    
    while cola:
        nodo_actual = cola.popleft()
        nodos_explorados.add(nodo_actual)
        
        # Verificar si encontramos el objetivo
        if nodo_actual == objetivo:
            # Reconstruir camino
            camino = []
            nodo = objetivo
            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]
            camino.reverse()
            return camino, nodos_explorados, len(nodos_explorados)
        
        # Explorar vecinos
        if nodo_actual in grafo:
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = nodo_actual
                    cola.append(vecino)
    
    # No se encontró camino
    return None, nodos_explorados, len(nodos_explorados)
