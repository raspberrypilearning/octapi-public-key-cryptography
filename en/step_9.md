## Finding prime factors with a single Raspberry Pi

As you already learned, finding the factors of a number becomes more difficult the larger the number is. Let's look at running a program to find prime factors of the number `2396059349` using the processing power of a single Raspberry Pi.

The program you will run in this section involves some code to test a number to see whether it is prime, which we would not necessarily expect you to be able to write yourself. However, there is a full explanation of how the code works and it is fully commented if you would like to investigate how it works more thoroughly.

- Download the [code for a stand-alone Raspberry Pi](resources/factor_standalone.py) by right clicking the link. Save it onto your Raspberry Pi.

- Open Python 3 (IDLE)

    [[[rpi-gui-idle-opening]]]

- Click `File` > `Open` in IDLE, then browse to the code you just saved

- Press `F5` to run the code

- You will be asked for the semi-prime number you would like to factor. Enter the number `2396059349` and press `Enter`.

- You will be asked for the scale of the chunk size. Type in `1000` and press `Enter`. The search is done in "chunks" (blocks of primes), where the size of the chunk is based on 1) the number of digits in the semi-prime and 2) the scale factor, in this case `1000`.

### Explanation
You will see the following results:

```
Attempting factors in range 48949 - 70546, chunk size 21597
Attempting factors in range 70547 - 92144, chunk size 21597
90373 * 26513 = 2396059349
```

    - The code contains a function which searches for a factor.
    - We only want to test prime numbers, so a lot of the code is devoted to **primality tests**, which test whether a number is prime or not.
    - The search starts at the **square root** of the public key. It does this because the factors are likely to have a roughly similar number of digits as the square root. Remember that when selecting the primes to use as the private keys, it is important that each has roughly the same number of digits as the other. For example, if the two prime numbers chosen to make up a key were `15485863` and `17`, they would not share equal security strength.
    - The program will take each chunk one at a time and search for a matching pair of prime factors.
    - This program searches in chunks to mimic the way the OctaPi will approach the problem when running the searches in parallel across several processors.
    - When the two factors are found, the result is printed. In this case the factors are `90373` and `26513` which would be the private keys, and the original semi-prime `2396059349` was the public key.
