import numpy as np
# PART 1

# Exercise 0 (1 point)
def sizeof_image(I):
    assert type(I) is np.ndarray
    assert len(I.shape) == 2
    shape = I.shape[0] * I.shape[1]
    return shape

# Exercise 1 (2 points)
def compress_image(I, k):
    Uk, S, VkT = np.linalg.svd(I)
    return S, Uk[:, :k], VkT[:k, :]

# Exercise 2 (2 points)
def sizeof_compressed_image(Sigma, Uk, VkT):
    size = ((k*len(Uk)) + k + (k*len(VkT.T)))*8
    return size

# Exercise 3 (2 points)
def compression_error (Sigma, k):
    """
    Given the singular values of a matrix, return the
    relative reconstruction error.
    """
    c_error = np.sqrt((sum(Sigma[k:]**2)) / (sum(Sigma**2)))
    return c_error

# Exercise 4 (2 points)
def uncompress_image(Sigma, Uk, VkT):
    assert Uk.shape[1] == VkT.shape[0]
    unc_img = np.dot(Uk[:, :k], np.dot(np.diag(Sigma[:k]), VkT[:k, :]))
    return unc_img

# Exercise 5 (3 points)
def find_rank(rel_err_target, Sigma):
    c = []
    for i in range(200):
        test =(compression_error(Sigma, i))
        if test >= rel_err_target:
            c.append(test)
            final = i+1
        else:
            continue
    return final
