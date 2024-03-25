import numpy as np
import scipy as sp

# ANCHOR - Part0
# Exercise 0 (2 points)
def linreg_fit(x, y):
    """Returns (alpha, beta) s.t. y ~ alpha*x + beta."""
    from numpy import ones
    m = len(x) ; assert len(y) == m
    u = ones(m)
    
    alpha = x.dot(y) - u.dot(x)*u.dot(y)/m
    alpha /= x.dot(x) - (u.dot(x)**2)/m
    beta = u.dot(y - alpha*x)/m

    return (alpha, beta)


# ANCHOR -Part 1
# Exercise 0 (1 points)
def f(x0, x1):
    return x0**2 + x1**2

# Exercise 1 (1 point)
def grad_f(x0, x1):
    return (2*x0, 2*x1)

# ANCHOR Part 2
# Exercise 1 (3 points)
def solve_neq(X, y):
    C = np.dot(np.transpose(X), X)
    b = np.dot(np.transpose(X), y)
    theta = sp.linalg.solve(C, b, assume_a='sym')
    return theta


# Exercise 2 (1 points)
def calc_residual_norm(X, y, theta):
    res = np.dot(X, theta) - y
    return np.sqrt(np.sum(res**2))

# Exercise 4 (2 points)
def random_mat (m, n, eps, start=0):
    return np.random.default_rng().uniform(start, eps, m*n).reshape((m, n))

# Exercise 5 (2 points)
def perturb_system(X, y, eps):
    return (X + random_mat(X.shape[0], X.shape[1], eps, -eps), y + random_mat(y.shape[0], y.shape[1], eps, -eps))

# Exercise 6 (1 point)
Q, R = np.linalg.qr(X)

# Exercise 7 (3 points)
def solve_qr(X, y):
    Q, R = np.linalg.qr(X)
    z = np.dot(np.transpose(Q), y)
    theta = sp.linalg.solve_triangular(R, z)
    return theta

# ANCHOR Part 4
# Exercise 1 (5 points)
PHI = 1.99 / LAMBDA_MAX # Fudge factor
rel_diffs = np.zeros((m+1, 1))

theta_k = np.zeros((n+1))
print(theta_k)
theta0 = 0
theta1 = 0
for k in range(m):
    rel_diffs[k] = rel_diff(theta_k, theta_true)
    
    xk = X[k]
    yk = y[k]
    
    res = np.dot(xk, yk - np.dot(xk, theta0))
    delta_k = np.dot(PHI, res)
    theta0 = theta1
    theta1 = theta1 + delta_k

print(theta0, theta1)
theta_k[0] = theta0
theta_k[1] = theta1
theta_lms = theta_k
rel_diffs[m] = rel_diff(theta_lms, theta_true)
