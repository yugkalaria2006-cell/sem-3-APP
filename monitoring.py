import tracemalloc
tracemalloc.start()
data = []
for i in range(1000000):
    data.append(i)
current, peak = tracemalloc.get_traced_memory()
print(f"Current :{current/1024: .2f} KB")
print(f"Peak :{peak/1024: .2f} KB")
tracemalloc.stop()