# So, can I hack with my OctaPi?


In short, no! Whilst you have demonstrated that using the OctaPi with multiple cores working in parallel can complete this kind of task much more quickly than a single processor, in practice, you still can't use it to break encryption. The 'large' number `2396059349` that you found the factors for in the demonstration is actually small compared to the size of the numbers actually used in public key cryptography. In fact, they may be as large as 2048 bits — that's 617 digits! Even with the power of multiple cores, calculating the prime factors for numbers like that has not been achieved — though not for lack of trying, as there was once a $200,000 USD prize offered to anyone who could accomplish it!

Watch this YouTube video to find out why you can't use your OctaPi to break RSA or other forms of public key encryption.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BI2RrHQ45XE" frameborder="0" allowfullscreen></iframe>

## What next?
- Not every program can be executed more quickly on an OctaPi. What characteristics make a program suitable to run on a cluster?
- Look up the Diffie-Hellman method of public key exchange, which is different to the method described in this project.
