# How can a key be public?

When you use the Caesar Cipher, it is crucial that the key remains secret. A public key cryptographic system consists of a **public key** and a matched but non-identical pair of **private keys**. The private keys are known only to the participants, and each participant holds one of them. The public key is created using the matched pair of private keys, and can be known by anyone.

So how does adding a public key __improve__ security? If anyone can find out the public key, does this mean they can break the encryption?

Here's how it works:

- Alice and Bob agree to use a public key cryptographic system. They decide on a public key which consits of two numbers; a large prime number `p` and another number `g` which is [calculated using `p`](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)

--- collapse ---
---
title: How to calculate `g`
---

--- /collapse ---

- `p` and `g` can be shared publicly. A *bad actor* Eve, could know these numbers, and still not be able to decrypt Alice's and Bob's conversations.
- Let's say that Alice and Bob agree that `p` is 23 and `g` is 5. In reality `p` would be a much larger prime number, but to keep things simple, we'll work with smaller numbers.
- Alice and Bob now each choose a private key. This can be any integer. Alice chooses `4` and Bob chooses `3`. They both keep these numbers secret. Nobody but Alice knows she has choosen `4`, and nobody but Bob knows that he has chosen `3`.
- Both Alice and Bob need to do a little maths now.

--- collapse ---
---
title: Modulo operation
---
In computing, the modulo operation finds the remainder after division of one number by another number.
For instance:

`15 mod 4 = 3`

or written another way:

`15 ÷ 4 = 3 remainder 3`

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

- Alice sends Bob `5**4 % 23 = 4`
- Bob sends Alice `5**3 % 23 = 10`
- Alice then works out the shared secret number = `10**4 % 23 = 18`
- Bob then also works out the shared secret number = `4**3 % 23 = 18`
- Now Alice and Bob have the shared secret `18`, and even though Eve knew the public keys, she can not work out this shared secret.
- The value 18, can now be used for the shift in a Caesar Cypher, and Alice and Bob can communicate securely.


### Test your understanding

**Why is this an asymmetric encryption algorithm?**


--- collapse ----
---
title: Answer
---

Bob's and Alice's private keys are different. They can both generate a shared secret using their own private keys and the pubic keys,

--- /collapse ---

**Why don't Alice and Bob only use their private key?**


--- collapse ----
---
title: Answer
---

Alice's key and Bob's key are not the same. If Alice used her private key to encrypt the data without the existence of a shared public key, it would not be unlockable by Bob's private key. Bob needs both his key and the public key to be able to decrypt the message.

--- /collapse ---

**Why is the public key even needed?**


--- collapse ----
---
title: Answer
---
Alice encrypts the message with her private key to prove she is the sender. Bob reads the message using his private key, which is the only way of decrypting the message, thus proving he is the intended recipient. This proof of identity, also called authentication, is only possible with the addition of a shared public key.

--- /collapse ---
