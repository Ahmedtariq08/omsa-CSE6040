import numpy as np

# ANCHOR PART 0

# SECTION Exercise 2 (5 points)
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


# SECTION Exercise 4
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

# ANCHOR PART 2
# SECTION Exercise 1
def linearize_colmajor(i, j, m, n):  # calculate `u`
    return i + j * m


def linearize_rowmajor(i, j, m, n):  # calculate `v`
    return i * n + j


# SECTION Exercise 3
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


# ANCHOR PART 3
def sparse_matrix(base_type=float):
    """Returns a sparse matrix using nested default dictionaries."""
    from collections import defaultdict
    return defaultdict(lambda: defaultdict (base_type))

def dense_vector(init, base_type=float):
    """
    Returns a dense vector, either of a given length
    and initialized to 0 values or using a given list
    of initial values.
    """
    # Case 1: `init` is a list of initial values for the vector entries
    if type(init) is list:
        initial_values = init
        return [base_type(x) for x in initial_values]
    
    # Else, case 2: `init` is a vector length.
    assert type(init) is int
    return [base_type(0)] * init

# SECTION Exercise 2
def spmv(A, x, num_rows=None):
    if num_rows is None:
        num_rows = max(A.keys()) + 1
    y = dense_vector(num_rows)
   
    # Recall: y = A*x is, conceptually,
    # for all i, y[i] == sum over all j of (A[i, j] * x[j])
    res = []
    for row_index in range(len(A) + 1):
        s = 0.0
        for col_index in range(len(A[row_index]) + 1):
            element = A[row_index][col_index]
            s += element * x[col_index]
        res.append(s)
   
    return res
    #return y


# SECTION Exercise 3
G = sparse_matrix()
for i in range(len(edges)):
    s = edges['Source'].iloc[i]
    t = edges['Target'].iloc[i]
    s_id = name2id[s]
    t_id = name2id[t]
    G[s_id][t_id] = 1.0


# SECTION Exercise 4
H = sparse_matrix()
for i in range(len(edges)):
    s = edges['Source'].iloc[i]
    t = edges['Target'].iloc[i]
    H[s][t] = 1.0


# SECTION Exercise 5
def spmv_keyed(A, x):
    """Performs a sparse matrix-vector multiply for keyed matrices and vectors."""
    assert type(x) is dict
    
    y = vector_keyed(keys=A.keys(), values=0.0)
    for i, row_i in A.items():
        s = 0.
        for j, a_ij in row_i.items():
            s += a_ij * x[j]
        y[i] = s
            
    return y

# SECTION Exercise 6
coo_rows = [name2id[s] for s in edges['Source']]
coo_cols = [name2id[t] for t in edges['Target']]
coo_vals = [1] * len(edges)

# SECTION Exercise 7
def spmv_coo(R, C, V, x, num_rows=None):
    """
    Returns y = A*x, where A has 'm' rows and is stored in
    COO format by the array triples, (R, C, V).
    """
    assert type(x) is list
    assert type(R) is list
    assert type(C) is list
    assert type(V) is list
    assert len(R) == len(C) == len(V)
    if num_rows is None:
        num_rows = max(R) + 1
    
    y = dense_vector(num_rows)
    
    for i, j, a_ij in zip(R,C,V):
        y[i] += a_ij * x[j]
    
    return y

# SECTION Exercise 8
def coo2csr(coo_rows, coo_cols, coo_vals):
    from operator import itemgetter
    C = sorted(zip(coo_rows, coo_cols, coo_vals), key=itemgetter(0))
    nnz = len(C)
    assert nnz >= 1

    csr_inds = [j for _, j, _ in C]
    csr_vals = [a_ij for _, _, a_ij in C]
    
    rows = max(coo_rows) + 1
    csr_ptrs = [0] * (rows + 1)

    for i in range(nnz):
        csr_ptrs[coo_rows[i] + 1]= csr_ptrs[coo_rows[i] + 1] +1
    for i in range(rows):
        csr_ptrs[i + 1] = csr_ptrs[i + 1] + csr_ptrs[i]
        #print("after: " , csr_row) # this helps the user follow along

    print(csr_ptrs[:10])
    
    return csr_ptrs, csr_inds, csr_vals

# SECTION Exercise 9
def spmv_csr(ptr, ind, val, x, num_rows=None):
    assert type(ptr) == list
    assert type(ind) == list
    assert type(val) == list
    assert type(x) == list
    if num_rows is None: num_rows = len(ptr) - 1
    assert len(ptr) >= (num_rows+1)  # Why?
    assert len(ind) >= ptr[num_rows]  # Why?
    assert len(val) >= ptr[num_rows]  # Why?
    
    y = dense_vector(num_rows)
    
    # convert csr to coo
    csr = ptr
    coo_rows = []
    for row_index, start_index in enumerate(csr):
        end_index = csr[row_index + 1] if row_index + 1 < len(csr) else len(csr) - 1
        for _ in range(end_index - start_index):
            coo_rows.append(row_index)
            
    # do sparse multiplication of coo
    y = spmv_coo(coo_rows, ind, val, x)
    
    return y
