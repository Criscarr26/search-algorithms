# Algoritmos de Búsqueda Desinformada

Implementación completa en Python de 5 algoritmos de búsqueda desinformada con casos de prueba, visualización y comparación.

## 📋 Algoritmos Implementados

### 1. **BFS (Búsqueda Primero en Amplitud)**
- **Archivo**: `algorithms/bfs.py`
- **Estructura**: Cola (FIFO)
- **Características**:
  - ✓ Completa (encuentra solución si existe)
  - ✓ Óptima (en términos de número de aristas)
  - Uso: Encontrar el camino más corto en términos de pasos

### 2. **DFS (Búsqueda en Profundidad)**
- **Archivo**: `algorithms/dfs.py`
- **Estructura**: Pila (LIFO)
- **Características**:
  - ✓ Completa (en grafos finitos)
  - ✗ NO óptima
  - Uso: Exploración exhaustiva, detección de ciclos

### 3. **DLS (Búsqueda en Profundidad Limitada)**
- **Archivo**: `algorithms/dls.py`
- **Estructura**: Pila con límite de profundidad
- **Características**:
  - ✓ Completa si la solución está dentro del límite
  - ✗ NO óptima
  - Uso: Limitar búsqueda en grafos infinitos

### 4. **IDS (Profundización Iterativa)**
- **Archivo**: `algorithms/ids.py`
- **Estructura**: DLS repetido con límites incrementales
- **Características**:
  - ✓ Completa
  - ✓ Óptima (combina ventajas de BFS y DFS)
  - Uso: Espacios muy grandes donde BFS usa mucha memoria

### 5. **UCS (Búsqueda de Costo Uniforme)**
- **Archivo**: `algorithms/ucs.py`
- **Estructura**: Cola de prioridad
- **Características**:
  - ✓ Completa
  - ✓ Óptima en costo total
  - Uso: Grafos ponderados, encontrar camino de menor costo

## 📁 Estructura del Proyecto

```
search-algorithms/
├── algorithms/           # Módulo con los algoritmos
│   ├── __init__.py
│   ├── bfs.py           # Búsqueda en Amplitud
│   ├── dfs.py           # Búsqueda en Profundidad
│   ├── dls.py           # Búsqueda en Profundidad Limitada
│   ├── ids.py           # Profundización Iterativa
│   └── ucs.py           # Búsqueda de Costo Uniforme
│
├── problems/            # Módulo con casos de prueba
│   ├── __init__.py
│   ├── graph.py        # Clase Grafo
│   └── test_cases.py   # Casos de prueba predefinidos
│
├── main.py             # Programa principal
├── visualization.py    # Módulo de visualización
├── requirements.txt    # Dependencias
└── README.md          # Este archivo
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8+
- No hay dependencias externas (usa librerías estándar)

### Instalación
```bash
# Clonar o descargar el proyecto
cd search-algorithms

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias (aunque solo sean librerías estándar)
pip install -r requirements.txt
```

### Ejecución
```bash
# Ejecutar el programa principal
python main.py

# Seguir las instrucciones en el menú interactivo
```

## 🧪 Casos de Prueba

### 1. Grafo Simple
Red simple de 6 nodos para pruebas rápidas:
```
    A --- B --- D
    |     |     |
    C --- E --- F
```

**Uso**: Verificación rápida de funcionamiento

### 2. Ruta de Ciudades
Grafo que representa ciudades españolas conectadas con distancias reales:
```
Madrid ←→ Barcelona
  ↓         ↓
Valencia ←→ Tarragona
  ↓
Alicante
```

**Uso**: Problema de búsqueda de ruta con costos

### 3. Mapa con Costos
Árbol con pesos variables en las aristas:
```
        A
       / \
      B   C
     /|   |\
    D E   F G
