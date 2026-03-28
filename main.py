import numpy as np
# Slicing

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]

print(array[:2, 2:]) #first 2 rows and 2 last columns