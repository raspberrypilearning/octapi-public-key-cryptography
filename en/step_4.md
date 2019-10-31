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
