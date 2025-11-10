#include <stdio.h>
#include <stdlib.h>

typedef struct {
		int pos;
		long long people;
} Gate;

int compare(const void *a, const void *b) {
		Gate *ga = (Gate *)a;
		Gate *gb = (Gate *)b;
		return ga->pos - gb->pos;
}

int can_assign(Gate * gates, int k, int N, int D) {
		long long pos = 1;
		
		for (int i = 0; i < k; i++) {
			int gate_pos = gates[i].pos;
			long long people = gates[i].people;
			
			long long left = gate_pos - D;
			long long right = gate_pos + D;
			
			long long start = (pos > left) ? pos : left;
			
			if (start > right) {
					return 0;
			}
			
			long long end = start + people - 1;
			if (end > right || end > N) {
					return 0;
			}
			
			pos = end + 1;
		}
		
		return 1;
}

int solve(int N, int K, int *A, long long *B) {
		Gate *gates = (Gate *)malloc(K * sizeof(Gate));
		int k_filtered = 0;
		long long total = 0;
		
		for (int i = 0; i < K; i++) {
				if (B[i] > 0) {
						gates[k_filtered].pos = A[i];
						gates[k_filtered].people = B[i];
						k_filtered++;
						total += B[i];
				}
		}
		
		if (k_filtered == 0) {
			 free(gates);
			 return 0;
		}
		
		if (total > N) {
			 free(gates);
			 return -1;
		}
		
		qsort(gates, k_filtered, sizeof(Gate), compare);
		
		int lo = 0, hi = N, ans = -1;
		
		while (lo <= hi) {
				int mid = (lo + hi) >> 1;
				
				if (can_assign(gates, k_filtered, N, mid)) {
						ans = mid;
						hi = mid - 1;
				} else {
						lo = mid + 1;
				}
		}
		
		free(gates);
		return ans;
}

int main() {
    int T, tc;
    scanf("%d", &T);
    
    for (tc = 0; tc < T; tc++) {
        int N, K, i;
        scanf("%d %d", &N, &K);
        
        int *A = (int *)malloc(K * sizeof(int));
        long long *B = (long long *)malloc(K * sizeof(long long));
        
        for (i = 0; i < K; i++) scanf("%d", &A[i]);
        for (i = 0; i < K; i++) scanf("%lld", &B[i]);
        
        Gate *gates = (Gate *)malloc(K * sizeof(Gate));
        int k_filtered = 0;
        long long total = 0;
        
        for (i = 0; i < K; i++) {
            if (B[i] > 0) {
                gates[k_filtered].pos = A[i];
                gates[k_filtered].people = B[i];
                k_filtered++;
                total += B[i];
            }
        }
        
        if (k_filtered == 0) {
            printf("0\n");
            free(A);
            free(B);
            free(gates);
            continue;
        }
        
        if (total > N) {
            printf("-1\n");
            free(A);
            free(B);
            free(gates);
            continue;
        }
        
        qsort(gates, k_filtered, sizeof(Gate), compare);
        
        int lo = 0, hi = N, ans = -1;
        
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can_assign(gates, k_filtered, N, mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        
        printf("%d\n", ans);
        
        free(A);
        free(B);
        free(gates);
    }
    
    return 0;
}