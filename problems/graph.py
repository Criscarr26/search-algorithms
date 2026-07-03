"""Clase Grafo para representar gratos de manera estructurada."""

from typing import Dict, List, Tuple, Optional


class Grafo:
    """
    Clase para representar un grafo no dirigido con costos opcionales.
    """
    
    def __init__(self, nombre: str = "Grafo"):
        """
        Inicializar el grafo.
        
        Args:
            nombre: Nombre descriptivo del grafo
        """
        self.nombre = nombre
        self.adyacencia: Dict[str, List[str]] = {}
        self.costos: Dict[Tuple[str, str], float] = {}
    
    def agregar_arista(self, origen: str, destino: str, costo: float = 1, 
                       dirigido: bool = False):
        """
        Agregar una arista entre dos nodos.
        
        Args:
            origen: Nodo de origen
            destino: Nodo de destino
            costo: Peso/costo de la arista
            dirigido: Si False, agrega arista bidireccional
        """
        # Agregar nodos si no existen
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []
        
        # Agregar arista
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
        self.costos[(origen, destino)] = costo
        
        # Agregar arista inversa si no es dirigida
        if not dirigido:
            if origen not in self.adyacencia[destino]:
                self.adyacencia[destino].append(origen)
            self.costos[(destino, origen)] = costo
    
    def obtener_vecinos(self, nodo: str) -> List[str]:
        """Obtener lista de vecinos de un nodo."""
        return self.adyacencia.get(nodo, [])
    
    def obtener_costo(self, origen: str, destino: str) -> float:
        """Obtener costo de una arista."""
        return self.costos.get((origen, destino), 1)
    
    def contiene_nodo(self, nodo: str) -> bool:
        """Verificar si un nodo existe en el grafo."""
        return nodo in self.adyacencia
    
    def obtener_nodos(self) -> List[str]:
        """Obtener lista de todos los nodos."""
        return list(self.adyacencia.keys())
    
    def __str__(self) -> str:
        """Representación en string del grafo."""
        lineas = [f"\n{'='*50}"]
        lineas.append(f"Grafo: {self.nombre}")
        lineas.append(f"Nodos: {', '.join(self.obtener_nodos())}")
        lineas.append(f"Cantidad de nodos: {len(self.adyacencia)}")
        lineas.append(f"{'='*50}\n")
        
        for nodo in sorted(self.adyacencia.keys()):
            vecinos = []
            for vecino in self.adyacencia[nodo]:
                costo = self.obtener_costo(nodo, vecino)
                vecinos.append(f"{vecino}({costo})")
            lineas.append(f"{nodo:15} -> {', '.join(vecinos)}")
        
        return '\n'.join(lineas)
