# How can a key be public?

When you use the Caesar Cipher, it is crucial that the key remains secret. A public key cryptographic system consists of a **public key** and a matched but non-identical pair of **private keys**. The private keys are known only to the participants, and each participant holds one of them. The public key is created using the matched pair of private keys, and can be known by anyone.

So how does adding a public key **improve** security? If anyone can find out the public key, does this mean they can break the encryption?

Here's how it works:

- Alice and Bob agree to use a public key cryptographic system and generate one private key each (A and B), as well as a public key (AB) which is created by multiplying A and B (A * B).
- Bob sends Alice the public key AB.
- Alice receives the public key AB, and she knows this public key corresponds to her private key A. Alice encrypts her message with her private key A and sends it to Bob.
- Bob receives Alice's encrypted message. He has the public key AB and his private key B. Bob knows that AB = A * B, so he can work out A (by calculating A = AB / B) and decrypt the message from Alice.

### Test your understanding

**Why is this an asymmetric encryption algorithm?**

## \--- collapse \----

## title: Answer

Bob's and Alice's private keys are different. The private key used to perform the encryption is not the same as the private key held by the person decrypting the information.

\--- /collapse \---

**Why don't Alice and Bob only use their private key?**

## \--- collapse \----

## title: Answer

Alice's key and Bob's key are not the same. If Alice used her private key to encrypt the data without the existence of a shared public key, it would not be unlockable by Bob's private key. Bob needs both his key and the public key to be able to decrypt the message.

\--- /collapse \---

**Why is the public key even needed?**

## \--- collapse \----

## title: Answer

Alice encrypts the message with her private key to prove she is the sender. Bob reads the message using his private key, which is the only way of decrypting the message, thus proving he is the intended recipient. This proof of identity, also called authentication, is only possible with the addition of a shared public key.

\--- /collapse \---