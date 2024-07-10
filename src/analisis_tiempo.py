import time
import random
import matplotlib.pyplot as plt
from ordenamiento import MetodosDeOrdenamientos
    
def plot_tiempo_analisis1():
    sizes = [10, 50, 100, 200, 500]
    time_quick = []
    time_merge = []
    time_selection = []
    time_insertion = []

    for size in sizes:
        lista = list(range(size, 0, -1))  # Lista inversamente ordenada de tamaño 'size'

        # Medir el tiempo de ejecución para Merge Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista.copy())
        ordenar.mergeSort()
        end_time = time.time()
        time_merge.append(end_time - start_time)

        # Medir el tiempo de ejecución para Selection Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista.copy())
        ordenar.selectionSort()
        end_time = time.time()
        time_selection.append(end_time - start_time)

        # Medir el tiempo de ejecución para Insertion Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista.copy())
        ordenar.insertionSort()
        end_time = time.time()
        time_insertion.append(end_time - start_time)
        
        # Medir el tiempo de ejecución para Quick Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista.copy())
        ordenar.quickSort()
        end_time = time.time()
        time_quick.append(end_time - start_time)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, time_quick, marker='o', color='b', label='Quick Sort')
    plt.plot(sizes, time_selection, marker='s', color='r', label='Selection Sort')
    plt.plot(sizes, time_insertion, marker='^', color='g', label='Insertion Sort')
    plt.plot(sizes, time_merge, marker='d', color='y', label='Merge Sort') 
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Tiempo de Ejecución de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./src/data/grafico1.jpg')
    plt.show()

# Llamar a la función para graficar el tiempo de ejecución
if __name__ == "__main__":
    plot_tiempo_analisis1()
    
def generar_lista_aleatoria(size):
    lista = list(range(1, size+1))
    random.shuffle(lista)
    return lista
    
def plot_tiempo_analisis2():
    sizes = [10, 50, 100, 200, 500]
    time_quick = []
    time_merge = []
    time_selection = []
    time_insertion = []
    
    for size in sizes:
        lista_aleatoria = generar_lista_aleatoria(size)
        
        # Medir el tiempo de ejecución para Merge Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista_aleatoria.copy())
        ordenar.mergeSort()
        end_time = time.time()
        time_merge.append(end_time - start_time)
        
        # Medir el tiempo de ejecucion para Quick Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista_aleatoria.copy())
        ordenar.quickSort()
        end_time = time.time()
        time_quick.append(end_time - start_time)
        
        # Medir el tiempo de ejecucion para Insertion Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista_aleatoria.copy())
        ordenar.insertionSort()
        end_time = time.time()
        time_insertion.append(end_time - start_time)
        
        # Medir el tiempo de ejecucion para Selection Sort
        start_time = time.time()
        ordenar = MetodosDeOrdenamientos(lista_aleatoria.copy())
        ordenar.selectionSort()
        end_time = time.time()
        time_selection.append(end_time - start_time)
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, time_quick, marker='o', color='b', label='Quick Sort')
    plt.plot(sizes, time_selection, marker='d', color='r', label='Selection Sort')
    plt.plot(sizes, time_insertion, marker='d', color='g', label='Insertion Sort')
    plt.plot(sizes, time_merge, marker='o', color='y', label='Merge Sort') 
    plt.xlabel('Tamaño de la Lista Aleatoria')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Tiempo de Ejecución de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./src/data/grafico2.jpg')
    plt.show()
    
# Llamar a la función para graficar el tiempo de ejecución
if __name__ == "__main__":
    plot_tiempo_analisis2()