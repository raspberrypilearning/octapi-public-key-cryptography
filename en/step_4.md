## How can a key be public?

With the Caesar Cipher, it is crucial that the key remains secret. A public key cryptographic system consists of a **public key** and a matched (but non identical) pair of **private keys**. The private keys are known only to the participants, each participant holds one of the private keys. The public key is created using the matched pair of private keys, and can be known by anyone.

So how does adding a public key __improve__ security? If anyone who wants to can know the public key, does this mean they can break the encryption?

Here's how it works:

- Alice and Bob agree to use a public key cryptographic system and generate one private key each (A and B) and a public key (AB) which is created by multiplying A * B
- Bob sends Alice the public key AB
- Alice receives the public key AB, and she knows this public key corresponds to her private key A. Alice encrypts her message with her private key A and sends it to Bob.
- Bob receives Alice's encrypted message. He has the public key AB and his private key B. Bob knows that AB = A * B, so he can work out A (by calculating A = AB / B) and decrypt the message from Alice.

### Test your understanding
1. Why is this an **asymmetric** encryption algorithm?
1. Why don't Alice and Bob just each use private keys?
1. Why is the public key even needed?

### Answers to Test your understanding

--- collapse ----
---
title: Answer
image: images/https.png
---

- Answer: Bob's and Alice's private keys are different. The private key used to perform the encryption is not the same as the private key held by the person decrypting the information.
- Answer: Alice's key and Bob's key are not the same. If Alice used a private key to encrypt the data without the existence of a shared public key, it would not be unlockable with Bob's private key. Both Bob's key and the public key together must be known for Bob to be able to decrypt the message, because Bob needs both his key and the public key to be able to decrypt the message.
- Answer: Alice encrypts the message with her private key to prove she is the sender, and Bob reads the message using his private key, which is the only way of decrypting the message, thus proving he is the intended recipient. This is only possible with the addition of a shared public key.

--- /collapse ---
