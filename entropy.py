import numpy as np
import scipy

def calculate_entropy(distances,sigma):
  p_conds = scipy.special.softmax(-np.array(distances)/(2*sigma*sigma))
  entropy = 0
  for i in range(len(p_conds)):
    entropy += (p_conds[i]*np.log2(p_conds[i]))
  return -entropy
