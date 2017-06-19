# Programming challenge

- Write a Python program that takes the number 28 and prints out all of its factors.

  --- hints ---
  --- hint ---
  Create a loop that checks every number between 2 and 27 to see if it is a factor of 28. You will need to use the modulo (%) operator to check whether dividing 28 by a number leaves a remainder or not.

  --- /hint ---
  --- hint ---
  Here is some pseudo code which will help with the structure of your program:

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
  [Download the solution](resources/brute_force_factor.py).


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

  --- /hint ---

  --- /hints ---


- Alter your program so that it takes any number the user types in and outputs all of its factors.

  --- hints ---
  --- hint ---
  Use `input()` to allow the user to type a number in, and convert the input into an integer with `int()`.

  --- /hint ---

  --- hint ---
  [Download the solution](resources/brute_force_factor2.py).

  At the start of your program, change the value of the variable `public_key` to be an integer input from the user.

  ```python
  public_key = int(input("Enter a number: "))
  ```



- Experiment (with trial and error) to find the largest number can you give your program before it takes a very long time or crashes.

- Add a timer to benchmark how long your code takes to return the answer. Here is some [timer code](resources/timer_code.py), to time how long a loop takes to execute. Can you adapt this code to time how long your script takes to find the factors of a given number?

  --- hints ---
  --- hint ---
  Here is the timer code. Add the part from this code which starts the timer **before** your brute force factoring program, and put the code which ends the timer afterwards. Don't forget to start the timer _after_ you choose a number otherwise the time you spend choosing will be added on to the total time!

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

  --- /hint ---
  --- hint ---

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
  --- /hint ---
  --- /hints ---


- Run your code and time how long it takes to find the factors of 3-, 5- and 7-digit numbers.

- You could draw a graph to illustrate the relationship between the number of digits in the number and the length of time taken to find the factors.
