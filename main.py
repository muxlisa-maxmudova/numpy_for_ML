import numpy as np
# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

scores[scores<60] = 0
scores[scores>60] = 1
print(scores)
