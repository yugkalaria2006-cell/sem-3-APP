import gc
class Student:
    def __init__(self,name):
        self.name = name
        self.friend = None
gc.disable()
s1= Student("Amit")
s2= Student("Rahul")
s1.friend = s2
s2.friend = s1
print("Circular refences created")
del s1
del s2
print("student references delete")
gc.enable()
collected = gc.collect()
print("Object collected :",collected)