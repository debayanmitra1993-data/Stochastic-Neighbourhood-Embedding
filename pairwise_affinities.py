import numpy as np

def calculate_pairwise_distances_squared(X):
  pairwise_distances_squared = np.zeros((X.shape[0], X.shape[0]))
  for i in range(X.shape[0] - 1):
    for j in range(i + 1, X.shape[0]):
      pairwise_distances_squared[i,j] = round(np.linalg.norm(X[i] - X[j])**2,2)
      pairwise_distances_squared[j,i] = pairwise_distances_squared[i,j]
  return pairwise_distances_squared
