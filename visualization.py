"""Módulo de visualización de resultados de búsqueda."""

from typing import List, Dict, Tuple, Optional, Set
from datetime import datetime


class VisualizadorBusqueda:
    """Clase para visualizar resultados de búsqueda de forma estructurada."""
    
    def __init__(self):
        """Inicializar el visualizador."""
        self.colores = {
            'rojo': '\033[91m',
            'verde': '\033[92m',
            'amarillo': '\033[93m',
            'azul': '\033[94m',
            'magenta': '\033[95m',
            'cian': '\033[96m',
            'blanco': '\033[97m',
            'reset': '\033[0m',
            'negrita': '\033[1m',
        }
    
    def _colorear(self, texto: str, color: str = 'blanco', negrita: bool = False) -> str:
        """Aplicar color a texto."""
        color_code = self.colores.get(color, '')
        negrita_code = self.colores['negrita'] if negrita else ''
        reset_code = self.colores['reset']
        return f"{negrita_code}{color_code}{texto}{reset_code}"
    
    def mostrar_titulo(self, titulo: str):
        """Mostrar un título destacado."""
        barra = "=" * (len(titulo) + 4)
        print(f"\n{self._colorear(barra, 'azul', negrita=True)}")
        print(self._colorear(f"  {titulo}  ", 'azul', negrita=True))
        print(f"{self._colorear(barra, 'azul', negrita=True)}\n")
    
    def mostrar_resultado_busqueda(self, nombre_algoritmo: str, camino: Optional[List[str]], 
                                   nodos_explorados: Set[str], num_explorados: int, 
                                   costo: Optional[float] = None, tiempo: Optional[float] = None):
        """
        Mostrar resultado de una búsqueda.
        
        Args:
            nombre_algoritmo: Nombre del algoritmo usado
            camino: Lista de nodos del camino encontrado
            nodos_explorados: Conjunto de nodos explorados
            num_explorados: Número de nodos explorados
            costo: Costo total (si aplica)
            tiempo: Tiempo de ejecución en segundos
        """
        print(self._colorear(f"\n▶ {nombre_algoritmo}:", 'magenta', negrita=True))
        
        if camino:
            print(self._colorear("✓ Camino encontrado:", 'verde'))
            camino_str = " → ".join(camino)
            print(f"  {self._colorear(camino_str, 'verde')}")
            print(f"  Longitud del camino: {self._colorear(str(len(camino)), 'verde')}")
            
            if costo is not None:
                print(f"  Costo total: {self._colorear(f'{costo:.2f}', 'verde')}")
        else:
            print(self._colorear("✗ No se encontró camino", 'rojo'))
        
        print(f"  Nodos explorados: {self._colorear(str(num_explorados), 'amarillo')}")
        
        if tiempo is not None:
            print(f"  Tiempo de ejecución: {self._colorear(f'{tiempo*1000:.4f}ms', 'cian')}")
        
        # Mostrar lista de nodos explorados
        nodos_lista = sorted(list(nodos_explorados))
        print(f"  Nodos explorados: {', '.join(nodos_lista)}")
    
    def mostrar_comparativa(self, resultados: Dict[str, Dict]):
        """
        Mostrar comparativa de todos los algoritmos.
        
        Args:
            resultados: Diccionario con resultados de cada algoritmo
        """
        print(self._colorear("\n" + "="*80, 'amarillo', negrita=True))
        print(self._colorear("COMPARATIVA DE ALGORITMOS", 'amarillo', negrita=True))
        print(self._colorear("="*80 + "\n", 'amarillo', negrita=True))
        
        # Encabezados
        ancho_algoritmo = 25
        ancho_camino = 12
        ancho_explorados = 12
        ancho_costo = 12
        ancho_tiempo = 12
        
        encabezado = (
            f"{'Algoritmo':<{ancho_algoritmo}} | "
            f"{'Camino encontrado':<{ancho_camino}} | "
            f"{'Nodos explorados':<{ancho_explorados}} | "
            f"{'Costo':<{ancho_costo}} | "
            f"{'Tiempo (ms)':<{ancho_tiempo}}"
        )
        
        print(self._colorear(encabezado, 'azul', negrita=True))
        print(self._colorear("-" * len(encabezado), 'azul'))
        
        # Filas
        for algoritmo, datos in resultados.items():
            camino_encontrado = "Sí" if datos['camino'] else "No"
            nodos = datos['nodos_explorados']
            costo_str = f"{datos['costo']:.2f}" if datos['costo'] is not None else "N/A"
            tiempo_str = f"{datos['tiempo']*1000:.4f}" if datos['tiempo'] is not None else "N/A"
            
            # Colorear según resultado
            color_resultado = 'verde' if datos['camino'] else 'rojo'
            
            linea = (
                f"{algoritmo:<{ancho_algoritmo}} | "
                f"{self._colorear(camino_encontrado, color_resultado):<{ancho_camino}} | "
                f"{str(nodos):<{ancho_explorados}} | "
                f"{costo_str:<{ancho_costo}} | "
                f"{tiempo_str:<{ancho_tiempo}}"
            )
            print(linea)
        
        print()
    
    def mostrar_grafo_info(self, nombre: str, nodos: List[str], cantidad_aristas: int):
        """Mostrar información del grafo."""
        print(self._colorear(f"\n📊 Información del Grafo: {nombre}", 'cian', negrita=True))
        print(f"   Nodos: {', '.join(nodos)}")
        print(f"   Total de nodos: {len(nodos)}")
        print(f"   Total de aristas: {cantidad_aristas}\n")


