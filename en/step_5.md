## How are public and private keys chosen?

**Public and private keys** are generated in different ways, using different cryptographic systems. But here we can focus on one of the earliest and simplest forms of **public key** cryptography.

A **public key** is actually two numbers. Here's how you can generate one:

- Randomly pick three prime numbers, that couldn't be predicted.
- The prime numbers should be large numbers, with lots of digits.
- The first part of the **public key**  is simply the product of the two larger prime numbers.
- The second part of the **public key** is the third and smaller prime.

We can see how this works in practice as follows:

Suppose we ignore the requirement for the **public key** to be a large number for now and use small randomly chosen **prime** numbers, A=7 and B=11 and C=13. This makes the first part of the **public key** BC = 11 * 13 = 143.
The second part of the **public key** is just A, so in this case 7.
So the **public key** in it's entirity is 143, 7

It's really easy to work out that 11 * 13 is 143, but not so easy to work out which two prime numbers are.

Working out the private key is a little more complicated. It uses a little more complicated maths on the prime numbers to calculate. In this case, the private key ends up being 143, 103. If you'd like to know how this was generated then have a look at the section below.

[[[generic-python-generate-encryption-keys]]]

Now imagine an attacker intercepts the message sent from Bob to Alice. The attacker can find out that the **public key** was `143, 7`, as it was never sent securely, but the attacker needs to know the private key to decrypt the message.

To do this the attacker will need to know which two prime numbers when multiplied together make `143`

```
143 = A * B
```

Because we have chosen small primes A=11 and B=13, in this example, it is very easy for the attacker to figure out what the **private key** would be. All they have to do is multiply all possible values of `A` and `B` and see which multiplication results in the value `143`. In this example, the attacker could probably even do it in their head!

However, if the primes were a larger number, it would be considerably more difficult to work out the **factors**. Essentially, this is what protects the message: a hard maths problem.

## Example: Encrypting and Decrypting with public and private keys

The encryption and decryption process with the public and private keys is not too complicated.

Bob has Alices' public key, and wants to send her a simple message - "Hello".

The first thing that Bob needs to do is to turn the string `"Hello"` into an integer.

```python
import binascii
message = b"Hello"
x = binascii.hexlify(message)
int(x, 16)
```

This gives a value of 

