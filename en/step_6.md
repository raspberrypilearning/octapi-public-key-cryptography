# Programming challenge

1. Write a Python program that takes the number 28 and prints out all of its factors.

--- hints ---
--- hint ---
Create a loop that checks every number between 2 and 27 to see if it is a factor of 28. You will need to use the modulo (%) operator to check whether dividing 28 by a number leaves a remainder or not.

--- /hint ---
--- hint ---

```Python
public_key = 28

# Store the discovered factors in a list

# Begin testing at 2
test_number = 2

# Loop through all numbers from 2 up until the one below the key you are testing
while test_number < public_key:

    # If the public key divides exactly into the test_number, it is a factor
    if :
        # Add this factor to the list

    # Move on to the next test number

```

--- /hint ---
--- hint ---
A solution can be found [here](resources/brute_force_factor.py).
--- /hint ---

--- /hints ---


1. Alter your program so that it takes any number the user types in and outputs all of its factors.

--- hints ---
--- hint ---
Use `input()` to allow the user to type a number in, and convert the input into an integer with `int()`.

--- /hint ---

--- hint ---
A solution can be found [here](resources/brute_force_factor2.py).
--- /hint ---

--- /hints ---



1. Experiment (with trial and error) to find the largest number can you give your program before it takes a very long time or crashes.

1. Add a timer to benchmark how long your code takes to return the answer. Here is some [timer code](resources/timer_code.py), to time how long a loop takes to execute. Can you adapt this code to time how long your script takes to find the factors of a given number?

--- hints ---
--- hint ---
Add the part from the [timer code](resources/timer_code.py) which starts the timer before your brute force factoring program, and put the code which ends the timer afterwards.

--- /hint ---
--- hint ---

```python
from time import time

# Start the timer
start = time()

# Paste in your brute force factoring code here

# Stop the timer
end = time()
total = end - start
print( str(total) + " seconds" )


```
--- /hint ---
--- /hints ---


1. Run your code and time how long it takes to find the factors of 3-, 5- and 7-digit numbers.
