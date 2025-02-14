import os
from lector_data import lector_data
from algoritmos_ordenamiento import (
    bubble_sort, 
    insertion_sort, 
    merge_sort_recursivo, 
    merge_sort_iterativo,
    quicksort_recursivo,
    quicksort_iterativo
)

def escribir_resultados(arr, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write("GameID,Teams,Yards,Quarter\n")
        for jugada in arr:
            file.write(str(jugada) + '\n')

def main():
    print("Iniciando lectura de archivos...")
    lector = lector_data()
    jugadas_punt = lector.read_punts()
    
    if not jugadas_punt:
        print("No se encontraron jugadas para procesar")
        return
        
    print("\nIniciando ordenamiento de jugadas...")
    
    algoritmos = {
        'bubble': (bubble_sort, 'parte1-bubble-sort-resultado_{year}.csv'),
        'insertion': (insertion_sort, 'parte1-insertion-sort-resultado_{year}.csv'),
        'merge_recursivo': (merge_sort_recursivo, 'parte1-merge-sort-rec-resultado_{year}.csv'),
        'merge_iterativo': (merge_sort_iterativo, 'parte1-merge-sort-iter-resultado_{year}.csv'),
        'quick_recursivo': (quicksort_recursivo, 'parte1-quick-sort-rec-resultado_{year}.csv'),
        'quick_iterativo': (quicksort_iterativo, 'parte1-quick-sort-iter-resultado_{year}.csv')
    }
    
    jugadas_por_anio = {}
    for jugada in jugadas_punt:
        year = jugada._game_id[:4] 
        if year not in jugadas_por_anio:
            jugadas_por_anio[year] = []
        jugadas_por_anio[year].append(jugada)

    for nombre, (algoritmo, archivo_salida) in algoritmos.items():
        print(f"\nEjecutando {nombre}...")
        
        for year, jugadas in jugadas_por_anio.items():
            print(f"Procesando año {year}...")
            jugadas_actuales = jugadas.copy() 
            stats = algoritmo(jugadas_actuales)
            
            print(f"Tiempo de ejecución ({year}): {stats['tiempo']:.4f} segundos")
            print(f"Comparaciones ({year}): {stats['comparaciones']}")
            print(f"Intercambios ({year}): {stats['intercambios']}")

            ruta_completa = os.path.join(
                'c:\\data\\primeraprogramada' if os.name == 'nt' else '/data/primeraprogramada',
                archivo_salida.format(year=year)
            )
            escribir_resultados(jugadas_actuales, ruta_completa)
            print(f"Resultados guardados en: {ruta_completa}")

if __name__ == "__main__":
    main()