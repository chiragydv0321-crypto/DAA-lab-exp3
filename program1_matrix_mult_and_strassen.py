"""
Experiment 3: Matrix and Binary Search
Program 1: Matrix Multiplication and Strassen's Algorithm
Aim: Multiply two matrices using conventional multiplication and Strassen's method for 2×2 matrices.
"""

def multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def strassen_2x2(a, b):
    a11, a12, a21, a22 = a[0][0], a[0][1], a[1][0], a[1][1]
    b11, b12, b21, b22 = b[0][0], b[0][1], b[1][0], b[1][1]
    m1 = (a11 + a22) * (b11 + b22)
    m2 = (a21 + a22) * b11
    m3 = a11 * (b12 - b22)
    m4 = a22 * (b21 - b11)
    m5 = (a11 + a12) * b22
    m6 = (a21 - a11) * (b11 + b12)
    m7 = (a12 - a22) * (b21 + b22)
    return [[m1 + m4 - m5 + m7, m3 + m5],
            [m2 + m4, m1 - m2 + m3 + m6]]

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(multiply(a, b))
print(strassen_2x2(a, b))
