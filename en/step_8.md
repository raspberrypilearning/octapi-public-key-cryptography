## Finding prime factors with a single Raspberry Pi

As you learnt earlier, finding the factors of a number becomes more difficult the larger the number is. In this step, you will look at running a program to find prime factors of the number `2396059349` using the processing power of a single Raspberry Pi.

The program that you will run in this section involves a function to test whether a number is prime. You are not expected to be able to write this code yourself, or to understand exactly how it works. However, the code is included in case you would like to investigate it more thoroughly. The 'main' part of the program begins on line 146 and should be accessible to people who have completed the previous parts of this resource. 

- To download the [code for a stand-alone Raspberry Pi](resources/factor_standalone.py), right-click the link. Save it onto your Raspberry Pi.

- Open Python 3 (IDLE).

[[[rpi-gui-idle-opening]]]

- Click `File` > `Open` in IDLE, then browse to the code that you just saved.

- Press `F5` to run the code.

- You will be asked for the semiprime number that you would like to factor. Enter the number `2396059349` and press `Enter`.

- You will be asked for the scale of the chunk size. Type in `1000` and press `Enter`. The search is done in 'chunks' (i.e. blocks of primes), where the size of the chunk is based on the number of digits in the semiprime, and the scale factor —  in this case, `1000`.

### Explanation
You will see the following results:

```python
Attempting factors in range 48949 - 70546, chunk size 21597
Attempting factors in range 70547 - 92144, chunk size 21597
90373 * 26513 = 2396059349
```

- The code contains a function that searches for a factor.
- We only want to test prime numbers, so a lot of the code is devoted to **primality tests**, which work out whether a number is prime or not.
 - The factor search starts at the **square root** of the public key. This is because the factors are likely to have a roughly similar number of digits as the square root. Remember that when you select prime numbers to use as private keys, it is important that each has roughly the same number of digits as the other. For example, if the two prime numbers chosen to make up a key were `15485863` and `17`, they would not share equal security strength.
- The program will take each chunk one at a time and search for a matching pair of prime factors.
- This search happens in chunks to mimic the way that the OctaPi will approach the problem when running the searches in parallel across several processors.
- When the two factors are found, the result is printed. In this case, the factors are `90373` and `26513`, which would be the private keys to the original semiprime public key `2396059349`.
