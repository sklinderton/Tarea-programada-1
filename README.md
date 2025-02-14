# TAREA PROGRAMADA 1 - Estructura del Proyecto
TAREA_PROGRAMADA_1/
│
├── Parte_1/
│ ├── algoritmos_ordenamiento.py
│ ├── lector_data.py
│ ├── main.py
│ └── punt_play.py
│
└── Parte_2/
├── algoritmos_ordenamiento_parte2.py
├── lector_data_parte2.py
├── main_parte2.py
├── play_comparator.py
└── punt_play_parte2.py

### Descripción de la Estructura

1. **Raíz del Proyecto**:
   - `Parte_1/` y `Parte_2/`: Subdirectorios para cada parte de la tarea.

2. **Parte 1**:
   - `algoritmos_ordenamiento.py`: Implementación de algoritmos de ordenamiento para la Parte 1.
   - `lector_data.py`: Clase para leer archivos CSV de jugadas de punt.
   - `main.py`: Script principal para ejecutar la Parte 1.
   - `punt_play.py`: Clase que representa una jugada de punt (atributos básicos).

3. **Parte 2**:
   - `algoritmos_ordenamiento_parte2.py`: Algoritmos adaptados para usar `play_comparator`.
   - `lector_data_parte2.py`: Lector de datos con atributos adicionales (fecha y hora).
   - `main_parte2.py`: Script principal para ejecutar la Parte 2.
   - `play_comparator.py`: Clase para comparar jugadas con múltiples criterios.
   - `punt_play_parte2.py`: Clase extendida de `punt_play` con fecha y hora.

---

### Notas Adicionales
- Los archivos de datos CSV deben ubicarse en `c:\data\primeraprogramada` (Windows) o `/data/primeraprogramada` (Linux/Mac).
- Los resultados se generan en la misma carpeta de datos con el formato `parteX-[algoritmo]-resultado_YYYY.csv`.
