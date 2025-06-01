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
