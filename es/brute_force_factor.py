public_key = 28

# Store the discovered factors in this list
factors = []

# Begin testing at 2 
test_number = 2

# Loop through all numbers from 2 up until the public_key number
while test_number < public_key:

    # If the public key divides exactly into the test_number, it is a factor
    if public_key % test_number == 0:
        factors.append(test_number)

    # Move on to the next number
    test_number += 1

# Print the result
print(factors)
