'''Removes the first occurrence of the value 3 
from the array and prints the result.'''
import array as arr

ls = [1, 2, 3, 4, 5, 6]

a = arr.array("i", ls)

#index
#0 1 2 3 .....
#1 2   3 4 5 6 Value of given array

a.remove(3)

print(*a)