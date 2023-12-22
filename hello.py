print("Hello from Binder!")


import numpy as np
# Define an array of numbers
foo = np.array([0,1,2,3,4,5])

# Define a function that squares numbers
def bar(x):
    return x*x

# Loop over each element and perform an action on it
for element in foo:
    # Print the result of bar
    print(bar(element))

# (Very) inefficient way to define a map function
def my_map(function, array):
    # create a container for the results
    output = []
    
    # loop over each element
    for element in array:
        # add the intermediate result to the container
        output.append(function(element))
        
    # return the now-filled container
    return output

my_map(bar,foo)


# NB: in Python3 `map` is a generator, so we need to cast it to a list for this comparison
list(map(bar,foo))


# Parallel Workers
# In the exampke we showed before, no step of the `map` call depend on other stpes
# Rather than waiting for the function to loop over each value, we could create multiple instances of the function `barz and apply
# it to each value simultaneously.
# This is achieved with the `multiprocessing` module and a pool of workers.
