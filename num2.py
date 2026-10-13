'''Removes value 3 from an array, prints a Unicode 
string, and prints the updated array.'''
import array as arr

ls = [1,2,3,4,5,6]

a = arr.array("i",ls)

#index
#0 1 2 3 .....
#1 2   3 4 5 6 Value of given array

a.remove(3)

b = "\u092D\u093E\u0930\u0924"
print(b)
print(*a)