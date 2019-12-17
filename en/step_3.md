# How can a key be public?

When you use the Caesar cipher, it is crucial that the key remains secret.

A public key cryptographic system consists of **public keys** and **private keys**. The public keys can be used in the encryption process, but the private keys are needed to decrypt the data being exchanged. This is called **asymmetric encryption**.

The private keys need to be kept secret. If they are known by any external individual, then the data can be decrypted.

Public key cryptography relies heavily on modular arithmetic, which you can read about below.

--- collapse ---
---
title: Modular arithmetic
---
In computing, the modulo operation finds the remainder after one number is divided by another number.

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

In Python, you can use the `%` operator to calculate modulo.

```python
15 % 4
3
>>>
```
--- /collapse ---

So how does adding a public key __improve__ security? If anyone can find out the public key, does this mean that they can break the encryption?

There are many different algorithms for public key cryptography. The earliest publicly known example is the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)){:target="_blank"}, which was developed in 1977. However, the same algorithm had actually already been suggested by GCHQ cryptographer [James Ellis](https://en.wikipedia.org/wiki/James_H._Ellis){:target="_blank"} and then been developed by GCHQ mathematician [Clifford Cocks](https://en.wikipedia.org/wiki/Clifford_Cocks){:target="_blank"} in 1973, but his work was not declassified until 1997.

--- collapse ---
---
title: The RSA cryptosystem
---
- Alice chooses three prime numbers, for example: `13`, `17`, and `19`.
- She multiplies the two largest numbers together: `17 x 19 = 323`
- Her **public key** is now a combination of this product `323` and the small prime number `13`. She can share this with anyone.
- To get her private key, she subtracts `1` from the two large primes and then multiplies them together.

```
17 - 1 = 16
19 - 1 = 18
16 * 18 = 288
```

- Alice's private key is `288`.

- Now, Alice finds a number that, when multiplied by the small prime and divided by this product, gives a remainder of `1`.

```
some_number * 13 ÷ 288 = some_other_number remainder 1
```

- In this case, that number is `133`. This can be quickly calculated by a computer.

```
133 * 13 = 1729
1729 ÷ 288 = 6 remainder 1
```

- She now has her private key. It's `323 133`.

- Alice sends her public key off over the internet, and Bob gets his copy.

- Bob wants to encrypt the letter `q` to send it to Alice. He converts it to a number first, using its position in the alphabet — `17`.

- Bob raises that number to the power of the second part of Alice's public key.

```
17 ** 13 = 9904578032905937
```

- Now, he divides that number by the first part of Alice's public key, and works out the remainder.

```
9904578032905937 ÷ 323 = 30664328275250 remainder 187
```

- This number, `187`, is now the ciphertext, which Bob can send to Alice.

- Alice receives the number `187`. She raises it to the power of the second part of her private key.

```
187 ** 133 = 142867573740720566967281881607100347295847400907671386091157121622780454369129479664615460769905626347535899931271341842520680048730294079130102722601895364310787622375946501020768888839654428347116807175403923673347503784689653101030237682797486439417148026581600192839120518456938618487878401112343947
```

- That's a big number! Now, she divides that number by the first part of her private key and calculates the remainder.

```
142867573740720566967281881607100347295847400907671386091157121622780454369129479664615460769905626347535899931271341842520680048730294079130102722601895364310787622375946501020768888839654428347116807175403923673347503784689653101030237682797486439417148026581600192839120518456938618487878401112343947

÷ 323 = 

442314469785512581539161245422235995778036566832043721231550219640260682060418642693079682615153948474292406207252865372224104020193042907357701452102267201984216551240583474414661674655052564333398394342775448312722776663559110370250126302215824888785001731815323491471101026301914858467798032580608

remainder 17
```

- Notice that remainder: it's `17`, which is the position of `q` in the alphabet. Alice has decrypted the ciphertext and has the plaintext that Bob sent her.

--- /collapse ---

Here is a simplified version of how public key (asymmetric) cryptography can work, using a system called the [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange){:target="_blank"}. Again, this system was actually first developed within GCHQ, by [Malcolm Williamson](https://en.wikipedia.org/wiki/Malcolm_J._Williamson), but it remained classified until 1997.

- Alice and Bob agree to use a public key cryptographic system. They decide on a public key which consists of two numbers: a large prime number `p` and another [smaller number](https://en.wikipedia.org/wiki/Primitive_root_modulo_n){:target="_blank"} `g`.

- `p` and `g` can be shared publicly. Alice can choose them and just send them to Bob without worrying about who can see them. An *eavesdropper*, Eve, could know these numbers, and still not be able to decrypt Alice's and Bob's conversations.

- Imagine that Alice and Bob agree that `p` is 23 and `g` is 5. In reality, `p` would be a much larger prime number, but to keep things simple, this example will involve smaller numbers.

- Alice and Bob now each choose a private key. This can be any integer. Alice chooses `4` and Bob chooses `3`. They both keep these numbers secret. Nobody but Alice knows that she has chosen `4`, and nobody but Bob knows that he has chosen `3`.

- Both Alice and Bob need to do a little maths now.

- Alice sends Bob `g`<sup>`4`</sup> `mod p`

```python
g**4 % p
5**4 % 23 = 4
```

- Bob sends Alice `g`<sup>`3`</sup> `mod p`

```python
g**3 % p
5**3 % 23 = 10
```

- Alice then works out the shared secret number using her private key: `10**4 % 23 = 18`

- Bob then also works out the shared secret number using his private key: `4**3 % 23 = 18`

- Both Alice and Bob have calculated a shared **secret number**, which they have worked out using the number that they were sent, and their own private keys.

- Alice and Bob have the shared secret `18`, and even though Eve knew the public keys, she can not work out this shared secret.

- The value `18` can now be used for the shift in a Caesar cipher or another, more secure, cryptographic technique, and Alice and Bob can communicate securely.

## Test your understanding

**Why is this an asymmetric encryption algorithm?**

--- collapse ---
---
title: Answer
---

Bob's and Alice's private keys are different. They can both generate a shared secret using their own private keys and the public keys.

--- /collapse ---


**Why don't Alice and Bob only use their private key?**

--- collapse ---
---
title: Answer
---

Alice's key and Bob's key are not the same. If Alice used her private key to encrypt the data without the existence of a shared public key, the data could not be ecrypted with Bob's private key. Bob needs both his private key and the public key to be able to decrypt the message.

--- /collapse ---
