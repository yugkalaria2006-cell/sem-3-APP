import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s-%(message)s")

def add(a,b):
    logging.info("Function Called sucessfully!")
    result = a+b
    logging.info("Execution completed Sucessfully!")
    return result

x = add(10,29)
print("Result" , x)