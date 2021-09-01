import numpy as np

#list to array
lst = [1, 2, 3]
arr = np.array(lst)
print(arr,"\n")


#array of a range
print(np.arange(0,10), "\n")
print(np.arange(0,10,2), "\n")


#array of any number, "zeros can be replaced by ones, twos....."
print(np.zeros(5), "\n")
print(np.zeros((2,5)), "\n")


#linspace to get array evenly spaced arrays between 2 numbers
print(np.linspace(2,10,4), "\n")


#identity matrix using eye()
print(np.eye(5), "\n")

