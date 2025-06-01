# Projeto – Análise do Algoritmo QuickSort

Este projeto realiza uma análise teórica e prática do algoritmo **QuickSort**, desenvolvido como parte da disciplina de **Teoria da Computação** da CESAR School.

---

## 🎯 Objetivo

Analisar o comportamento do algoritmo QuickSort com foco em:
- Desempenho prático (tempo de execução real).
- Complexidade teórica (melhor caso, caso médio, pior caso).
- Comparação entre linguagens (Python e C).
- Visualização com gráficos.
- Classificação em P/NP.

---

## 📁 Estrutura do Projeto

- `python/` — Códigos Python:
  - `quicksort.py` — Implementação do algoritmo QuickSort em Python
  - `medir_tempos.py` — Mede tempo de execução, média e desvio padrão
  - `graficos.py` — Gera os gráficos 1,2 e 3 com matplotlib
  - `quicksort_casos.py` — Simula e compara os tempos de execução do QuickSort no melhor, médio e pior caso, executando 15 vezes cada cenário, gera o gráfico 4


- `c/` — Códigos em C:
  - `quicksort.c` — Implementação do algoritmo e testes de tempo
  - `medir_tempos.c` — Mede tempo de execução, média e desvio padrão

- `imgs/` — Gráficos gerados:
  - `grafico1_tempos.png` — Tempo médio de execução
  - `grafico2_desvios.png` — Desvio padrão das execuções
  - `grafico3_complexidade.png` — Complexidade teórica comparativa

- `relatorio/` — Documentação final:
  - `Projeto_Teoria_Computacao_QuickSort.pdf` — Relatório completo do projeto

- `dados/` — Dados coletados:
  - `resultados_execucoes.csv` — Arquivo com os tempos de execução obtidos (Python e C)
  
- `README.md` — Documento principal de apresentação do projeto

## 🧠 Conteúdo

### 1. Algoritmo QuickSort
- Implementado tanto em Python quanto em C.
- Usa estratégia "dividir para conquistar".
- Código comentado com clareza.
- Inclui pseudocódigo e exemplos no relatório.

### 2. Testes de Desempenho
- 3 tamanhos de entrada: **pequena (10), média (1000), grande (10000)**.
- Cada teste executado **15 vezes**.
- Cálculo de **média e desvio padrão** dos tempos.

### 3. Geração de Gráficos
- **Gráfico 1:** Tempo médio Python vs C  
- **Gráfico 2:** Desvio padrão das execuções  
- **Gráfico 3:** Complexidade Teórica (Ω, Θ, O)  
- **Gráfico 4:** Comparação prática entre melhor, médio e pior caso do QuickSort (em Python)  
- Visualização clara do crescimento assintótico e do desempenho real em diferentes linguagens e cenários.

### 4. Análise Teórica e Prática
- Complexidade assintótica:
  - Melhor caso: Ω(n log n)
  - Caso médio: Θ(n log n)
  - Pior caso: O(n²)
- Discussão sobre aplicabilidade e limitações.

### 5. Classe de Complexidade
- O QuickSort pertence à classe **P**.
- Não é um problema de decisão, logo não pertence à classe **NP**.
- É comparado a problemas **NP-completos** como TSP e Job Shop.

---

## 🧪 Como Executar

### ▶️ Python

```bash
cd python/
python medir_tempos.py     # Executa os testes e coleta tempo, média e desvio padrão
python graficos.py         # Gera os gráficos 1,2 e 3 com base nos dados obtidos
python quicksort_casos.py     # Executa 15 vezes o melhor, médio e pior caso do QuickSort e gera o gráfico 4
```

📦 Requisitos:
- `matplotlib`
- `pandas`
- `numpy`

Instale com:

```bash
pip install matplotlib pandas numpy
```

---

### 💻 C

```bash
cd c/
gcc quicksort.c -o quicksort.exe
./quicksort.exe
```

---

## 📊 Resultados

Os gráficos gerados automaticamente estão disponíveis na pasta:

```
/imgs/
```

Eles também estão inseridos e discutidos no relatório final em PDF.

---

## 📄 Relatório

O documento completo do projeto pode ser acessado em:

```
/relatorio/Projeto_Teoria_Computacao_QuickSort.pdf
```

O relatório inclui:
- ✅ Descrição detalhada do algoritmo QuickSort  
- ✅ Análise assintótica (Ω, Θ, O)  
- ✅ Aplicabilidade prática  
- ✅ Testes empíricos com Python e C  
- ✅ Gráficos comparativos comentados  
- ✅ Reflexão sobre classes P, NP e problemas relacionados  

---

## 👨‍💻 Autores

- Gabriel Antônio de Oliveira Rocha  
- Enzo de Barros Nunes  
- Davi Maurício Araújo Pereira  

**CESAR School – 2024/2025**

---

## 🔗 Licença

Este projeto é acadêmico e de uso livre para fins educacionais.