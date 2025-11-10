#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int swapped; // Optimasi: cek apakah ada pertukaran
    
    for (i = 0; i < n - 1; i++) {
        swapped = 0;
        
        // Elemen terbesar akan "mengapung" ke akhir
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Tukar elemen
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        
        // Jika tidak ada pertukaran, array sudah terurut
        if (swapped == 0)
            break;
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {25, 64, 22, 12, 34};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Array sebelum diurutkan: ");
    printArray(arr, n);
    
    bubbleSort(arr, n);
    
    printf("Array setelah diurutkan: ");
    printArray(arr, n);
    
    return 0;
}