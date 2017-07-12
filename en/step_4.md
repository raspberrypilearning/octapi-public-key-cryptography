# How can a key be public?

When you use the Caesar Cipher, it is crucial that the key remains secret. This is because it is a form of symmetric cryptography, meaning that the same key is used to encrypt and decrypt messages.

A public key cryptographic system consists of a **public key** a **private key**. The private key is only known to the receiver of the encrypted message. The public key can be provided to anyone who wants to send an encrypted message to the person who generated the keys.

So how does adding a public key __improve__ security? If anyone can find out the public key, does this mean they can break the encryption?

Here's how it works:

- Alice wants to receive encrypted messages from Bob, and they agree on a cryptographic system.
- Alice generates a private key and a public key, and sends the public key off to Bob. She doesn't care if anyone else knows the public key, as it can only be used to encrtypt messages.
- Bob uses Alice's public key to encrypt a message. He can send this to Alice. It doesn't matter if anyone else receives the encrypted message, as it can only be decrypted by Alice's private key, which she keeps safe.
- When Alice receives the message, she can use her private key to decrypt it, and read the message Bob sent.
- If Alice now want to reply to Bob, then Bob needs to generate his own private and public keys. He can then send hsi own public key to Eve, and she can use it to securely encrypt messages to Bob.

### Test your understanding

**Why is this an asymmetric encryption algorithm?**


--- collapse ----
---
title: Answer
---

Bob's and Alice's private keys are different. The private key used to perform the encryption is not the same as the private key held by the person decrypting the information.

--- /collapse ---

**Why is the public key even needed?**


--- collapse ----
---
title: Answer
---
A public key stops the problem of secure key exchange. If Alice and Bob were using a symmetric encryption algorithm, such as the Caesar Cypher, how could they securely tell each other what they key was, without actually meeting in person and whispering it? By using a public key, it doesn't matter who knows how to encrypt a message, as only the private key can decrypt it.

--- /collapse ---
