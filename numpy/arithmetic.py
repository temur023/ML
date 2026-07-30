import numpy as np

array = np.array([1.01,2.25,3.9])

#Scalar artithmetic

print(array + 1)
print(array - 2)
print(array * 2)
print(array / 2)
print(array ** 2)

#Vectorized math functions

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

#EXERCISE

radii = np.array([1,2,3])
print(np.pi*radii**2) #Area of a circle

#Element-wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

#Comparison operators
scores = np.array([91,55,100,73,82,64])
print(scores >= 60)

scores[scores < 60] = 0
print(scores)