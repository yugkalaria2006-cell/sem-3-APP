'''write a program in python to find and display 
the number of cpu cores available on the system'''
import multiprocessing

cores = multiprocessing.cpu_count()

print("Number of cores in cpu are", cores)