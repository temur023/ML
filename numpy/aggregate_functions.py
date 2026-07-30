import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) #position of the min value
print(np.argmax(array)) #position of the max value

print(np.sum(array,axis=1)) #axis=0 sum all the collumns, axis=1 sum all the rows