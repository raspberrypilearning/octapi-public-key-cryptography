# Spot the weaknesses

Imagine you are an adversary trying to read the encrypted message that Alice sent to Bob. You already have the message and the public key.

**Question 3** - What information do you need to obtain to try to decrypt the message?

**Question 4** - How could you try to obtain this information?

### Answers

**Question 3** - To be able to decrypt the message, you must find out Bob's private key.

**Question 4** - You could try to obtain this information in two ways:

- Break into where Bob stores his private key and steal it. This might involve both physical security measures (guards, CCTV, locked rooms) and electronic security measures. This may work, however it is likely that Bob will find out if you steal his key and that he and Alice will generate a different set of keys for future messages.
- Try to work out both private keys by searching for the two prime factors of the public key using a program. Bob will not know his key has been compromised and you can continue to read future messages undetected. As a bonus, this method also simultaneously finds Alice's key too, so you will be able to read messages sent by Bob to Alice.

In order to obtain Bob's key by working out the prime factors of the public key, you will need to launch a **brute force attack**. This means you will try all of the possible solutions in turn until you find one which works.
