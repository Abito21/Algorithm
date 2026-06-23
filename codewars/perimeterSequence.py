"""
Perimeter sequence
The first three stages of a sequence are shown.

blocks

The blocksize is a by a and a ≥ 1.

What is the perimeter of the nth shape in the sequence (n ≥ 1) ?

Link : https://www.codewars.com/kata/589519d1f0902e01af000054

Pola yang terlihat dari problem
n=1 → satu kotak → keliling = 4a
n=2 → dua kotak tersambung → keliling = 8a
n=3 → tiga kotak tersambung dalam pola soal → keliling = 12a
Kuncinya setiap kota memiliki keliling yang bertambah 4.
"""

# Solution:
def perimeter_sequence(a, n): 
    return 4 * a * n
