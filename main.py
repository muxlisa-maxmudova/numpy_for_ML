import numpy as np
# Shuffling the array
rng = np.random.default_rng()
fruits = np.array(["apple", "orange", "coconut", "pineapple"])
fruit = rng.choice(fruits, size = (2,2))
print(fruit)














