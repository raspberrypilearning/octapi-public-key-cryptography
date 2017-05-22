# So can I now hack with my OctaPi?

In short, no! Whilst you have demonstrated that using the OctaPi with multiple cores working in parallel can complete this kind of task much more quickly than a single processor working on the task, you still can't use it to break encryption in practice. The 'large' prime number `2396059349` we found the factors for in the demonstration is actually not very large compared to the size of the primes actually used in public key cryptography. For example, the numbers used may be as large as 2048 bits (that's 617 digits!) Even using the power of multiple cores, calculating the prime factors has not been achieved - there was even once a $200,000 USD prize offered for anyone who could achieve it!

Take a look at this YouTube video to find out why you can't use your OctaPi to break RSA or other forms of public key encryption.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BI2RrHQ45XE" frameborder="0" allowfullscreen></iframe>

## What's next?
- Not every program can be executed more quickly on an OctaPi. What characteristics make a program suitable to run on a cluster?
- Look up the Diffie-Hellman method of public key exchange which is different to the method described here
