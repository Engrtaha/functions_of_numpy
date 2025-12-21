import numpy as np
array = np.array([1,3,2,9,8,7,4,6,5])
array1 = np.random.normal(20,10,[3,4])
array.sort()
array1.sort(axis=0)
print(array)
print(array1)
