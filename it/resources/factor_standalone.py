# Find the prime factors of a large 'semi-prime' number.
#
# This code runs standalone on an OctaPi client and is intended to
# show the difference in run time with similar code running on the
# Octapi cluster using Dispy.
#

# Primality test algorithms derived from code by Shay Margalit, 12 Dec 2013
# https://www.codeproject.com/articles/691200/primality-test-algorithms-prime-test-the-fastest-w
#
# License: The Code Project Open License (CPOL) 1.02, https://www.codeproject.com/info/cpol10.aspx
# The main points subject to the terms of the License are:
#   Source Code and Executable Files can be used in commercial applications;
#   Source Code and Executable Files can be redistributed; and
#   Source Code can be modified to create derivative works.
#   No claim of suitability, guarantee, or any warranty whatsoever is provided. The software is provided "as-is".
#   The Article(s) accompanying the Work may not be distributed or republished without the Author's consent

# All other original code: Crown Copyright 2016, 2017


def find_factor(semi_prime, lower, upper):

    def naivePrimalityTest(number):
        import math

        if number == 2:
           return true
        if number % 2 == 0:
            return False

        i = 3
        sqrtOfNumber = math.sqrt(number)

        while i <= sqrtOfNumber:
            if number % i == 0:
                return False
            i = i+2

        return True

    def FermatPrimalityTest(number):
        import random, math

        # If number != 1
        if (number > 1):
            # Repeat the test a few times
            for time in range(3):
                # Draw a RANDOM number in range of number ( Z_number )
                randomNumber = random.randint(2, number)-1

                # Test if a^(n-1) = 1 mod n
                if ( pow(randomNumber, number-1, number) != 1 ):
                    return False

            return True
        else:
            # case number == 1
            return False

    def MillerRabinPrimalityTest(number):
        import random, math

        # Because the algorithm input is an ODD number, if we get
        # even and it is the number 2 we return TRUE ( special case )
        # If we get the number 1 we return false, and if we get any other even
        # number we will return false.

        if number == 2:
            return True
        elif number == 1 or number % 2 == 0:
            return False

        # First we want to express n as : 2^s * r ( where r is odd )

        # The odd part of the number
        oddPartOfNumber = number - 1

        # The number of times that the number is divided by two
        timesTwoDividNumber = 0

        # While r is even, divide by 2 to find the odd part
        while oddPartOfNumber % 2 == 0:
            oddPartOfNumber = oddPartOfNumber // 2
            timesTwoDividNumber = timesTwoDividNumber + 1


        # Since there are numbers that are cases of "strong liar" we
        # need to check more than one number

        for time in range(3):

            # Choose "Good" random number
            while True:
                # Draw a RANDOM number in range of number ( Z_number )
                randomNumber = random.randint(2, number)-1
                if randomNumber != 0 and randomNumber != 1:
                    break

            # randomNumberWithPower = randomNumber^oddPartOfNumber mod number
            randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)

            # If random number is not 1 and not -1 ( in mod n )
            if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
                # Number of iterations
                iterationNumber = 1

                # While we can square the number and the squared number is not -1 mod number
                while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                    # Square the number
                    randomNumberWithPower = pow(randomNumberWithPower, 2, number)

                    # Increment the number of iteration
                    iterationNumber = iterationNumber + 1

                # If x != -1 mod number then it is because we did not find strong witnesses
                # hence 1 has more than two roots in mod n ==>
                # n is composite ==> return false for primality

                if (randomNumberWithPower != (number - 1)):
                    return False

        # Will the number pass the tests ==> it is probably prime ==> return true for primality
        return True


    # Search between the lower and upper limits
    while (lower <= upper):
        factor1 = lower
        # Only test prime numbers
        if MillerRabinPrimalityTest(factor1) and FermatPrimalityTest(factor1):
            if (semi_prime % factor1 == 0):
                factor2 = semi_prime // factor1

                # Try this prime to see if it is a factor
                if (factor1 * factor2 == semi_prime):
                    #print ('%i * %i = %i' % (factor1, factor2, factor1*factor2))
                    return (factor1, factor2)

        lower = lower + 2    # Skip even factors because they can't be prime

    # No factors found
    return (0, 0)


# Main loop
if __name__ == '__main__':
    import random, math

    # This is the number we have been given to factor
    semi_prime = int( input( "What semi-prime number do you want to try and factor? " ) )
    # chunk size = chunk_scale * log(semi-prime)
    chunk_scale = int( input( "What scale of search chunk size do you want? (generally 100 - 1000) ") )

    # Assume that the prime factors are roughly the same length
    # We can start our search from the square root
    lower = int( math.sqrt(semi_prime) )
    if (lower % 2) == 0: lower += 1    # Make sure we start with an odd number (which could also be prime)
    upper = semi_prime / 2             # Make sure we search far enough

    # The chunk size is the search space starting from 'lower'
    chunk = int ( chunk_scale * math.log(semi_prime) )

    # Search for prime factors between the lower and upper limits
    found = False
    while (lower <= upper) and (found == False):
        print(('Attempting factors in range %i - %i, chunk size %i' % (lower, lower+chunk, chunk) ))

        factor1, factor2 = find_factor(semi_prime, lower, lower+chunk)

        # Report the outcome
        if (factor1 != 0):
            print(('%i * %i = %i' % (factor1, factor2, factor1*factor2)))
            found = True

        # Next chunk (make sure it's prime)
        lower += chunk
        if (lower % 2) == 0: lower += 1

    # Report the outcome
    if (found == False): print ('no factors found')
