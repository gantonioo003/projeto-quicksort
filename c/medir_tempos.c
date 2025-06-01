#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

void troca(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int particiona(int arr[], int baixo, int alto) {
    int pivo = arr[alto];
    int i = (baixo - 1);
    for (int j = baixo; j < alto; j++) {
        if (arr[j] <= pivo) {
            i++;
            troca(&arr[i], &arr[j]);
        }
    }
    troca(&arr[i + 1], &arr[alto]);
    return (i + 1);
}

void quicksort(int arr[], int baixo, int alto) {
    if (baixo < alto) {
        int pi = particiona(arr, baixo, alto);
        quicksort(arr, baixo, pi - 1);
        quicksort(arr, pi + 1, alto);
    }
}

void gerar_lista(int *lista, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        lista[i] = rand() % (tamanho * 10);
    }
}

double medir_tempo_execucao(void (*func)(int*, int, int), int* arr, int tamanho) {
    LARGE_INTEGER inicio, fim, frequencia;
    QueryPerformanceFrequency(&frequencia);
    QueryPerformanceCounter(&inicio);

    func(arr, 0, tamanho - 1);

    QueryPerformanceCounter(&fim);
    return (double)(fim.QuadPart - inicio.QuadPart) / frequencia.QuadPart;
}

void testar_execucoes(int tamanho, const char *rotulo) {
    double tempos[15];
    printf("\n== %s ==\n", rotulo);
    printf("Tamanho: %d\n", tamanho);

    for (int i = 0; i < 15; i++) {
        int *lista = malloc(sizeof(int) * tamanho);
        gerar_lista(lista, tamanho);

        tempos[i] = medir_tempo_execucao(quicksort, lista, tamanho);
        printf("Execucao %2d: %.9f segundos\n", i + 1, tempos[i]);

        free(lista);
    }

    // Média
    double soma = 0.0;
    for (int i = 0; i < 15; i++) soma += tempos[i];
    double media = soma / 15.0;

    // Desvio padrão
    double variancia = 0.0;
    for (int i = 0; i < 15; i++) variancia += pow(tempos[i] - media, 2);
    variancia /= 14.0;
    double desvio = sqrt(variancia);

    printf("\nMedia de tempo: %.9f segundos\n", media);
    printf("Desvio padrao: %.9f segundos\n", desvio);
}

int main() {
    srand(GetTickCount());

    testar_execucoes(10, "ENTRADA PEQUENA");
    testar_execucoes(1000, "ENTRADA MEDIA");
    testar_execucoes(10000, "ENTRADA GRANDE");

    return 0;
}
