# main.py
import pandas as pd
import time
from rich.console import Console
import time

# Your DoSolve function
def DoSolve():
    # Record the initial time
    initialtime = time.time()
    
    # Wait for user input (assumed to be Enter key)
    input()
    
    # Record the final time
    endtime = time.time()
    
    # Calculate the time taken for the solve
    return (endtime - initialtime)

# Using timeit to measure the execution time
#time_taken = timeit.timeit(DoSolve, number=1)

# Printing the result
#print(f"Solve time: {time_taken:.3f} seconds")
