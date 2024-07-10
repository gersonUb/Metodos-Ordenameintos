import pytest
from src.ordenamiento import MetodosDeOrdenamientos

@pytest.fixture
def sorting_instance():
    return lambda lista: MetodosDeOrdenamientos(lista.copy())

def test_selection_sort(sorting_instance):
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    lista1_ordenada = [11, 12, 22, 25, 34, 64, 90]
    lista2 = [1, 11, 111, 1, 11, 0]
    lista2_ordenada = [0, 1, 1, 11, 11, 111]
    assert sorting_instance(lista1).selectionSort() == lista1_ordenada
    assert sorting_instance(lista2).selectionSort() == lista2_ordenada

def test_insertion_sort(sorting_instance):
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    lista1_ordenada = [11, 12, 22, 25, 34, 64, 90]
    lista2 = [1, 11, 111, 1, 11, 0]
    lista2_ordenada = [0, 1, 1, 11, 11, 111]
    assert sorting_instance(lista1).insertionSort() == lista1_ordenada
    assert sorting_instance(lista2).insertionSort() == lista2_ordenada

def test_quick_sort(sorting_instance):
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    lista1_ordenada = [11, 12, 22, 25, 34, 64, 90]
    lista2 = [1, 11, 111, 1, 11, 0]
    lista2_ordenada = [0, 1, 1, 11, 11, 111]
    assert sorting_instance(lista1).quickSort() == lista1_ordenada
    assert sorting_instance(lista2).quickSort() == lista2_ordenada

def test_merge_sort(sorting_instance):
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    lista1_ordenada = [11, 12, 22, 25, 34, 64, 90]
    lista2 = [1, 11, 111, 1, 11, 0]
    lista2_ordenada = [0, 1, 1, 11, 11, 111]
    assert sorting_instance(lista1).mergeSort() == lista1_ordenada
    assert sorting_instance(lista2).mergeSort() == lista2_ordenada
