import numpy as np
m = np.array([[1, 0, 1],
              [0, 2, 0]])

# Two students: Column 0 is Student A, Column 1 is Student B
v_batch = np.array([[5, 1],
                    [10, 1],
                    [3, 1]])

print("Batch Result:\n", m @ v_batch)











