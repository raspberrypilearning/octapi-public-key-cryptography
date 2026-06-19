# How are public and private keys chosen?

Using public key cryptography is like signing a message with your own **digital signature**. Not only does it prevent unauthorised people from reading your message, it proves that the message originates from the person who claims to have sent it.

The **public key** can be any number which meets the following criteria:

- It is chosen using a random source of information so that it is unpredictable.
- It is the product of two numbers, A * B = AB, and A and B are both **prime** numbers (each only divisible by itself and 1).
- This product AB is a large number and therefore has many digits.
- A and B are used as private keys and are the only **factors** of the public key AB.

We can see how this works in practice as follows:

Suppose we ignore the requirement for the **public key** to be a large number for now and use small randomly chosen **prime** numbers, A=2 and B=5. This makes the **public key** AB = 2 * 5 = 10. It is easy to work out that A=2 and B=5 are the only possible **factors** of 10.

If we use A=2 and B=5 as the **private keys**, AB = 10 becomes the **public key**. Let's assume Alice uses A=2 as her **private key** and Bob uses B=5 as his.

Now imagine an attacker intercepts the message sent from Bob to Alice. The attacker can find out that the **public key** was 10 because it will need to be sent along with the encrypted message, and the attacker may even know that the **private keys** are the **factors** of the **public key**.

So from the attacker's point of view, to break the cryptography they will need to find A and B by finding the factors of the **public key**, AB = 10:

    10 = A * B
    

Because we have chosen small value **private keys**, A=2 and B=5, in this example, it is very easy for the attacker to figure out what these **private keys** are. All they have to do is multiply all possible values of `A` and `B` and see which multiplication results in the value 10. In this example, the attacker could probably even do it in their head!

However, if the **public key** were a larger number, it would be considerably more difficult to work out the **factors**. Essentially, this is what protects the message: a hard maths problem.

## Example: Choosing public keys to use with the Caesar Cipher

The Caesar Cipher has 25 possible keys which represent the number of places each letter of the alphabet is transposed to generate the cipher text. Of these, the following numbers are prime (only divisible by itself and 1).

- [ 2, 5 ]
- [ 7, 11 ]
- [ 13, 17 ]
- [ 19, 23 ]

We have put these into pairs to illustrate four possible private key combinations which could be used with the Caesar Cipher. Supposing we chose the first pair in this list, `[2, 5]`, we would calculate the public key by multiplying the two primes together - `2 * 5 = 10`. The public key for this pair is 10.

The two private keys of 2 and 5 are held by Alice and Bob. Alice can encrypt a message with her private key, and send the public key with the message to Bob. Bob then uses the combination of the public key and his private key to work out the key Alice used to encrypt her message - `10 / 5 = 2`. Bob can then decrypt the message. You can try this out in the interactive example below. <iframe src="https://trinket.io/embed/python/bf71e29704" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

[Download the code](resources/pkc_caesar.py)

Of course, nobody would actually use public key cryptography with the Caesar Cipher - it would be extremely easy for any attacker to work out the factors and therefore the keys used, even without the help of a computer!