#!/usr/bin/env python3
"""
Programa Principal: Comparación de Algoritmos de Búsqueda Desinformada

Este programa demuestra la implementación y comparación de cinco algoritmos
de búsqueda desinformada en diferentes tipos de problemas.

Estructura:
- Algoritmos: BFS, DFS, DLS, IDS, UCS
- Problemas: Ciudades, Mapa de costos, Laberinto
"""

from algorithms import (
    busqueda_amplitud,
    busqueda_profundidad,
    busqueda_profundidad_limitada,
    busqueda_profundizacion_iterativa,
    busqueda_costo_uniforme
)
from problems import obtener_grafo_ciudades, obtener_mapa_costos, obtener_laberinto, obtener_grafo_simple
from visualization import ejecutar_comparacion_algoritmos, VisualizadorBusqueda


def main():
    """Función principal del programa."""
    
    visualizador = VisualizadorBusqueda()
    
    # Diccionario con todas las funciones de algoritmos
    algoritmos = {
        'bfs': busqueda_amplitud,
        'dfs': busqueda_profundidad,
        'dls': busqueda_profundidad_limitada,
        'ids': busqueda_profundizacion_iterativa,
        'ucs': busqueda_costo_uniforme
    }
    
    # Mostrar menú
    while True:
        visualizador.mostrar_titulo("ALGORITMOS DE BÚSQUEDA DESINFORMADA")
        
        print("\nSelecciona un problema de prueba:\n")
        print("1. Grafo Simple (Para pruebas rápidas)")
        print("2. Ruta de Ciudades (Búsqueda de ruta con distancias)")
        print("3. Mapa con Costos (Árbol con pesos variables)")
        print("4. Laberinto (Matriz de maze)")
        print("5. Salir\n")
        
        opcion = input("Ingresa tu opción (1-5): ").strip()
        
        if opcion == '1':
            visualizador.mostrar_titulo("GRAFO SIMPLE")
            grafo, inicio, objetivo = obtener_grafo_simple()
            print(grafo)
            print(f"📍 Buscando ruta desde: {inicio} → {objetivo}\n")
            ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, algoritmos)
            
        elif opcion == '2':
            visualizador.mostrar_titulo("RUTA DE CIUDADES")
            grafo, inicio, objetivo = obtener_grafo_ciudades()
            print(grafo)
            print(f"📍 Buscando ruta desde: {inicio} → {objetivo}\n")
            ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, algoritmos)
            
        elif opcion == '3':
            visualizador.mostrar_titulo("MAPA CON COSTOS")
            grafo, inicio, objetivo = obtener_mapa_costos()
            print(grafo)
            print(f"📍 Buscando camino desde: {inicio} → {objetivo}\n")
            ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, algoritmos)
            
        elif opcion == '4':
            visualizador.mostrar_titulo("LABERINTO")
            grafo, inicio, objetivo = obtener_laberinto()
            print(grafo)
            print(f"📍 Buscando salida desde: {inicio} → {objetivo}\n")
            ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, algoritmos)
            
        elif opcion == '5':
            visualizador.mostrar_titulo("¡Hasta luego!")
            break
        
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.\n")
            continue
        
        # Preguntar si continuar
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
