import sys
a =10
b = "Python Programming"
c= [1,2,3,4,5]
d = {"name":"Amit","age":25}
#bytes
print(f"Integer Size :{sys.getsizeof(a)}")
print(f"String :{sys.getsizeof(b)}")
print(f"List: {sys.getsizeof(c)}")
print(f"Dictory: {sys.getsizeof(d)}")