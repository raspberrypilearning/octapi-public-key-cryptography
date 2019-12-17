# How are public and private keys chosen?

Using public key cryptography is like signing a message with your own __digital signature__. Not only does it prevent unauthorised people from reading your message, it proves that the message originates from the person who claims to have sent it.

A **public key** can be any number that meets the following criteria:

- It is chosen using a random source of information so that it is unpredictable
- In part, it is the product of two numbers, A * B = AB, where A and B are both **prime** numbers (each only divisible by itself and 1)
- This product AB is a large number and therefore has many digits
- A and B are also used to generate a private key and are the only **factors** of the public key AB

You can see how this works in practice as follows:

Suppose that we ignore the requirement for the **public key** to be a large number for now and use small randomly chosen **prime** numbers, A=2 and B=5. This makes the **public key** AB = 2 * 5 = 10. It is easy to work out that A=2 and B=5 are the only possible **factors** of 10.

We can use A=2 and B=5 as the **private keys**.

Now, imagine that an attacker intercepts the message sent from Bob to Alice. The attacker knows that the **public key** is 10.

So from the attacker's point of view, to break the cryptography, they will need to find A and B by finding the factors of the **public key**, AB = 10:

```
10 = A * B
```

Because we have chosen **private keys** with small values, A=2 and B=5, it is very easy for the attacker to work out what these **private keys** are. All they have to do is multiply all possible values of `A` and `B` and see which multiplication results in the value 10. In this example, the attacker could probably even do it in their head!

However, if the **public key** were a larger number, it would be considerably more difficult to work out the **factors**. Essentially, this is what protects the message: a hard maths problem.
