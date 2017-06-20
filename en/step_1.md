# OctaPi: Public Key Cryptography

In this resource you will learn about the ideas behind public key cryptography (PKC), including the concepts of a **public key** and a **private key**. With this background on PKC, you will test your understanding by answering questions and completing a Python programming challenge. You will then use the OctaPi to find prime factors with a brute-force method.

## The story of Public Key Encryption

In 1976, the American mathematicians Whitfield Diffie and Martin Hellman published a method for securely exchanging cryptographic keys in public. For many years this was the story of PKC. However, in 1997 GCHQ declassified and published work done for them in the early 1970s by British mathematicians that showed that the key concepts of public key cryptography had been originally discovered in the UK. Up to that point, this had all been kept secret by the UK government.

The GCHQ mathematician James Ellis first came up with the idea in two papers: [The Possibility of Secure Non-secret Digital Encryption](https://www.gchq.gov.uk/sites/default/files/document_files/CESG_Research_Report_No_3006_0.pdf) (January 1970) and [The Possibility of Secure Non-secret Analogue Encryption](https://www.gchq.gov.uk/sites/default/files/document_files/CESG_Research_Report_No_3007_0.pdf) (May 1970).

In 1974, another GCHQ mathematician, Clifford Cocks, described a possible implementation of the "non-secret encryption" technique using prime numbers in his paper [Note on "Non-secret Encryption"](https://www.gchq.gov.uk/sites/default/files/document_files/Cliff%20Cocks%20paper%2019731120.pdf).

A third GCHQ mathematician, Malcolm Williamson, described a method of key exchange in January 1974 in his paper [Non-secret Encryption using a Finite Field"](https://www.gchq.gov.uk/sites/default/files/document_files/nonsecret_encryption_finite_field_0.pdf). It is very similar to the Diffie-Hellman technique, but predates it by several years.

If you are interested in knowing more about the topic, have a look at _Applied Cryptography - Protocols, Algorithms, and Source Code in C_, Bruce Schneier, Wiley, ISBN 978-1-119-09672-6. Note that the story of public key cryptography in this book pre-dates the GCHQ announcement in 1997.

## Licence

Build an OctaPi by [GCHQ](https://www.gchq.gov.uk/) and the Raspberry Pi Foundation is licenced under a Creative Commons Attribution 4.0 International Licence.
Based on a work at https://github.com/raspberrypilearning/rpi-python-build-an-octapi

**Code and scripts**
Copyright: [Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
License: [Apache 2](https://www.apache.org/licenses/LICENSE-2.0)
