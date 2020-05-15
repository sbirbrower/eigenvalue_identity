#! /usr/bin/env python3

import numpy as np

def matrix_minors (matrix):
    return [np.delete((np.delete(my_matrix, i, axis=0)), i, axis=1) for i in range(matrix.shape[0])]
   
def check_Hermitian (matrix):
    return np.allclose(matrix, np.conj(matrix).T)

def numpy_eigvectors (matrix):
    _, eigenvectors = np.linalg.eig(matrix)
    normalized_eig = eigenvectors / np.sqrt(np.sum(eigenvectors ** 2))
    normalized_eig = np.abs(normalized_eig)
    return normalized_eig.T

# from https://arxiv.org/pdf/1908.03795.pdf
def eigvectors_from_eigvalues (matrix):
    if check_Hermitian(matrix) == False:
        print ("Not a Hermitian matrix")
        return
    eigenvalues, _ = np.linalg.eig(matrix)
    minors = matrix_minors(matrix)
    minor_eigvalues, _ = np.linalg.eig(minors)

    eigenvectors = []
    for eigenval in eigenvalues:
        vector = []
        denominator = 1
        for i in range(len(minor_eigvalues)):
            denominator = np.prod([eigenval - eigenvalues[k] for k in range(len(eigenvalues)) if eigenvalues[k] != eigenval])
            numerator = 1
            for j in range(len(minor_eigvalues[i])):
                numerator = numerator * (eigenval - minor_eigvalues[i][j])
            vector.append(numerator / denominator)
        eigenvectors.append(vector)

    eigenvectors = np.array(eigenvectors)
    eigenvectors[np.abs(eigenvectors) < 0.000000001] = 0   
    return np.real(np.sqrt(eigenvectors) / np.sqrt(np.sum((np.sqrt(eigenvectors)) ** 2)))



my_matrix = np.array([[1, 1, -1],[1, 3, 1],[-1, 1, 3]])

np.allclose(numpy_eigvectors(my_matrix), eigvectors_from_eigvalues(my_matrix))



