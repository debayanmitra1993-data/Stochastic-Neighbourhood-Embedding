import numpy as np
import scipy

def calculate_conditional_probabilities(pairwise_distances, sigmas):
  conditional_probabilities = np.zeros((pairwise_distances.shape[0], pairwise_distances.shape[0]))
  for i in tqdm_notebook(range(len(pairwise_distances))):
    conditional_probabilities[i] = scipy.special.softmax(-pairwise_distances[i]/(2*sigmas[i]*sigmas[i]))
  return conditional_probabilities
