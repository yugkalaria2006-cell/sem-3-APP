# write a program in python to demonstrate basic threading using start and join methods
import threading
import time

def task(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))
t1.start()
t1.join()
t2.start()
t2.join()
print("Task is completed")