def ejecutar_comparacion_algoritmos(grafo, inicio: str, objetivo: str, 
                                    algoritmos_importados: Dict):
    """
    Ejecutar todos los algoritmos y mostrar comparativa.
    
    Args:
        grafo: Objeto Grafo
        inicio: Nodo de inicio
        objetivo: Nodo objetivo
        algoritmos_importados: Diccionario con funciones de algoritmos
    
    Returns:
        Diccionario con resultados
    """
    import time
    
    visualizador = VisualizadorBusqueda()
    resultados = {}
    
    # Información del grafo
    nodos = grafo.obtener_nodos()
    aristas = len(grafo.costos) // 2  # Las aristas no dirigidas contan doble
    visualizador.mostrar_grafo_info(grafo.nombre, nodos, aristas)
    
    # BFS
    inicio_tiempo = time.time()
    camino_bfs, explorados_bfs, num_exp_bfs = algoritmos_importados['bfs'](
        grafo.adyacencia, inicio, objetivo
    )
    tiempo_bfs = time.time() - inicio_tiempo
    
    visualizador.mostrar_resultado_busqueda(
        "BFS (Búsqueda en Amplitud)", camino_bfs, explorados_bfs, num_exp_bfs, 
        tiempo=tiempo_bfs
    )
    resultados['BFS'] = {
        'camino': camino_bfs,
        'nodos_explorados': num_exp_bfs,
        'costo': None,
        'tiempo': tiempo_bfs
    }
    
    # DFS
    inicio_tiempo = time.time()
    camino_dfs, explorados_dfs, num_exp_dfs = algoritmos_importados['dfs'](
        grafo.adyacencia, inicio, objetivo
    )
    tiempo_dfs = time.time() - inicio_tiempo
    
    visualizador.mostrar_resultado_busqueda(
        "DFS (Búsqueda en Profundidad)", camino_dfs, explorados_dfs, num_exp_dfs,
        tiempo=tiempo_dfs
    )
    resultados['DFS'] = {
        'camino': camino_dfs,
        'nodos_explorados': num_exp_dfs,
        'costo': None,
        'tiempo': tiempo_dfs
    }
    
    # DLS
    limite = len(nodos) - 1
    inicio_tiempo = time.time()
    camino_dls, explorados_dls, num_exp_dls = algoritmos_importados['dls'](
        grafo.adyacencia, inicio, objetivo, limite
    )
    tiempo_dls = time.time() - inicio_tiempo
    
    visualizador.mostrar_resultado_busqueda(
        f"DLS (Búsqueda en Profundidad Limitada, límite={limite})", 
        camino_dls, explorados_dls, num_exp_dls,
        tiempo=tiempo_dls
    )
    resultados['DLS'] = {
        'camino': camino_dls,
        'nodos_explorados': num_exp_dls,
        'costo': None,
        'tiempo': tiempo_dls
    }
    
    # IDS
    inicio_tiempo = time.time()
    camino_ids, explorados_ids, num_exp_ids = algoritmos_importados['ids'](
        grafo.adyacencia, inicio, objetivo
    )
    tiempo_ids = time.time() - inicio_tiempo
    
    visualizador.mostrar_resultado_busqueda(
        "IDS (Profundización Iterativa)", camino_ids, explorados_ids, num_exp_ids,
        tiempo=tiempo_ids
    )
    resultados['IDS'] = {
        'camino': camino_ids,
        'nodos_explorados': num_exp_ids,
        'costo': None,
        'tiempo': tiempo_ids
    }
    
    # UCS
    inicio_tiempo = time.time()
    camino_ucs, explorados_ucs, num_exp_ucs, costo_ucs = algoritmos_importados['ucs'](
        grafo.adyacencia, grafo.costos, inicio, objetivo
    )
    tiempo_ucs = time.time() - inicio_tiempo
    
    visualizador.mostrar_resultado_busqueda(
        "UCS (Costo Uniforme)", camino_ucs, explorados_ucs, num_exp_ucs,
        costo=costo_ucs, tiempo=tiempo_ucs
    )
    resultados['UCS'] = {
        'camino': camino_ucs,
        'nodos_explorados': num_exp_ucs,
        'costo': costo_ucs,
        'tiempo': tiempo_ucs
    }
    
    # Mostrar comparativa
    visualizador.mostrar_comparativa(resultados)
    
    return resultados
