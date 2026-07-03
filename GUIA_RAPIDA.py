#!/usr/bin/env python3
"""
GUÍA RÁPIDA DE EJECUCIÓN

Este archivo explica cómo ejecutar el proyecto de Algoritmos de Búsqueda Desinformada.
"""

import os
import sys

def mostrar_guia():
    """Mostrar la guía de uso."""
    
    guia = """
╔════════════════════════════════════════════════════════════════════╗
║          ALGORITMOS DE BÚSQUEDA DESINFORMADA - GUÍA RÁPIDA        ║
╚════════════════════════════════════════════════════════════════════╝

📋 ARCHIVOS PRINCIPALES:
   • main.py          → Programa interactivo principal (RECOMENDADO)
   • test_all.py      → Pruebas automáticas de todos los casos
   • verify.py        → Verificación rápida de funcionamiento

🚀 CÓMO EJECUTAR:

   OPCIÓN 1 - Programa Interactivo (Recomendado):
   ────────────────────────────────────────────────
   python main.py
   
   Esto abrirá un menú donde puedes seleccionar:
   • Grafo Simple (pruebas rápidas)
   • Ruta de Ciudades
   • Mapa con Costos
   • Laberinto
   
   El programa mostrará los resultados de todos los algoritmos
   en el problema seleccionado.

   OPCIÓN 2 - Ejecutar Todas las Pruebas:
   ──────────────────────────────────────
   python test_all.py
   
   Ejecuta automáticamente todos los 4 casos de prueba
   con todos los 5 algoritmos.

   OPCIÓN 3 - Verificación Rápida:
   ───────────────────────────────
   python verify.py
   
   Verifica que todos los módulos están correctamente instalados
   y ejecuta una prueba simple de BFS.

📁 ESTRUCTURA DEL PROYECTO:
   ────────────────────────
   search-algorithms/
   ├── algorithms/           (MÓDULO: Implementación de algoritmos)
   │   ├── bfs.py           → BFS (Búsqueda en Amplitud)
   │   ├── dfs.py           → DFS (Búsqueda en Profundidad)
   │   ├── dls.py           → DLS (Búsqueda en Profundidad Limitada)
   │   ├── ids.py           → IDS (Profundización Iterativa)
   │   └── ucs.py           → UCS (Costo Uniforme)
   │
   ├── problems/             (MÓDULO: Casos de prueba)
   │   ├── graph.py         → Clase Grafo
   │   └── test_cases.py    → Casos de prueba predefinidos
   │
   ├── main.py              → Programa Principal
   ├── test_all.py          → Script de pruebas
   ├── verify.py            → Verificación rápida
   ├── visualization.py     → Módulo de visualización
   ├── README.md            → Documentación completa
   └── requirements.txt     → Dependencias

🎯 CASOS DE PRUEBA:

   1️⃣  GRAFO SIMPLE (6 nodos)
       Estructura simple para verificación rápida
       Tiempo: < 1ms

   2️⃣  RUTA DE CIUDADES (5 ciudades)
       Buscador de rutas entre ciudades españolas con distancias
       Tiempo: < 1ms

   3️⃣  MAPA CON COSTOS (9 nodos)
       Árbol con pesos variables para comparar optimalidad
       Tiempo: < 1ms

   4️⃣  LABERINTO (3×4)
       Búsqueda de ruta en maze representado como matriz
       Tiempo: < 1ms

📊 LOS 5 ALGORITMOS:

   BFS (Búsqueda en Amplitud)
   ├─ Estructura: Cola (FIFO)
   ├─ Óptima: ✓ Sí (en términos de pasos)
   ├─ Completa: ✓ Sí
   └─ Memoria: Alto

   DFS (Búsqueda en Profundidad)
   ├─ Estructura: Pila (LIFO)
   ├─ Óptima: ✗ No
   ├─ Completa: ✓ Sí (en grafos finitos)
   └─ Memoria: Bajo

   DLS (Profundidad Limitada)
   ├─ Estructura: Pila con límite
   ├─ Óptima: ✗ No
   ├─ Completa: Parcial (si solución dentro del límite)
   └─ Memoria: Bajo

   IDS (Profundización Iterativa)
   ├─ Estructura: DLS repetido
   ├─ Óptima: ✓ Sí
   ├─ Completa: ✓ Sí
   └─ Memoria: Medio

   UCS (Costo Uniforme)
   ├─ Estructura: Cola de prioridad
   ├─ Óptima: ✓ Sí (en costo total)
   ├─ Completa: ✓ Sí
   └─ Memoria: Alto

✨ CARACTERÍSTICAS DE SALIDA:

   Para cada búsqueda se muestra:
   • Camino encontrado (o si no existe)
   • Lista de nodos explorados
   • Número total de nodos explorados
   • Costo total (para UCS)
   • Tiempo de ejecución en milisegundos
   • Tabla comparativa de todos los algoritmos

💡 EJEMPLOS DE USO:

   Ejemplo 1: Encontrar ruta más corta
   ───────────────────────────────────
   python main.py
   [Seleccionar opción 2: Ruta de Ciudades]
   → Verás cómo BFS e IDS encuentran la mejor ruta
   → UCS también considerará distancias

   Ejemplo 2: Resolver laberinto rápidamente
   ──────────────────────────────────────────
   python test_all.py
   [Llegará automáticamente al caso del laberinto]
   → Todos los algoritmos resolverán el laberinto
   → Verás cuál es más eficiente

   Ejemplo 3: Prueba rápida
   ───────────────────────
   python verify.py
   → Verifica que todo está instalado correctamente
   → Muestra un ejemplo simple de BFS en acción

🔧 REQUISITOS:

   • Python 3.8 o superior
   • NO necesita dependencias externas
   • Solo usa librerías estándar: collections, heapq, typing, time

💻 COMANDO RÁPIDO:

   cd search-algorithms && python main.py

📚 DOCUMENTACIÓN:

   Cada módulo tiene documentación detallada:
   • README.md → Documentación completa
   • Cada archivo .py tiene docstrings en español
   • Cada función está documentada con Args, Returns, Raises

❓ PREGUNTAS FRECUENTES:

   P: ¿Por qué IDS explora más nodos que BFS?
   R: IDS repite búsquedas con límites incrementales, por lo que
      explora nodos múltiples veces en las iteraciones anteriores.

   P: ¿Cuál algoritmo debo usar?
   R: 
   • Para grafos pequeños: BFS
   • Para mucha profundidad: DFS
   • Para optimalidad con costos: UCS
   • Para espacios muy grandes: IDS

   P: ¿Puedo agregar mis propios grafos?
   R: Sí, modifica test_cases.py o crea una función nueva
      que retorne (Grafo, inicio, objetivo)

✅ VERIFICACIÓN DE INSTALACIÓN:

   python verify.py
   
   Esto te dirá si todo está funcionando correctamente.

═════════════════════════════════════════════════════════════════════
¡Listo para explorar algoritmos de búsqueda! 🎯
═════════════════════════════════════════════════════════════════════
"""
    
    print(guia)


if __name__ == "__main__":
    mostrar_guia()