```

**Uso**: Comparación de algoritmos óptimos vs no-óptimos

### 4. Laberinto
Matriz 3×4 donde 1 = camino válido, 0 = muro:
```
1 1 0 1
0 1 1 1
1 1 0 1
```

**Uso**: Problema de búsqueda en espacios de estado discretos

## 📊 Características Principales

### Para Cada Búsqueda se Retorna:
1. **Camino encontrado**: Lista de nodos desde inicio a objetivo
2. **Nodos explorados**: Conjunto de todos los nodos visitados
3. **Costo total**: (Solo UCS) Suma de pesos del camino
4. **Tiempo de ejecución**: Medido en milisegundos

### Visualización:
- Información del grafo (nodos, aristas)
- Resultado detallado por algoritmo
- Tabla comparativa con todos los algoritmos
- Colores ANSI para mejor legibilidad

## 📈 Ejemplo de Salida

```
==================================================
  RUTA DE CIUDADES  
==================================================

📊 Información del Grafo: Ruta de Ciudades
   Nodos: Madrid, Barcelona, Valencia, Alicante, Tarragona
   Total de nodos: 5
   Total de aristas: 5

▶ BFS (Búsqueda en Amplitud):
✓ Camino encontrado:
  Madrid → Valencia → Alicante
  Longitud del camino: 3
  Nodos explorados: 3
  Nodos explorados: Madrid, Valencia, Alicante
  
[... resultados de otros algoritmos ...]

================================================================================
COMPARATIVA DE ALGORITMOS
================================================================================

Algoritmo               | Camino encontrado | Nodos explorados | Costo    | Tiempo (ms)
────────────────────────────────────────────────────────────────────────────────────
BFS                    | Sí                | 3                | N/A      | 0.0234
DFS                    | Sí                | 3                | N/A      | 0.0156
DLS                    | Sí                | 3                | N/A      | 0.0189
IDS                    | Sí                | 5                | N/A      | 0.0312
UCS                    | Sí                | 3                | 560.00   | 0.0401
```

## 🔄 Comparación Entre Algoritmos

| Algoritmo | Completa | Óptima | Memoria | Tiempo | Mejor para |
|-----------|----------|--------|---------|--------|-----------|
| BFS       | ✓        | ✓      | Alto    | Medio  | Grafos pequeños |
| DFS       | ✓        | ✗      | Bajo    | Rápido | Búsqueda exhaustiva |
| DLS       | Parcial  | ✗      | Bajo    | Rápido | Limitar profundidad |
| IDS       | ✓        | ✓      | Medio   | Medio  | Espacios grandes |
| UCS       | ✓        | ✓      | Alto    | Lento  | Grafos ponderados |

## 💡 Notas Importantes

### BFS vs DFS
- **BFS**: Garantiza camino más corto (número de pasos)
- **DFS**: Más eficiente en memoria, pero no garantiza optimalidad

### IDS vs BFS
- **IDS**: Usa menos memoria que BFS
- **BFS**: Más rápido que IDS
- Ambos encuentran la solución óptima

### UCS vs BFS
- **BFS**: Óptimo solo si todos los costos son iguales
- **UCS**: Óptimo con cualquier costo positivo

### DLS y Límites
- Útil cuando se sabe dónde buscar
- Evita búsqueda infinita en grafos cíclicos

## 🎓 Conceptos Educativos

El proyecto demuestra:
- Estructuras de datos (cola, pila, heap)
- Reconstrucción de caminos
- Métricas de búsqueda
- Análisis comparativo
- Visualización de algoritmos

## ✅ Checklist de Requisitos

- [x] Implementar BFS correctamente
- [x] Implementar DFS correctamente
- [x] Implementar DLS con límite de profundidad
- [x] Implementar IDS con iteración de límites
- [x] Implementar UCS con cola de prioridad
- [x] Definir estado inicial y objetivo
- [x] Visualizar ruta encontrada
- [x] Mostrar nodos explorados
- [x] Indicar costo total (UCS)
- [x] Comparar resultados entre algoritmos
- [x] Usar estructuras adecuadas para cada algoritmo
- [x] Múltiples casos de prueba
- [x] Documentación completa

## 📝 Licencia

Este proyecto es de uso educativo.

## 👨‍💻 Autor

Implementación de algoritmos de búsqueda para propósitos educativos.

---

**¡Disfruta explorando algoritmos de búsqueda!** 🎯

## Aplicaciones

En [`aplicaciones/entrega_paquetes.ipynb`](aplicaciones/entrega_paquetes.ipynb)
los algoritmos del paquete se aplican a un problema real: planificar la entrega
de paquetes comparando estrategias de busqueda clasica. El notebook incluye los
resultados ejecutados.
