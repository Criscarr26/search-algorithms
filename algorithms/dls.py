"""
Búsqueda en Profundidad Limitada (DLS - Depth-Limited Search)

Variante de DFS que limita la profundidad máxima de búsqueda.
Útil cuando se conoce una cota superior de la solución.

Características:
- Completa: SOLO si la solución existe dentro del límite de profundidad
- NO óptima: puede encontrar soluciones no óptimas
- Complejidad espacial: O(b*l) donde l es el límite de profundidad
"""

from typing import List, Tuple, Dict, Set, Optional


def busqueda_profundidad_limitada(grafo: Dict, inicio: str, objetivo: str, 
                                   limite: int) -> Tuple[Optional[List[str]], Set[str], int]:
    """
    Implementa Búsqueda en Profundidad Limitada (DLS).
    
    Args:
        grafo: Diccionario con estructura {nodo: [nodos_vecinos]}
        inicio: Nodo de partida
        objetivo: Nodo objetivo a alcanzar
        limite: Profundidad máxima permitida
    
    Returns:
        Tuple con:
        - Lista de nodos que forman el camino (None si no existe)
        - Conjunto de nodos explorados
        - Número de nodos explorados
    """
    
    nodos_explorados = set()
    
    def dls_recursivo(nodo: str, profundidad: int, padres: Dict) -> Optional[List[str]]:
        """
        Función recursiva auxiliar para DLS.
        
        Args:
            nodo: Nodo actual
            profundidad: Profundidad actual
            padres: Diccionario para rastrear padres
        
        Returns:
            Camino si se encuentra objetivo, None si no
        """
        nodos_explorados.add(nodo)
        
        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            n = objetivo
            while n is not None:
                camino.append(n)
                n = padres[n]
            camino.reverse()
            return camino
        
        # Si alcanzamos el límite de profundidad, retornar
        if profundidad == 0:
            return None
        
        # Explorar vecinos
        if nodo in grafo:
            for vecino in grafo[nodo]:
                if vecino not in padres:  # Para evitar ciclos
                    padres[vecino] = nodo
                    resultado = dls_recursivo(vecino, profundidad - 1, padres)
                    if resultado is not None:
                        return resultado
                    # Limpiar para permitir exploración desde otros caminos
                    del padres[vecino]
        
        return None
    
    # Inicializar búsqueda
    padres = {inicio: None}
    camino = dls_recursivo(inicio, limite, padres)
    
    return camino, nodos_explorados, len(nodos_explorados)
