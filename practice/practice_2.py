#!/bin/python3

import os
import sys
import bisect

# Fungsi untuk membangun Sparse Table (untuk Range Maximum Query))
def build_sparse_table_max(arr):
		m = len(arr)
		if m == 0:
				return [], [0]
				
		LOG = (m).bit_length()
		st = [arr[:]] # level 0
		k = 1
		while (1 << k) <= m:
				prev = st[k-1]
				step = 1 << (k - 1)
				cur = [max(prev[i], prev[i + step]) for i in range(m - (1 << k) + 1)]
				st.append(cur)
				k += 1
				
		log2 = [0] * (m +1)
		for i in range(2, m + 1):
				log2[1] = log2[i // 2] + 1
		return st, log2

# Fungsi untuk mengambil nilai maksimum pada rentang [l, r]
def range_max_query(st, log2, l, r):
		if l > r:
				return 0
		length = r - l + 1
		k = log2[length]
		return max(st[k][l], st[k][r - (1 << k) + 1])

# Fungsi utama untuk menghitung proteksi minimum tiap portal		
def teleportation_portals(N, P1, P2, A):
		# Gabungkan semua portal (dua pusat + N portal baru)
		B = [P1, P2] + A[:]
		B.sort()
		m = len(B)
		
		# Jika hanya satu portal, maka tidak perlu proteksi
		if m <= 1:
				return [0] * N
				
		# Hitung jarak antar portal berurutan
		w = [B[i + 1] - B[i] for i in range(m - 1)]
		
		# Bangun Sparse Table untuk range maximum query
		st, log2 = build_sparse_table_max(w)
		
		# Temukan index P1 dan P2 dalam array B yang suah diurutkan
		idxP1 = bisect.bisect_left(B, P1)
		idxP2 = bisect.bisect_left(B, P2)
		
		result = []
		for x in A:
				idx = bisect.bisect_left(B, x)
				
				# Hitung jarak maksimum P1
				if idx == idxP1:
						max1 = 0
				else:
						l = min(idx, idxP1)
						r = max(idx, idxP1) - 1
						max1 = range_max_query(st, log2, l, r)
				
				# Hitung jarak maksimum ke P2
				if idx == idxP2:
						max2 = 0
				else:
						l = min(idx, idxP2)
						r = max(idx, idxP2) - 1
						max2 = range_max_query(st, log2, l, r)
						
				# Ambil nilai proteksi minimum antara dua rute
				result.append(min(max1, max2))
				
		return result
		
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())
    for _ in range(T):
        N, P1, P2 = map(int, input().split())
        A = list(map(int, input().split()))
        result = teleportation_portals(N, P1, P2, A)
        fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()