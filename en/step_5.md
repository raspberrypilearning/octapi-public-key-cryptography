## How are public and private keys chosen?

Using public key cryptography is like signing a message with your own __digital signature__. Not only does it prevent unauthorised people from reading your message, it proves that the message originates from the person who claims to have sent it.

The **public key** could be based on a number which meets the following criteria:

- It is chosen using a random source of information so that it is unpredictable
- It comprises the product of two numbers, A * B = AB, where A and B are both **prime** (each only divisible by themselves and 1)
- The product AB is a large number having many digits
- A and B are used as private keys and are **factors** of the public key, AB

We can see how this works in practice as follows.

Suppose we ignored the requirement for a large number for the time being and use small randomly chosen **prime** numbers, A=2 and B=5. This makes the **public key**, AB = 2 * 5 = 10, and we can see right away that A=2 and B=5 are the only possible **factors** of 10. If we use A=2 and B=5 as the **private keys**, AB = 10 becomes the **public key**.

Let's assume Alice uses A=2 as her **private key** and Bob uses B=5 as his.

An attacker intercepts the message sent from Bob to Alice. The attacker can find out that the **public key** was 10 because it will need to be sent along with the encrypted message, and the attacker may even know that the **private keys** are the **factors** of the **public key**.

So from the attacker's pint of view, to break the cryptography they will need to find, A and B, by finding the factors of the **public key**, AB = 10:

```
10 = A * B
```

Because we have chosen small value **private keys**, A=2 and B=10, in this example, it is very easy for the attacker to figure out what the **private keys** are. All they have to do is try all possible values of `A` and `B` and see which result in the value 10. In this example the attacker could probably even do it in their head!

However, what if the **public key** was a larger number, it would be considerably more difficult to work out what the **factors** are. In essence, this is what protects the message: a hard maths problem.

How easy would it be to find the two **factors** using a computer program?

## Finding factors

Remember that one of the criteria for a suitable public key that we are using is that it is a number which is the product of two **prime** numbers, or to put it another way, a number which has only two **factors**.

### Test your understanding 3
1. If you were given the number 12 and asked to find out its factors, what strategy might you take?
1. Does the number 12 meet the criteria of only having two factors?
1. Can you generalise your strategy from question 1, so that if you were given the number `n` and asked to find out its factors, you could describe to someone how to do it?

### Answers to Test your understanding 3
1. Try to divide 12 by all the numbers between 2 and 11, and write down which ones it is divisible by.
1. No. The number 12 can be factorised as 12 = 2 * 6 and 12 = 3 * 4.
1. You may generalise your previous rule as "Try to divide n by all the numbers between 2 and n-1, and write down which ones it is divisible by." In actual fact, you don't need to test up to n-1, you can stop at √n. Why not try [this activity](https://nrich.maths.org/7520) to learn about the Sieve of Eratosthenes to see why!
