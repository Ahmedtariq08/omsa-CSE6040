import numpy as np

# Exercise 1 (2 points)
def init_centers(X, k):
    """
    Randomly samples k observations from X as centers.
    Returns these centers as a (k x d) numpy array.
    """
    centers_matrix = X[np.random.choice(len(X), k, replace=False)]
    return centers_matrix

# Exercise 2 (3 points)
def compute_d2(X, centers):
    m = len(X)
    k = len(centers)
    
    S = np.empty((m, k))   
    #
    # YOUR CODE HERE
    
    # using the distance formula 
    for n in range(k):
        mu = centers[n:n+1, :]
        sq_diff = (X - mu)**2
        S[:, n:n+1] = np.sqrt(sq_diff[:,:1] + sq_diff[:, 1:2])**2
    
    # Answer provided
    #     for i in range(m):
    #         S[i,:] = np.linalg.norm(X[i,:] - centers, ord=2, axis=1)

    return S

# Exercise 3 (2 points)
def assign_cluster_labels(S):
    labels = np.argmin(S, axis=1)
    return np.array(labels)

# Exercise 4 (2 points)
def update_centers(X, y):
    # X[:m, :d] == m points, each of dimension d
    # y[:m] == cluster labels
    m, d = X.shape
    k = max(y) + 1
    assert m == len(y)
    assert (min(y) >= 0)
    
    centers = np.empty((int(k), int(d)))
    for j in range(int(k)):
        # Compute the new center of cluster j,
        # i.e., centers[j, :d].
        ###
        ### YOUR CODE HERE
        ###
        centers[j,:] = np.mean(X[y==j, :], axis=0)
    return centers

# Exercise 5 (2 points)
def WCSS(S):
    return sum(np.amin(S, axis=1))

# Exercise 6 (2 points)
def kmeans(X, k,
           starting_centers=None,
           max_steps=np.inf):
    if starting_centers is None:
        centers = init_centers(X, k)
    else:
        centers = starting_centers
        
    converged = False
    labels = np.zeros(len(X))
    i = 1
    while (not converged) and (i <= max_steps):
        old_centers = centers
        ###
        ### YOUR CODE HERE
        ###
        S = compute_d2(X, old_centers)
        labels[:] = assign_cluster_labels(S)  # check
        centers = update_centers(X, labels)
        converged = has_converged(old_centers, centers)
        
        print ("iteration", i, "WCSS = ", WCSS (S))
        i += 1
    return labels

# Exercise 7 (1 point)
r, c, l = img_arr.shape
img_reshaped = np.reshape(img_arr, (r*c, l), order="C")

# Exercise 8 (1 point)
labels = kmeans(img_reshaped, 3)

# Exercise 9 (2 points)
ind = np.column_stack((img_reshaped, labels))
centers = {}
for i in set(labels):
    c = ind[ind[:,3] == i].mean(axis=0)
    centers[i] = c[:3]

