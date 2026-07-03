#!/usr/bin/env python3
"""
Script de pruebas no interactivo para verificar todos los algoritmos.
Ejecuta todos los algoritmos en todos los casos de prueba y muestra resultados.
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


def probar_caso(nombre_caso, grafo, inicio, objetivo):
    """Probar un caso específico con todos los algoritmos."""
    
    visualizador = VisualizadorBusqueda()
    
    algoritmos = {
        'bfs': busqueda_amplitud,
        'dfs': busqueda_profundidad,
        'dls': busqueda_profundidad_limitada,
        'ids': busqueda_profundizacion_iterativa,
        'ucs': busqueda_costo_uniforme
    }
    
    visualizador.mostrar_titulo(nombre_caso)
    print(grafo)
    print(f"📍 Objetivo: {inicio} → {objetivo}\n")
    
    ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, algoritmos)
    
    input("\nPresiona Enter para continuar...\n")


def main():
    """Ejecutar todas las pruebas."""
    
    print("\n" * 2)
    print("=" * 80)
    print("PRUEBA COMPLETA DE ALGORITMOS DE BÚSQUEDA DESINFORMADA")
    print("=" * 80)
    print("\nEste script ejecutará todos los algoritmos en 4 casos de prueba diferentes.")
    print("Presiona Enter para comenzar...\n")
    
    input()
    
    # Caso 1: Grafo Simple
    grafo, inicio, objetivo = obtener_grafo_simple()
    probar_caso("1. GRAFO SIMPLE", grafo, inicio, objetivo)
    
    # Caso 2: Ciudades
    grafo, inicio, objetivo = obtener_grafo_ciudades()
    probar_caso("2. RUTA DE CIUDADES", grafo, inicio, objetivo)
    
    # Caso 3: Mapa de Costos
    grafo, inicio, objetivo = obtener_mapa_costos()
    probar_caso("3. MAPA CON COSTOS", grafo, inicio, objetivo)
    
    # Caso 4: Laberinto
    grafo, inicio, objetivo = obtener_laberinto()
    probar_caso("4. LABERINTO", grafo, inicio, objetivo)
    
    print("\n" + "=" * 80)
    print("✓ PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
