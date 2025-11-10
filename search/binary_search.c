#include<stdio.h>
#include<string.h>


// Binary Search - Iterative (lebih efisien)
int binarySearch(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;

    while (left <= right) {
        // cari middle point (hindari overflow)
        int mid = left + (right - left) / 2;
        printf("Mencari di range [%d, %d], mid=%d, arr[mid]=%d\n", left, right, mid, arr[mid]);

        // jika target ketemu di tengah
        if (arr[mid] == target) {
            return mid;
        }

        // jika target lebih besar, abaikan separuh di kiri
        if (arr[mid] < target) {
            left = mid + 1;
        } 
        // jika target lebih kecil, abaikan separuh di kanan
        else {
            right = mid - 1;
        }
    }

    return -1; // tidak ditemukan
}



// Binary Search - Recursive
int binarySearchRecursive(int arr[], int left, int right, int target) {
    if (left > right) {
        return -1; // base case, apabila tidak ditemukan
    }

    int mid = left + (right - left) / 2;

    if (arr[mid] == target) {
        return mid; // target ditemukan
    }

    if (arr[mid] < target) {
        // cari separuh di kanan
        return binarySearchRecursive(arr, mid + 1, right, target);
    } 
    // cari separuh di kiri
    else {
        return binarySearchRecursive(arr, left, mid - 1, target);
    }
}



// Binary Search untuk string (sorted)
int binarySearchString(char arr[][50], int n, char *target) {
    int left = 0;
    int right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        int cmp = strcmp(arr[mid], target);

        if (cmp == 0) {
            return mid;
        } else if (cmp < 0) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}



// Aplikasi praktis: Mencari harga produk berdasarkan ID (sorted by ID)
typedef struct {
    int id;
    char name[50];
    float price;
} Product;

int searchProductById(Product products[], int n, int targetId) {
    int left = 0, right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (products[mid].id == targetId) {
            return mid;
        } else if (products[mid].id < targetId) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    // Contoh 1: Binary Search Integer
    printf("=== BINARY SEARCH - INTEGER ===\n");
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    
    printf("Array terurut: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\nMencari: %d\n\n", target);
    
    int result = binarySearch(arr, n, target);
    if (result != -1) {
        printf("\nKetemu di index: %d\n", result);
    } else {
        printf("\nTidak ketemu\n");
    }
    
    // Contoh 2: Binary Search Recursive
    printf("\n=== BINARY SEARCH - RECURSIVE ===\n");
    target = 67;
    printf("Mencari: %d\n", target);
    result = binarySearchRecursive(arr, 0, n - 1, target);
    printf("Hasil: index %d\n", result);
    
    // Contoh 3: Binary Search String
    printf("\n=== BINARY SEARCH - STRING ===\n");
    char words[][50] = {"apple", "banana", "cherry", "date", "grape", "mango"};
    int wordCount = 6;
    char searchWord[] = "cherry";
    
    printf("Words (sorted): ");
    for (int i = 0; i < wordCount; i++) {
        printf("%s ", words[i]);
    }
    printf("\nMencari: %s\n", searchWord);
    
    result = binarySearchString(words, wordCount, searchWord);
    if (result != -1) {
        printf("Ketemu di index: %d\n", result);
    } else {
        printf("Tidak ketemu\n");
    }
    
    // Contoh 4: Practical - Product Search
    printf("\n=== PRACTICAL EXAMPLE - PRODUCT SEARCH ===\n");
    Product products[] = {
        {101, "Laptop", 5000000},
        {105, "Mouse", 150000},
        {110, "Keyboard", 300000},
        {115, "Monitor", 2000000},
        {120, "Headset", 500000}
    };
    int productCount = 5;
    int searchId = 110;
    
    printf("Products (sorted by ID):\n");
    for (int i = 0; i < productCount; i++) {
        printf("ID: %d, Name: %s, Price: %.0f\n", 
               products[i].id, products[i].name, products[i].price);
    }
    printf("\nMencari product dengan ID: %d\n", searchId);
    
    result = searchProductById(products, productCount, searchId);
    if (result != -1) {
        printf("Ketemu!\n");
        printf("Name: %s\n", products[result].name);
        printf("Price: Rp %.0f\n", products[result].price);
    } else {
        printf("Product tidak ditemukan\n");
    }
    
    // Perbandingan Performa
    printf("\n=== PERBANDINGAN PERFORMA ===\n");
    printf("Untuk array dengan 11 elemen:\n");
    printf("- Linear Search: worst case = 11 comparisons\n");
    printf("- Binary Search: worst case = 4 comparisons (log2(11) ≈ 4)\n");
    printf("\nUntuk 1000 elemen:\n");
    printf("- Linear Search: worst case = 1000 comparisons\n");
    printf("- Binary Search: worst case = 10 comparisons\n");
    
    return 0;
}