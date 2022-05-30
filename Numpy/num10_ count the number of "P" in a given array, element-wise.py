#Write a NumPy program to count the number of "P" in a given array, element-wise.

import numpy as np
x1 = np.array(['Python', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("Number of ‘P’:")
r = np.char.count(x1, "P")
print(r)
