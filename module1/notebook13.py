import numpy as np

# Exercise 0 (2 points)
def lin_discr (X, theta):
    y = X.dot(theta)
    return y

# Exercise 1 (2 points)
def heaviside(Y):
    def classify(yi):
        if yi > 0:
            return 1
        else:
            return 0
    np_classify = np.frompyfunc(classify, 1, 1)    
    return np_classify(Y)

# Exercise 3 (2 points)
def logistic(Y):
    def sigmoid(yi):
        from math import exp
        sig = 1 / (1 + exp(-yi))
        return sig
        
    logistic_values = np.vectorize(sigmoid)
    
    return logistic_values(Y)

# Exercise 6 (2 points)
def log_likelihood(theta, y, X):
    u = np.ones(len(y)).T   # Let u be the constant vector of ones. 
    
    def log_of_element(x):
        return np.log(x)
    
    log_of_matrix = np.frompyfunc(log_of_element, 1, 1)
    ln_G = log_of_matrix(logistic(-X.dot(theta)))
    
    likelihood = y.T.dot(X).dot(theta) + u.dot(ln_G)
    return likelihood

# Exercise 8 (2 points)
def grad_log_likelihood(theta, y, X):
    """Returns the gradient of the log-likelihood."""
    gradient = X.T.dot(y - logistic(X.dot(theta)))
    return gradient

# Exercise 9 (4 points)
    ###
    ### YOUR CODE HERE
    ###
    gradient = grad_log_likelihood(thetas[:, t:t+1], y, X)
    step_t = ALPHA * gradient
    thetas[:, t+1:t+2] = thetas[:, t:t+1] + step_t
