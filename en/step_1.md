# OctaPi: public key cryptography

In this resource, you will learn about the ideas behind public key cryptography (PKC), including the concepts of a **public key** and a **private key**. With this background on PKC, you will test your understanding by answering questions and completing a Python programming challenge. You will then use the OctaPi to find prime factors with a brute-force method.

## The story of public key encryption

In 1976, the American mathematicians Whitfield Diffie and Martin Hellman published a method for securely exchanging cryptographic keys in public. For many years, this was the story of PKC. However, in 1997, GCHQ declassified and published work done for them in the early 1970s by British mathematicians that showed that the key concepts of public key cryptography had originally been discovered in the UK. Until then, this had all been kept secret by the UK government.

The GCHQ mathematician James Ellis first came up with the idea in two papers: *The Possibility of Secure Non-secret Digital Encryption* (January 1970) and *The Possibility of Secure Non-secret Analogue Encryption* (May 1970).

In 1974, another GCHQ mathematician, Clifford Cocks, described a possible implementation of the "non-secret encryption" technique using prime numbers in his paper *Note on "Non-secret Encryption"*.

A third GCHQ mathematician, Malcolm Williamson, described a method of key exchange in January 1974 in his paper *Non-secret Encryption using a Finite Field*. It is very similar to the Diffie-Hellman technique, but predates it by several years.

If you are interested in knowing more about the topic, have a look at _Applied Cryptography: Protocols, Algorithms, and Source Code in C_, Bruce Schneier, Wiley (ISBN 978-1-119-09672-6). Note that the story of public key cryptography in this book predates the GCHQ announcement in 1997.

--- collapse ---
---
title: What you will need
---
### Hardware
For most of the tasks in this resource, you will just need a computer system running Python 3.

To complete the final task, you will need an OctaPi. For instructions on how to build one, see [Build an OctaPi](/en/projects/rpi-python-build-an-octapi).

![OctaPi system](images/octapi-system.png)

### Software
- Python 3
--- /collapse ---

--- collapse ---
---
title: Licence
---
OctaPi: Public Key Cryptography by [GCHQ](https://www.gchq.gov.uk/) and the Raspberry Pi Foundation is licensed under a Creative Commons Attribution 4.0 International Licence.
Based on a work at https://github.com/raspberrypilearning/rpi-python-octapi-public-key-cryptography

**Code and scripts**
Copyright: [Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
Licence: [Apache 2](https://www.apache.org/licenses/LICENSE-2.0)
--- /collapse ---
