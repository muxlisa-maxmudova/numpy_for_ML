import numpy as np
# Operations on multidimensional array:
array = np.array([[["A", "B", "C"],["D", "E", "F"], ["G", "H", "I"]],
                  [["J", "K", "L"],["M", "N", "O"], ["P", "Q", "R"]],
                  [["S", "T", "U"],["V", "W", "X"], ["Y", "Z", ""]]])
word = array[0,2,1] + array[0,0,0] + array[2,0,0] + array[0,0,0] + array[1,1,1]

print(word)