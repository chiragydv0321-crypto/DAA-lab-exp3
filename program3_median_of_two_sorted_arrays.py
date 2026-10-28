"""
Experiment 3: Matrix and Binary Search
Program 3: Median of Two Sorted Arrays
Aim: Find the median by merging the two sorted arrays.
"""

def median_two_sorted(a, b):
    merged, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged += a[i:] + b[j:]
    n = len(merged)
    if n % 2:
        return merged[n // 2]
    return (merged[n // 2 - 1] + merged[n // 2]) / 2

print(median_two_sorted([1, 3], [2]))
