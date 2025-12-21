import numpy as np
array = np.arange(20).reshape(5,4)
array1 = np.split(array,[1,3])
array2 = np.hsplit(array,4)
array3 = np.vsplit(array,5)
print(array)
print(array1)
print(array2)
print(array3)