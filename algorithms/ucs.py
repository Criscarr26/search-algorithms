"""
Búsqueda de Costo Uniforme (UCS - Uniform Cost Search)

Es una generalización de BFS que explora nodos en orden de su costo acumulado.
Utiliza una cola de prioridad para siempre expandir el nodo de menor costo.

Características:
- Completa: encontrará solución si existe
- Óptima: encuentra la solución de menor costo
- Complejidad espacial y temporal: depende de la función de costo
"""

import heapq
from typing import List, Tuple, Dict, Set, Optional


def busqueda_costo_uniforme(grafo: Dict, costos: Dict, inicio: str, 
                             objetivo: str) -> Tuple[Optional[List[str]], Set[str], int, Optional[float]]:
    """
    Implementa Búsqueda de Costo Uniforme (UCS).
    
    Args:
        grafo: Diccionario con estructura {nodo: [nodos_vecinos]}
        costos: Diccionario con estructura {(nodo_a, nodo_b): costo}
        inicio: Nodo de partida
        objetivo: Nodo objetivo a alcanzar
    
    Returns:
        Tuple con:
        - Lista de nodos que forman el camino (None si no existe)
        - Conjunto de nodos explorados
        - Número de nodos explorados
        - Costo total del camino (None si no existe)
    """
    
    # Inicializar estructuras
    # Heap: (costo_acumulado, nodo)
    heap = [(0, inicio)]
    costo_g = {inicio: 0}  # Costo desde el inicio
    padres = {inicio: None}
    nodos_explorados = set()
    visitados = set()
    
    while heap:
        costo_actual, nodo_actual = heapq.heappop(heap)
        
        # Si ya fue visitado, saltar
        if nodo_actual in visitados:
            continue
        
        visitados.add(nodo_actual)
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
            
            costo_final = costo_g[objetivo]
            return camino, nodos_explorados, len(nodos_explorados), costo_final
        
        # Explorar vecinos
        if nodo_actual in grafo:
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    # Calcular costo del arista
                    arista = (nodo_actual, vecino)
                    costo_arista = costos.get(arista, 1)  # Por defecto costo 1
                    
                    nuevo_costo = costo_actual + costo_arista
                    
                    # Si encontramos un camino mejor al vecino
                    if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                        costo_g[vecino] = nuevo_costo
                        padres[vecino] = nodo_actual
                        heapq.heappush(heap, (nuevo_costo, vecino))
    
    # No se encontró camino
    return None, nodos_explorados, len(nodos_explorados), None
