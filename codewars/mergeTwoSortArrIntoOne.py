"""
Problem:
Description:
You are given two sorted arrays that contain only integers. These arrays may be sorted in either ascending or descending order. Your task is to merge them into a single array, ensuring that:

The resulting array is sorted in ascending order.

Any duplicate values are removed, so each integer appears only once.

If both input arrays are empty, return an empty array.

No input validation is needed, as both arrays are guaranteed to contain zero or more integers.

Examples (input -> output)
* [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
Happy coding!

Link : https://www.codewars.com/kata/5899642f6e1b25935d000161
"""

# Solution:
def merge_arrays(a, b):
    hasil = []

    if len(a) < 2:
        asc_a = True
    else:
        asc_a = a[0] <= a[1]

    if len(b) < 2:
        asc_b = True
    else:
        asc_b = b[0] <= b[1]

    if asc_a:
        kiri_a = 0
        kanan_a = len(a) - 1
    else:
        kiri_a = len(a) - 1
        kanan_a = 0

    if asc_b:
        kiri_b = 0
        kanan_b = len(b) - 1
    else:
        kiri_b = len(b) - 1
        kanan_b = 0

    aa = []
    bb = []

    i = kiri_a
    while True:
        if len(a) == 0:
            break

        aa.append(a[i])

        if i == kanan_a:
            break

        if asc_a:
            i += 1
        else:
            i -= 1

    j = kiri_b
    while True:
        if len(b) == 0:
            break

        bb.append(b[j])

        if j == kanan_b:
            break

        if asc_b:
            j += 1
        else:
            j -= 1

    i = 0
    j = 0

    while i < len(aa) or j < len(bb):

        if i >= len(aa):
            nilai = bb[j]
            j += 1

        elif j >= len(bb):
            nilai = aa[i]
            i += 1

        elif aa[i] < bb[j]:
            nilai = aa[i]
            i += 1

        elif bb[j] < aa[i]:
            nilai = bb[j]
            j += 1

        else:
            nilai = aa[i]
            i += 1
            j += 1

        if len(hasil) == 0 or hasil[len(hasil) - 1] != nilai:
            hasil.append(nilai)

    return hasil
