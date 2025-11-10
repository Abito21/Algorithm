def lampuDanTombolSpesial(N, L):
		count = 0
		# Loop dari lampu peryama sampai ketika terakhir
		for i in range(N-2):
				if L[i] == 0:
						# Tekan tombol i+1 (indeks i+1)
						count += 1
						# Toggle lampu i, i+1, i+2
						L[i] = 1 - L[i]
						L[i+1] = 1 - L[i+1]
						L[i+2] = 1 - L[i+2]
						
		# Setelah semua tombol dicoba, cek apakah semua lampu menyala
		if all(x == 1  for x in L):
				return f"YES {count}"
		else:
				return "NO -1"