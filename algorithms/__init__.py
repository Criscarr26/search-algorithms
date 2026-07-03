"""Paquete de algoritmos de búsqueda desinformada."""

from .bfs import busqueda_amplitud
from .dfs import busqueda_profundidad
from .dls import busqueda_profundidad_limitada
from .ids import busqueda_profundizacion_iterativa
from .ucs import busqueda_costo_uniforme

__all__ = [
    'busqueda_amplitud',
    'busqueda_profundidad',
    'busqueda_profundidad_limitada',
    'busqueda_profundizacion_iterativa',
    'busqueda_costo_uniforme'
]
