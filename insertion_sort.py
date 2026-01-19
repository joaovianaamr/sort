# algoritmo que implementa o insertion sort em Python

# O(n^2) versão recursiva do insertion sort
# mais complexa de entender
def insertion_sort(arr: list, index: int = 0):
    if index == len(arr) - 1:
        return
    
    # Swap com o próximo elemento se necessário
    if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
    
    # Move o elemento para sua posição correta
    aux = index
    while aux > 0 and arr[aux] < arr[aux - 1]:
        arr[aux], arr[aux - 1] = arr[aux - 1], arr[aux]
        aux -= 1
    
    insertion_sort(arr, index + 1)

# O(n^2) versão iterativa do insertion sort
# mais simples de entender
def insertion_sort_iterativo(arr: list):
    for index in range(1, len(arr)):
        aux = index
        while aux > 0 and arr[aux] < arr[aux - 1]:
            arr[aux - 1], arr[aux] = arr[aux], arr[aux - 1]
            aux -= 1

# Testando a versão recursiva
print("Versão recursiva:")
arr_recursiva = [13, 8, 3, 5, 2]
insertion_sort(arr_recursiva)
print(arr_recursiva)

# Testando a versão iterativa
print("\nVersão iterativa:")
arr_iterativa = [13, 8, 3, 5, 2]
insertion_sort_iterativo(arr_iterativa)
print(arr_iterativa)
