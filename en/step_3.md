# What is Public Key Cryptography?

Although you might not realise it, you probably use public key cryptography on a daily basis. When visiting a web page, you may have noticed a small padlock in the address bar, and an address beginning with `https`, like this:

  ![HTTPS webpage](images/https.png)

This padlock means that when you communicate with the web page, the information sent by you is only able to be read by that web page, and the information it sends back is only able to be read by you. The website uses **public key cryptography** to keep your information secure. Public key cryptography provides two useful properties - __encryption__ (preventing unauthorised access to the data) and __authentication__ (proving the person sending or receiving is who they claim to be).

**Why did GCHQ keep the discovery of public key cryptography secret in the 1970s?**

--- collapse ---
---
title: Answer
image: images/https.png
---

GCHQ is part of the team which protects the UK, along with law enforcement and other intelligence agencies. They defend government systems from attack, provide support to the Armed Forces and strive to keep the public safe, in real life and online. In the 1970s this involved creating cryptographic systems to protect government and military communications, and to  remain effective, the systems had to remain secret. When James Ellis died in 1997, it was decided to reveal the story of how public key cryptography was developed. Today, GCHQ works with industry, academia, and other parts of government to improve cybersecurity in the UK by promoting development of new cryptographic techniques, as much as possible without using secrecy.

--- /collapse ---

## How does traditional encryption work?

You may have come across simple encryption methods before, such as the Caesar Cipher. Here is a project you could try which uses a [Caesar Cipher](https://codeclubprojects.org/en-GB/python/secret-messages/)

In the Caesar Cipher method, a numerical key is used to encrypt a message. The letters of the alphabet are transposed forwards by the number of places given by the key, so if the key is 3, the letter A becomes D, the letter B becomes E, and so on. The alphabet is considered to wrap around, so the letter Z would become C.

  ![Caesar cipher example](images/messages-wheel-eg.png)

A message is encrypted using the key, and the receiver uses the same key to decrypt the message. The key needs to be agreed on by both sides beforehand and kept secret.

### Test your understanding

**Does the Caesar Cipher use a public or a private key?**

--- collapse ---
---
title: Answer
image: images/https.png
---

The key must be kept private, otherwise anyone could decrypt the information.

--- /collapse ---

**Does the Caesar Cipher offer any authentication?**

--- collapse ---
---
title: Answer
image: images/https.png
---

No - anyone could send an encrypted message if they knew the key, and there is no way of proving who created the message.

--- /collapse ---

**If you intercepted a message encrypted using a Caesar Cipher, how would you go about decrypting it without knowing the key?**

--- collapse ---
---
title: Answer
image: images/https.png
---

Try all possible keys (there are only 25) until you find the correct one. This is known as a brute-force attack.

--- /collapse ---
