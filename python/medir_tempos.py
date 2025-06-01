import random
import time
import statistics

# Algoritmo QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

# Função para testar e medir tempo
def testar_tempo(tamanho, rotulo):
    tempos = []
    print(f"\n== {rotulo.upper()} ==")
    print(f"Tamanho: {tamanho}\n")

    for i in range(15):
        lista = random.sample(range(1, tamanho * 10), tamanho)
        inicio = time.perf_counter()
        quicksort(lista)
        fim = time.perf_counter()
        tempo = fim - inicio
        tempos.append(tempo)
        print(f"Execução {i+1:2d}: {tempo:.9f} segundos")

    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    print(f"\nMédia de tempo: {media:.9f} segundos")
    print(f"Desvio padrão: {desvio:.9f} segundos")

# Rodar para entradas pequena, média e grande
testar_tempo(10, "pequena")
testar_tempo(1000, "média")
testar_tempo(10000, "grande")
