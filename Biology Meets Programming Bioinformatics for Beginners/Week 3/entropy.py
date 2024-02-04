import numpy as np

a = [0.0, 0.0, 0.0, 1]

entropy = 0
for i in a:
    if i != 0:
        entropy += -i * (np.log2(i))

print(entropy)
