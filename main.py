import numpy as np
# Operations on multidimensional array:
array = np.array([[["A", "B", "C"],["D", "E", "F"], ["G", "H", "I"]],
                  [["J", "K", "L"],["M", "N", "O"], ["P", "Q", "R"]],
                  [["S", "T", "U"],["V", "W", "X"], ["Y", "Z", ""]]])
print(array[0][0][0]) # chain indexing - regular
