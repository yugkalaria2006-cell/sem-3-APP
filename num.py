'''Inserts the integer 10 at index 2
of the array and prints all elements.'''
import array as arr

ls = [1, 2, 3, 4, 5, 6]

a = arr.array("i", ls)

#index
#0 1 2 3 .....
#1 2   3 4 5 6 Value of given array

a.insert(2,10)

print(*a)