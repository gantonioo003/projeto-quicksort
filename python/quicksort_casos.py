import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)  # aumenta o limite se quiser testar mais

def quicksort_melhor(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    pivo = arr[meio]
    menores = [x for i, x in enumerate(arr) if x < pivo or (x == pivo and i != meio)]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return quicksort_melhor(menores) + iguais + quicksort_melhor(maiores)

def quicksort_medio(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[0]
    menores = [x for x in arr[1:] if x <= pivo]
    maiores = [x for x in arr[1:] if x > pivo]
    return quicksort_medio(menores) + [pivo] + quicksort_medio(maiores)

def quicksort_pior(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[-1]
    menores = [x for x in arr[:-1] if x <= pivo]
    maiores = [x for x in arr[:-1] if x > pivo]
    return quicksort_pior(menores) + [pivo] + quicksort_pior(maiores)

def medir_tempo(funcao, entrada):
    inicio = time.perf_counter()
    funcao(entrada)
    fim = time.perf_counter()
    return fim - inicio

execucoes = 15
tamanho = 500

tempos_melhor = []
tempos_medio = []
tempos_pior = []

print("Rodando 15 execuções para cada caso...")

for _ in range(execucoes):
    lista_base = random.sample(range(tamanho * 10), tamanho)
    entrada_melhor = sorted(lista_base)
    entrada_medio = lista_base.copy()
    entrada_pior = sorted(lista_base)

    tempos_melhor.append(medir_tempo(quicksort_melhor, entrada_melhor.copy()))
    tempos_medio.append(medir_tempo(quicksort_medio, entrada_medio.copy()))
    tempos_pior.append(medir_tempo(quicksort_pior, entrada_pior.copy()))

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(range(1, execucoes+1), tempos_melhor, label="Melhor Caso (Ω(n log n))", marker='o')
plt.plot(range(1, execucoes+1), tempos_medio, label="Caso Médio (Θ(n log n))", marker='^')
plt.plot(range(1, execucoes+1), tempos_pior, label="Pior Caso (O(n²))", marker='x')
plt.title("Comparação de Tempos — QuickSort: Melhor, Médio e Pior Caso")
plt.xlabel("Execução")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
