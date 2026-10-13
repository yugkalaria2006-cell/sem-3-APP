from memory_profiler import profile
@profile
def memory_test():
    data = [i for i in range(100000)]
    square = [i * i for i in data]
    del data
    return square

if __name__ == "__main__":
    result = memory_test()
    print("number of elements :",len(result))