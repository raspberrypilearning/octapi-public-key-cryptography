## Finding prime factors with a single Raspberry Pi

As you already learned, finding the factors of a number becomes more difficult the larger the number is. Let's look at running a program to find prime factors of the number `2396059349` using the processing power of a single Raspberry Pi.

1. Download the [code for a stand-alone Raspberry Pi](resources/factor_standalone.py) and save it onto your Raspberry Pi.

1. Open a terminal and change to the directory where you saved the code using the `cd` command.

    ![Open a terminal](images/terminal.png)

1. Run the code by typing the following command:

    ```bash
    python3 factor_standalone.py 2396059349 1000
    ```

### Explanation
We are running the Python code and passing it two pieces of data, the first being the number `2396059349` which is the public key we want to find the factors for.

The code contains a function which searches for a factor using the **square root** of the public key as the starting point. This is a good starting point because when selecting the primes to use as the private keys, they each should have roughly the same number of digits. As an example, if the two prime numbers chosen to make up a key were `15485863` and `17`, this would mean that the security strength would not be shared equally amongst them.

The search is done in "chunks" (blocks of primes), where the size of the chunk is based on 1) the number of digits in the public key and 2) the scale factor, which was the `1000` parameter we passed to the script when we ran it. The program will take each chunk one at a time and search for a matching pair of prime factors. This program searches in chunks to mimic the way the OctaPi will approach the problem when running the searches in parallel across several processors.
