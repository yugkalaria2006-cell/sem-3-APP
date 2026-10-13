# Combines two 1D lists into a 2D NumPy array matrix and prints it.
import numpy as np
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#value of given array
ls1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]#value of given array

arr_2d = np.array([ls, ls1])
print(arr_2d)