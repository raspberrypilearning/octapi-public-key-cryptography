# This code implements the Caesar cipher, but using public key
# encryption techniques. No one would actually do this, but as
# the Caesar cipher is easy to understand, it's a potentially
# handy cipher technique in order to explain PKC.
#
# Instead of passing the key (amount of shift) privately through
# an independent channel, we can pass the public key with the 
# message. 

# All original code: Crown Copyright 2017 

# Using public key cryptography is like signing a message with 
# your own digital signature. Not only does it prevent 
# unauthorised people from reading your message, it proves that 
# the message originates from the person who claims to have sent 
# it.
#
# The public key can be any number which meets the following 
# criteria:
#     * It is chosen using a random source of information so that 
#       it is unpredictable.
#     * It is the product of two numbers, A * B = AB, and A and 
#       B are both prime numbers (each only divisible by itself 
#       and 1).
#     * This product AB is a large number and therefore has many 
#       digits.
#     * A and B are used as private keys and are the only factors 
#       of the public key AB.
#
# We can see how this works in practice as follows:
# Suppose we ignore the requirement for the public key to be a 
# large number for now and use small randomly chosen prime numbers, 
# A=2 and B=5. This makes the public key AB = 2 * 5 = 10. It is 
# easy to work out that A=2 and B=5 are the only possible factors 
# of 10.
#
# If we use A=2 and B=5 as the private keys, AB = 10 becomes the 
# public key. Let’s assume Alice uses A=2 as her private key and 
# Bob uses B=5 as his.
# 
# Now imagine an attacker intercepts the message sent from Bob to 
# Alice. The attacker can find out that the public key was 10 
# because it will need to be sent along with the encrypted message, 
# and the attacker may even know that the private keys are the 
# factors of the public key.
#
# So from the attacker’s point of view, to break the cryptography 
# they will need to find A and B by finding the factors of the public 
# key, AB = 10
#
# Because we have chosen small value private keys, A=2 and B=5, 
# in this example, it is very easy for the attacker to figure out 
# what these private keys are. All they have to do is multiply all 
# possible values of A and B and see which multiplication results 
# in the value 10. In this example, the attacker could probably 
# even do it in their head!
# 
# However, if the public key were a larger number, it would be 
# considerably more difficult to work out the factors. Essentially, 
# this is what protects the message: a hard maths problem.

# public key is the product of two private keys which are prime numbers
privatekey = [ [ 2, 5 ], [ 7, 11 ], [ 13, 17 ], [ 19, 23 ] ]

#
# Caesar cipher - a shift of the letters of the alphabet with
#                 wrap-around at the end for continuity
#
def caesar( plaintext, cipherkey ):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphertext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in range(len(plaintext)):
        idx = alphabet.index(plaintext[i])

        # wrap around at top on encrypt
        idx =  (idx + cipherkey) % len(alphabet) 

        # prevent underflow on decrpt
        if (idx<0): idx += len(alphabet)

        # apply shift to the character        
        ciphertext = ciphertext + alphabet[idx]

    return( ciphertext )


# main loop
if __name__ == '__main__':
    # Encrypting or decrypting?
    encrypt = input( "Encrypting or decrypting (E or D)? ")
    encrypt = encrypt.upper() #  convert to upper case
    if (encrypt == "E"):
        encrypting = True
    elif (encrypt == "D"):
        encrypting = False
    else:
        print( "must be E or D, cannot continue" )
        exit(0)

    # Which set of keys should be used
    print("Choice of keys is as follows:")
    for i in range(len(privatekey)):
        print( "Private key set %s is [ %s, %s ] (public key %s)" % (i, privatekey[i][0], privatekey[i][1], privatekey[i][0] * privatekey[i][1]))
    keyindex = int( input("Which set of keys? (0-3) ") )
    if (keyindex > 3):
        print( "Keys must be in range (0-3), cannot continue" )
        exit(0)

    # find out if private key A or B should be used
    user = input( "Which user - Alice or Bob (A or B)? ")
    user = user.upper() #  convert to upper case
    if (user == "A"):
        username = "Alice"
        # Alice's private key choice from the selected set depends on whether she is encrypting or decrypting  
        if (encrypting): 
            useridx = 0 
        else: 
            useridx = 1
    elif (user == "B"):
        # Bob's private key choice from the selected set depends on whether he is encrypting or decrypting  
        username = "Bob"
        if (encrypting): 
            useridx = 1 
        else: 
            useridx = 0
    else:
        print( "User must be A or B, cannot continue" )
        exit(0)

    # what plain text should be enciphered
    msgtext = input( "Message text to be processed using Caesar cipher? ")
    msgtext = msgtext.replace(" ", "X") # replace space with 'X'
    msgtext = msgtext.upper()           # force all characters to upper case

    # public key is the product of the pair of private keys 
    publickey = privatekey[keyindex][0] * privatekey[keyindex][1]

    # explain what we are doing
    print( "Public key is %s for set %s, so private key to be used by %s is %s" % (publickey, keyindex, username, privatekey[keyindex][useridx]) )

    # obtain the caesar cipher using the selected private key 
    if (encrypting):
        ciphertext = caesar(msgtext, privatekey[keyindex][useridx] )
    else:
        plaintext = caesar(msgtext, -privatekey[keyindex][useridx] )

    if (encrypting):
        print( "%s therefore sends public key %s and %s as cipher text %s" % (username, publickey, msgtext, ciphertext) )
    else:
        print( "%s therefore decrypts %s as %s" % (username, msgtext, plaintext) )

