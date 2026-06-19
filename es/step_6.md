## Finding factors

Remember that one of the criteria for a suitable public key is that it must be a number which is the product of two **prime** numbers. To put it another way, a public key has to be a number with only two **factors**, meaning dividing the number by any number besides the two factors will leave a remainder.

### Test your understanding

**If you were given the number 12 and asked to find out its factors, what strategy would you take?**

## \--- collapse \---

## title: Answer

Try to divide 12 by all the numbers between 2 and 11, and write down which ones it is divisible by. \--- /collapse \---

**Does the number 12 meet the criteria of only having two factors?**

## \--- collapse \---

## title: Answer

No. The number 12 can be **factorised** as 12 = 2 * 6 and 12 = 3 * 4. \--- /collapse \---

**Can you generalise your strategy for finding factors, so that if you were given the number `n` and asked to find out its factors, you could describe to someone how to do it?**

## \--- collapse \---

## title: Answer

You may generalise your previous rule as "Try to divide n by all the numbers between 2 and n-1, and write down which ones it is divisible by." In actual fact, you don't need to test up to n-1, you can stop at √n. Why not try [this activity](https://nrich.maths.org/7520) to learn about the Sieve of Eratosthenes to see why! \--- /collapse \---

How easy would it be to find the two **factors** using a computer program?

## Programming challenge

- Write a Python program that takes the number 28 and prints out all of its factors.
    
    \--- hints \--- \--- hint \--- Create a loop that checks every number between 2 and 27 to see if it is a factor of 28. You will need to use the modulo (%) operator to check whether dividing 28 by a number leaves a remainder or not.
    
    \--- /hint \--- \--- hint \--- Here is some pseudo code which will help with the structure of your program:
    
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
    
    \--- /hint \--- \--- hint \--- [Download the solution](resources/brute_force_factor.py).
    
    ```python
    public_key = 28
    
    # Store the discovered factors in this list
    factors = []
    
    # Begin testing at 2
    test_number = 2
    
    # Loop through all numbers from 2 up until the public_key number
    while test_number < public_key:
    
      # If the public key divides exactly into the test_number, it is a factor
      if public_key % test_number == 0:
          factors.append(test_number)
    
      # Move on to the next number
      test_number += 1
    
    # Print the result
    print(factors)
    ```
    
    \--- /hint \---
    
    \--- /hints \---

- Alter your program so that it takes any number the user types in and outputs all of its factors.
    
    \--- hints \--- \--- hint \--- Use `input()` to allow the user to type a number in, and convert the input into an integer with `int()`.
    
    \--- /hint \---
    
    \--- hint \--- [Download the solution](resources/brute_force_factor2.py).
    
    At the start of your program, change the value of the variable `public_key` to be an integer input from the user.
    
    ```python
    public_key = int(input("Enter a number: "))
    ```
    
    \--- /hint \--- \--- /hints \---

- Experiment (by trial and error) to find the largest number can you give your program before it takes a very long time or crashes.

- Add a timer to benchmark how long your code takes to return the answer. Here is some [timer code](resources/timer_code.py), to time how long a loop takes to execute. Can you adapt this code to time how long your script takes to find the factors of a given number?
    
    \--- hints \--- \--- hint \--- Here is the timer code. Add the part from this code which starts the timer **before** your brute force factoring program, and put the code which ends the timer afterwards. Don't forget to start the timer *after* you choose a number otherwise the time you spend choosing will be added on to the total time!
    
    [Download this code](resources/timer_code.py)
    
    ```python
    from time import time
    
    # Start the timer
    start = time()
    
    # Run some example code
    for i in range(1000):
        print("Heya")
    
    # Stop the timer
    end = time()
    total = end - start
    print( str(total) + " seconds" )
    
    ```
    
    \--- /hint \--- \--- hint \---
    
    ```python
    from time import time
    # Choose the number you wish to find the factors of
    
    # Start the timer
    start = time()
    
    # Paste in your brute force factoring code here
    
    # Stop the timer
    end = time()
    total = end - start
    print( str(total) + " seconds" )
    
    
    ```
    
    \--- /hint \--- \--- /hints \---

- Run your code and time how long it takes to find the factors of 3-, 5- and 7-digit numbers.

- You could draw a graph to illustrate the relationship between the number of digits in the number and the length of time taken to find the factors.