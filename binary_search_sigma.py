import numpy as np

def binary_search_sigma(dist, target_entropy,lower_sigma = 1e-20, upper_sigma = 1000, max_iter = 1000, tol = 1e-10,):

  for _ in range(max_iter):
    guess_sigma = (lower_sigma + upper_sigma)/2
    entropy_calculated = calculate_entropy(dist, guess_sigma)
    
    if entropy_calculated < target_entropy:
      lower_sigma = guess_sigma
    elif entropy_calculated > target_entropy:
      upper_sigma = guess_sigma
    elif abs(entropy_calculated - target_entropy) <= tol:
      return guess_sigma
  return guess_sigma

def find_sigmas(pairwise_distances):
  sigmas = []
  for i in range(pairwise_distances.shape[0]):
    sigmas.append(binary_search_sigma(dist = pairwise_distances[i], 
                                      target_entropy = required_entropy))
  return np.array(sigmas)
