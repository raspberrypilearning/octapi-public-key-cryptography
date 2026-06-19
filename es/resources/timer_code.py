from time import time

# Start the timer
start = time()

# Run some example code
for i in range(1000):
    print("Heya")

# Stop the timer
end = time()
total = end - start
print( str(total) + " seconds" )
