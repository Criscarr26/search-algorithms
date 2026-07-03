"""
Búsqueda en Profundidad (DFS - Depth-First Search)

Explora el grafo bajando lo más profundo posible antes de retroceder.
Utiliza una pila (stack) para llevar el control de los nodos.

Características:
- Completa: encontrará solución si existe (en grafos finitos)
- NO óptima: puede encontrar soluciones no óptimas
- Complejidad espacial: O(b*d) donde b es el factor de ramificación
"""

from typing import List, Tuple, Dict, Set, Optional


def busqueda_profundidad(grafo: Dict, inicio: str, objetivo: str) -> Tuple[Optional[List[str]], Set[str], int]:
    """
    Implementa Búsqueda en Profundidad (DFS) de forma iterativa con pila explícita.
    
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
    pila = [inicio]  # Pila para implementar LIFO
    visitados = {inicio}
    padres = {inicio: None}
    nodos_explorados = set()
    
    while pila:
        nodo_actual = pila.pop()
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
        
        # Explorar vecinos (en orden inverso para mantener orden consistente)
        if nodo_actual in grafo:
            for vecino in reversed(grafo[nodo_actual]):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = nodo_actual
                    pila.append(vecino)
    
    # No se encontró camino
    return None, nodos_explorados, len(nodos_explorados)


def busqueda_profundidad_recursiva(grafo: Dict, nodo: str, objetivo: str, 
                                    visitados: Set[str], padres: Dict,
                                    nodos_explorados: Set[str]) -> bool:
    """
    Versión recursiva de DFS (uso alternativo).
    
    Args:
        grafo: Diccionario con estructura del grafo
        nodo: Nodo actual siendo explorado
        objetivo: Nodo objetivo
        visitados: Conjunto de nodos ya visitados
        padres: Diccionario para rastrear el camino
        nodos_explorados: Conjunto de nodos explorados
    
    Returns:
        True si encontró el objetivo, False en caso contrario
    """
    visitados.add(nodo)
    nodos_explorados.add(nodo)
    
    if nodo == objetivo:
        return True
    
    if nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                padres[vecino] = nodo
                if busqueda_profundidad_recursiva(grafo, vecino, objetivo, 
                                                  visitados, padres, nodos_explorados):
                    return True
    
    return False
