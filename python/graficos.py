import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados de entrada agregados
dados = {
    "Entrada": ["Pequena (10)", "Média (1000)", "Grande (10000)"],
    "Python Média (s)": [0.000037660, 0.004762167, 0.041407687],
    "Python Desvio (s)": [0.000012109, 0.001355305, 0.010236077],
    "C Média (s)": [0.000000953, 0.000133193, 0.001953973],
    "C Desvio (s)": [0.000000270, 0.000037794, 0.000416724],
    "Teórico Médio (Θ)": [np.log2(10)*10, np.log2(1000)*1000, np.log2(10000)*10000],
    "Teórico Pior (O)": [10**2, 1000**2, 10000**2]
}

# Melhor caso 5% abaixo do médio, apenas para visualização
dados["Teórico Melhor (Ω)"] = [val * 0.95 for val in dados["Teórico Médio (Θ)"]]

df = pd.DataFrame(dados)
x = np.arange(len(df["Entrada"]))

# === Gráfico 1: Tempo médio de execução ===
plt.figure(figsize=(10, 6))
plt.plot(x, df["Python Média (s)"], marker='o', label="Python", color='blue')
plt.plot(x, df["C Média (s)"], marker='o', label="C", color='orange')
plt.title("Gráfico 1 - Tempo Médio de Execução por Linguagem")
plt.ylabel("Tempo (segundos)")
plt.xlabel("Tamanho da Entrada")
plt.xticks(x, df["Entrada"])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Gráfico 2: Desvio padrão ===
plt.figure(figsize=(10, 6))
plt.plot(x, df["Python Desvio (s)"], marker='s', color='blue', label="Python (Desvio)")
plt.plot(x, df["C Desvio (s)"], marker='s', color='orange', label="C (Desvio)")
plt.title("Gráfico 2 - Desvio Padrão dos Tempos de Execução")
plt.ylabel("Desvio padrão (segundos)")
plt.xlabel("Tamanho da Entrada")
plt.xticks(x, df["Entrada"])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Gráfico 3: Complexidade Teórica (Colunas + Linha Tracejada) ===
max_valor = max(df["Teórico Pior (O)"])
df["Melhor_norm"] = df["Teórico Melhor (Ω)"] / max_valor
df["Médio_norm"] = df["Teórico Médio (Θ)"] / max_valor
df["Pior_norm"] = df["Teórico Pior (O)"] / max_valor

largura = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - largura, df["Melhor_norm"], width=largura, label="Melhor caso (Ω)", color='green')
plt.bar(x, df["Médio_norm"], width=largura, label="Caso médio (Θ)", color='blue')
plt.bar(x + largura, df["Pior_norm"], width=largura, label="Pior caso (O)", color='red')
plt.plot(x, df["Melhor_norm"], 'g--', linewidth=1, label="Linha Ω")
plt.plot(x, df["Médio_norm"], 'b--', linewidth=1, label="Linha Θ")
plt.plot(x, df["Pior_norm"], 'r--', linewidth=1, label="Linha O")

plt.xticks(x, df["Entrada"])
plt.ylabel("Complexidade (normalizada)")
plt.xlabel("Tamanho da Entrada")
plt.title("Gráfico 3 - Complexidade Teórica do QuickSort")
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.show()
