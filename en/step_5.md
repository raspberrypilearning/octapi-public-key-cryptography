## How are public and private keys chosen?

**Public and private keys** are generated in different ways, depending on the  cryptographic system being used. But here we can focus on one of the earliest and simplest forms of **public key** cryptography, called RSA.

A **public key** is actually two numbers. Here's how you can generate one:

- Randomly pick three prime numbers, that couldn't be predicted.
- The prime numbers should be large numbers, with lots of digits.
- The first part of the **public key**  is simply the product of the two larger prime numbers.
- The second part of the **public key** is the third and smaller prime.

We can see how this works in practice as follows:

Suppose we ignore the requirement for the **public key** to be a large number for now and use small randomly chosen **prime** numbers, A=7 and B=11 and C=13. This makes the first part of the **public key** BC = 11 * 13 = 143.
The second part of the **public key** is just A, so in this case 7.
So the **public key** in it's entirety is 143, 7

It's really easy to work out that 11 * 13 is 143, but not so easy to work out which two prime numbers were used to make 143. In fact the only real way to do this, is to keep trying to multiply prime numbers until you reach 143.

Working out the private key is trickier. It uses a little more complicated maths on the prime numbers to calculate. In this case, the private key ends up being 143, 103. If you'd like to know how this was generated then have a look at the section below.

[[[generic-python-generate-encryption-keys]]]

Now imagine an attacker intercepts the message sent from Bob to Alice. The attacker can find out that the **public key** was `143, 7`, as it was never sent securely, but the attacker needs to know the private key to decrypt the message.

To do this the attacker will need to know which two prime numbers when multiplied together make `143`

```
143 = A * B
```

Because we have chosen small primes A=11 and B=13, in this example, it is very easy for the attacker to figure out what the **private key** would be. All they have to do is multiply all possible values of `A` and `B` and see which multiplication results in the value `143`. In this example, the attacker could probably even do it in their head!

However, if the primes were a larger number, it would be considerably more difficult to work out the **factors**. Essentially, this is what protects the message: a hard maths problem.

## Example: Encrypting and Decrypting with public and private keys

The encryption and decryption process with the public and private keys is not too complicated, and seems a little like magic.

Bob has Alice's' public key, and wants to send her a simple message. To make this ultra-simple we will say that all he wants to send is the letter f.

The first thing that Bob needs to do is to turn the letter into a number. You can use the Caesar Cipher method here, and just choose it's position in the alphabet - `6`

### Encrypt the number with the public key
- Take the number, and raise it to the power of the second part of the public key:
  ```python
  >>> 6 ** 7
  279936
  ```
- Now divide that by the first part of the public key, and work out the remainder:
```python
>>> 279936 % 143
85
```
- This number `85` is the one that Bob can send to Alice. It is important to note that it is impossible to get back to the number `6` from the number `85`, unless you know the two prime numbers that are factors of `143`

### Decrypt the number with the private key
- Alice receives the number `85`. She takes the number and raises it to the power of the second part of her private key:
```python
>>> 85 ** 103
5372165068090451358552095536898291599950869914462659379988337267350319478836832523349419260025144388487669389299833468374609344756454803518067078607594789130437462620903943388839252293109893798828125
```
- Now that's a huge number. Alice now just needs to divide by the first part of her private key and find the remainder:
```python
>>> 5372165068090451358552095536898291599950869914462659379988337267350319478836832523349419260025144388487669389299833468374609344756454803518067078607594789130437462620903943388839252293109893798828125 % 143
6
```

- Now Alice has the number `6`, which is the position of `f` in the alphabet. She has successfully decrypted the message.
