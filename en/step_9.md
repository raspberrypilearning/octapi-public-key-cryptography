## Finding prime factors with a single Raspberry Pi

As you already learned, finding the factors of a number becomes more difficult the larger the number is. Let's look at running a program to find prime factors of the number `2396059349` using the processing power of a single Raspberry Pi.

- Download the [code for a stand-alone Raspberry Pi](resources/factor_standalone.py) and save it onto your Raspberry Pi.

- Open a terminal and change to the directory where you saved the code using the `cd` command.

    ![Open a terminal](images/terminal.png)

- Run the code by typing the following command:

    ```bash
    python3 factor_standalone.py 2396059349 1000
    ```

### Explanation
We are running the Python code and passing it two pieces of data, the first being the number `2396059349` which is the public key we want to find the factors for.

The code contains a function which searches for a factor using the **square root** of the public key as the starting point. It does this because the factors are likely to have a roughly similar number of digits as the square root. Additionally, when selecting the primes to use as the private keys, it is important that each has roughly the same number of digits as the other. For example, if the two prime numbers chosen to make up a key were `15485863` and `17`, they would not share equal security strength.

The search is done in "chunks" (blocks of primes), where the size of the chunk is based on 1) the number of digits in the public key and 2) the scale factor, in this case the `1000` parameter we passed to the script when we ran it. The program will take each chunk one at a time and search for a matching pair of prime factors. This program searches in chunks to mimic the way the OctaPi will approach the problem when running the searches in parallel across several processors.
