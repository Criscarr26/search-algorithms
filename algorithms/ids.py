"""
Búsqueda de Profundización Iterativa (IDS - Iterative Deepening Search)

Combina las ventajas de BFS y DFS: realiza búsquedas con límites de profundidad 
incrementales (1, 2, 3, ...) hasta encontrar la solución.

Características:
- Completa: encontrará solución si existe
- Óptima: encuentra la solución óptima (en términos de número de aristas)
- Complejidad espacial: O(b*d) - mejor que BFS
"""

from typing import List, Tuple, Dict, Set, Optional


def busqueda_profundizacion_iterativa(grafo: Dict, inicio: str, objetivo: str, 
                                       max_profundidad: int = None) -> Tuple[Optional[List[str]], Set[str], int]:
    """
    Implementa Búsqueda de Profundización Iterativa (IDS).
    
    Args:
        grafo: Diccionario con estructura {nodo: [nodos_vecinos]}
        inicio: Nodo de partida
        objetivo: Nodo objetivo a alcanzar
        max_profundidad: Profundidad máxima a explorar (None para sin límite)
    
    Returns:
        Tuple con:
        - Lista de nodos que forman el camino (None si no existe)
        - Conjunto de nodos explorados (en TODAS las iteraciones)
        - Número de nodos explorados (en TODAS las iteraciones)
    """
    
    todos_nodos_explorados = set()
    
    def dls_recursivo(nodo: str, profundidad: int, visitados: Set[str], 
                      padres: Dict) -> Optional[List[str]]:
        """
        Búsqueda en profundidad limitada interna.
        """
        todos_nodos_explorados.add(nodo)
        visitados.add(nodo)
        
        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            n = objetivo
            while n is not None:
                camino.append(n)
                n = padres[n]
            camino.reverse()
            return camino
        
        if profundidad == 0:
            return None
        
        if nodo in grafo:
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    padres[vecino] = nodo
                    resultado = dls_recursivo(vecino, profundidad - 1, visitados, padres)
                    if resultado is not None:
                        return resultado
        
        return None
    
    # Determinar profundidad máxima
    if max_profundidad is None:
        max_profundidad = len(grafo)
    
    # Iteración: aumentar límite de profundidad gradualmente
    for limite_actual in range(max_profundidad + 1):
        visitados = set()
        padres = {inicio: None}
        resultado = dls_recursivo(inicio, limite_actual, visitados, padres)
        
        if resultado is not None:
            return resultado, todos_nodos_explorados, len(todos_nodos_explorados)
    
    # No se encontró camino
    return None, todos_nodos_explorados, len(todos_nodos_explorados)
