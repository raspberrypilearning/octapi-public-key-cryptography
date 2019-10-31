# How can a key be public?

When you use the Caesar Cipher, it is crucial that the key remains secret.

A public key cryptographic system consists of **public keys** and **private keys**. The public keys can be used in the encryption process, but the private keys are required to decrypt the data being exchanged.

The private keys need to be kept secret. If they are known by any external individual then the data can be decrypted.

Public key cryptography relies heavily on modular artihmetic, which you can read about below.

--- collapse ---
---
title: Modular Arithmetic
---
In computing, the modulo operation finds the remainder after division of one number by another number.

For instance:

```
15 mod 4 = 3
```

or written another way:

```
15 ÷ 4 = 3 remainder 3
```

You can see this using multiple subtractions:

```
15 - 4 = 11
11 - 4 = 7
 7 - 4 = 3
``` 

In python you can use the `%` operator to calculate modulo.

```python
15 % 4
3
>>>
```
--- /collapse ---

So how does adding a public key __improve__ security? If anyone can find out the public key, does this mean they can break the encryption?

There are many different algorithms for public key cryptography. The earliest known example is the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) which was developed in 1977, and released to the public. However, the same algorithm had actually already been developed by GCHQ mathemtaician [Clifford Cocks](https://en.wikipedia.org/wiki/Clifford_Cocks) in 1973, but his work was not declassified until 1997.

--- collapse ---
---
title: The RSA Cryptosystem
---
- Alice chooses three prime numbers. For example - `13`, `17` and `19`.
- She multiplies the two largest numbers together. `17 x 19 = 323`
- Her **public key** is now a combination of this product and the small prime number `323` `13`. She can share this with anyone.
- To get her private key, she subtracts `1` from her two large primes and then multiplies them together.

```
17 - 1 = 16
19 - 1 = 18
16 * 18 = 288
```

- Now Alice finds a number that when multiplied by the small prime and divided by this product, gives a remainder of `1`.

```
some_number * 13 ÷ 288 = some_other_number remainder 1
```

- In this case that number is `133`. This can be quickly calculated by a computer.

```
133 * 13 = 1729
1729 ÷ 288 = 6 remainder 1
```

- She now has her private key. It's `323 133`

- Alice sends her public key off over the internet, and Bob gets his copy.

- Bob wants to encrypt the letter `q` to send it to Alice. He converts it to a number first, using it's position in the alphabet - `17`

- Bob raises that number to the power of the second part of Alice's public key.

```
17 ** 13 = 9904578032905937
```

- Now he divides that number by the first part of Alice's public key, and works out the remainder.

```
9904578032905937 ÷ 323 = 30664328275250 remainder 187
```

- This number - `187` is now the ciphertext, that Bob can send to Alice.

- Alice receives the number `187`. She raises it to the power of the second part of her private key.

```
187 ** 133 = 142867573740720566967281881607100347295847400907671386091157121622780454369129479664615460769905626347535899931271341842520680048730294079130102722601895364310787622375946501020768888839654428347116807175403923673347503784689653101030237682797486439417148026581600192839120518456938618487878401112343947
```

- That's a big number. Now she calculates the remainder when that number is divided by the first part of her private key.

```
142867573740720566967281881607100347295847400907671386091157121622780454369129479664615460769905626347535899931271341842520680048730294079130102722601895364310787622375946501020768888839654428347116807175403923673347503784689653101030237682797486439417148026581600192839120518456938618487878401112343947

÷ 323 = 

442314469785512581539161245422235995778036566832043721231550219640260682060418642693079682615153948474292406207252865372224104020193042907357701452102267201984216551240583474414661674655052564333398394342775448312722776663559110370250126302215824888785001731815323491471101026301914858467798032580608

remainder 17
```

- Notice that remainder. It's `17`, which is the position of `q` in the alphabet. Alice has decrypted the ciphertext and has the plaintext that Bob sent her.

--- /collapse ---
