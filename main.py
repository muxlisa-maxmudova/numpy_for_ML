import numpy as np
# Random numbers

rng = np.random.default_rng(seed = 1) # same numbers appear everytime
print(rng.integers(low =1, high = 101, size = (3, 2))) # high (second number) is exclusive so we generate numbers 1, 2, 3, 4, 5 and 6














