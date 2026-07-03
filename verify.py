#!/usr/bin/env python3
"""Script simple para verificar que todos los módulos se importan correctamente."""

try:
    from algorithms import (
        busqueda_amplitud,
        busqueda_profundidad,
        busqueda_profundidad_limitada,
        busqueda_profundizacion_iterativa,
        busqueda_costo_uniforme
    )
    print("✓ Algoritmos importados correctamente")
    
    from problems import obtener_grafo_ciudades, obtener_mapa_costos, obtener_laberinto, obtener_grafo_simple
    print("✓ Casos de prueba importados correctamente")
    
    from visualization import VisualizadorBusqueda
    print("✓ Visualizador importado correctamente")
    
    # Prueba rápida de un algoritmo
    grafo, inicio, objetivo = obtener_grafo_simple()
    camino, explorados, num_explorados = busqueda_amplitud(grafo.adyacencia, inicio, objetivo)
    
    print("\n" + "="*50)
    print("PRUEBA RÁPIDA: BFS en Grafo Simple")
    print("="*50)
    print(f"Inicio: {inicio}")
    print(f"Objetivo: {objetivo}")
    print(f"Camino encontrado: {camino}")
    print(f"Nodos explorados: {sorted(list(explorados))}")
    print(f"Total nodos explorados: {num_explorados}")
    print("\n✓ ¡Todo funciona correctamente!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
