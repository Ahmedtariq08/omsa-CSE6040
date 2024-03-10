# Exercise 2 (5 oints
import numpy as np

Z = np.array([[0, 1, 2, 3, 4, 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]])

# Construct `Z_green`, `Z_red`, `Z_orange`, and `Z_cyan`:
Z_red = [Z[i, 2] for i in range(len(Z))]
Z_orange = Z[0][3:5]
Z_cyan = [c[4:] for c in Z[4:]]
Z_green = [Z[i][::2] for i in range(len(Z)) if i in [2, 4]]

# Exercise 3
x = [13, 4, 15, 6, 4, 15, 12, 13, 19, 7, 16, 6, 11, 11, 4]
mask_mult_3 = [True if k % 3 == 0 else False for k in x]


# Exercise 4

def sieve(n):
    """
    Returns the prime number 'sieve' shown above.

    That is, this function returns an array `X[0:n+1]`
    such that `X[i]` is true if and only if `i` is prime.
    """
    is_prime = np.empty(n + 1, dtype=bool)  # the "sieve"

    # Initial values
    is_prime[0:2] = False  # {0, 1} are _not_ considered prime
    is_prime[2:] = True  # All other values might be prime

    # Implement the sieving loop
    for i in range(2, n + 1):
        arr = range(2, i)
        is_prime[i] = True
        for val in arr:
            if i % val == 0:
                is_prime[i] = False

    return is_prime


# print("==> Primes through 20:\n", np.nonzero(sieve(20))[0])

# ART 2

# Exercise 1
def linearize_colmajor(i, j, m, n):  # calculate `u`
    return i + j * m


def linearize_rowmajor(i, j, m, n):  # calculate `v`
    return i * n + j


# Exercise 3
def matvec_py(m, n, A, x):
    res = []
    for i in range(m):
        s = 0.0
        for j in range(n):
            element = A[linearize_colmajor(i, j, m, n)]
            s += element * x[j]
        res.append(s)

    return res
    # return [sum([A[linearize_colmajor(i, j, m, n)] * x[j] for j in range(n)]) for i in range(m)]


A = [[1, 0, -2],
     [3, 4, 0]]
AC = [1.0, 3.0, 0.0, 4.0, -2.0, 0.0]
X = [1, 0, -2]

print(matvec_py(2, 3, AC, X))
