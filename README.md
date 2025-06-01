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

Projeto-QuickSort/
├── python/
│ ├── quicksort.py # Algoritmo em Python
│ ├── medir_tempos.py # Mede tempo, média e desvio padrão
│ ├── graficos.py # Gera os gráficos (matplotlib)
│ └── gerar_entradas.py # (opcional) geração separada de entradas
│
├── c/
│ ├── quicksort.c # Algoritmo + testes de tempo em C
│ └── Makefile # (opcional) para compilar rápido
│
├── imgs/
│ ├── grafico1_tempos.png # Tempo médio
│ ├── grafico2_desvios.png # Desvio padrão
│ └── grafico3_complexidade.png # Complexidade teórica
│
├── relatorio/
│ └── Projeto_Teoria_Computacao_QuickSort.pdf
│
└── README.md

markdown
Copiar
Editar

---

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
- **Gráfico 2:** Desvio padrão
- **Gráfico 3:** Complexidade Teórica (Ω, Θ, O)
- Visualização clara do crescimento assintótico e desempenho real.

### 4. Análise Teórica
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

### Python

```bash
cd python/
python medir_tempos.py     # Coleta média e desvio
python graficos.py         # Gera gráficos com base nos dados
Requisitos: matplotlib, pandas, numpy

Instalar com:

bash
Copiar
Editar
pip install matplotlib pandas numpy
C
bash
Copiar
Editar
cd c/
gcc quicksort.c -o quicksort.exe
./quicksort.exe
📊 Resultados
Os gráficos podem ser encontrados na pasta /imgs e também inseridos no relatório em PDF.

📄 Relatório
O relatório completo está disponível em:

📁 /relatorio/Projeto_Teoria_Computacao_QuickSort.pdf

O documento aborda:

Descrição detalhada do algoritmo

Análise assintótica

Aplicabilidade

Testes empíricos

Gráficos comentados

Reflexão final sobre classe P e NP

👨‍💻 Autores
Gabriel Antônio de Oliveira Rocha

Enzo de Barros Nunes

Davi Maurício Araújo Pereira

CESAR School – 2024/2025

🔗 Licença
Este projeto é acadêmico e de uso livre para fins educacionais.

go
Copiar
Editar
