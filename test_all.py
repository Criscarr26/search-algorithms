#!/usr/bin/env python3
"""
Script de pruebas no interactivo para verificar todos los algoritmos.

Ejecuta los cinco algoritmos sobre los cuatro casos de prueba y comprueba que
los caminos devueltos son válidos. Termina con código de salida 1 si alguna
comprobación falla, para que pueda usarse en integración continua.

    python test_all.py            # ejecuta y verifica
    python test_all.py --pausar   # se detiene entre casos (modo demo)
"""

import sys

from algorithms import (
    busqueda_amplitud,
    busqueda_profundidad,
    busqueda_profundidad_limitada,
    busqueda_profundizacion_iterativa,
    busqueda_costo_uniforme
)
from problems import obtener_grafo_ciudades, obtener_mapa_costos, obtener_laberinto, obtener_grafo_simple
from visualization import ejecutar_comparacion_algoritmos, VisualizadorBusqueda

ALGORITMOS = {
    'bfs': busqueda_amplitud,
    'dfs': busqueda_profundidad,
    'dls': busqueda_profundidad_limitada,
    'ids': busqueda_profundizacion_iterativa,
    'ucs': busqueda_costo_uniforme
}


def pausar(activada: bool) -> None:
    """Espera al usuario sólo si se pidió pausar y hay alguien escuchando.

    Sin la comprobación de `isatty`, ejecutar el script desde otro script o
    desde CI abortaba con EOFError, que es justo lo contrario de lo que
    promete el nombre del archivo.
    """
    if activada and sys.stdin is not None and sys.stdin.isatty():
        input("\nPresiona Enter para continuar...\n")


def camino_es_valido(camino, grafo, inicio, objetivo) -> str:
    """Devuelve una cadena vacía si el camino es correcto, o el motivo del fallo."""
    if camino is None:
        return "no encontró camino"
    if not camino:
        return "devolvió un camino vacío"
    if camino[0] != inicio:
        return f"empieza en {camino[0]} y no en {inicio}"
    if camino[-1] != objetivo:
        return f"termina en {camino[-1]} y no en {objetivo}"
    for origen, destino in zip(camino, camino[1:]):
        if destino not in grafo.obtener_vecinos(origen):
            return f"salta de {origen} a {destino}, que no son vecinos"
    if len(set(camino)) != len(camino):
        return "repite nodos: no es un camino simple"
    return ""


def costo_del_camino(camino, grafo) -> float:
    return sum(
        grafo.obtener_costo(origen, destino)
        for origen, destino in zip(camino, camino[1:])
    )


def probar_caso(nombre_caso, grafo, inicio, objetivo, pausa: bool) -> list:
    """Ejecuta el caso y devuelve la lista de fallos encontrados."""
    visualizador = VisualizadorBusqueda()
    visualizador.mostrar_titulo(nombre_caso)
    print(f"Objetivo: {inicio} -> {objetivo}\n")

    resultados = ejecutar_comparacion_algoritmos(grafo, inicio, objetivo, ALGORITMOS)
    fallos = []

    for nombre, datos in resultados.items():
        motivo = camino_es_valido(datos['camino'], grafo, inicio, objetivo)
        if motivo:
            fallos.append(f"{nombre_caso} / {nombre}: {motivo}")

    validos = {
        nombre: datos['camino']
        for nombre, datos in resultados.items()
        if not camino_es_valido(datos['camino'], grafo, inicio, objetivo)
    }

    # BFS e IDS son óptimos en número de aristas: deben coincidir en longitud.
    if 'BFS' in validos and 'IDS' in validos:
        if len(validos['BFS']) != len(validos['IDS']):
            fallos.append(
                f"{nombre_caso}: BFS ({len(validos['BFS'])} nodos) e IDS "
                f"({len(validos['IDS'])} nodos) deberían dar caminos igual de cortos"
            )

    # UCS es óptimo en costo: ningún otro camino puede salir más barato.
    if 'UCS' in validos:
        costo_ucs = costo_del_camino(validos['UCS'], grafo)
        for nombre, camino in validos.items():
            if nombre != 'UCS' and costo_del_camino(camino, grafo) < costo_ucs - 1e-9:
                fallos.append(
                    f"{nombre_caso}: {nombre} encontró un camino más barato "
                    f"({costo_del_camino(camino, grafo)}) que UCS ({costo_ucs})"
                )

    pausar(pausa)
    return fallos


def main() -> int:
    pausa = "--pausar" in sys.argv

    print("=" * 80)
    print("PRUEBA COMPLETA DE ALGORITMOS DE BÚSQUEDA DESINFORMADA")
    print("=" * 80)
    pausar(pausa)

    casos = [
        ("1. GRAFO SIMPLE", obtener_grafo_simple),
        ("2. RUTA DE CIUDADES", obtener_grafo_ciudades),
        ("3. MAPA CON COSTOS", obtener_mapa_costos),
        ("4. LABERINTO", obtener_laberinto),
    ]

    fallos = []
    for nombre, obtener in casos:
        grafo, inicio, objetivo = obtener()
        fallos.extend(probar_caso(nombre, grafo, inicio, objetivo, pausa))

    print("\n" + "=" * 80)
    if fallos:
        print(f"FALLARON {len(fallos)} COMPROBACIONES")
        for fallo in fallos:
            print(f"  - {fallo}")
        print("=" * 80 + "\n")
        return 1

    print(f"PRUEBAS COMPLETADAS: {len(casos)} casos x {len(ALGORITMOS)} algoritmos, "
          "todos los caminos verificados")
    print("=" * 80 + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
