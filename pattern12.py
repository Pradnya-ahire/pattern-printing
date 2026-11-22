n = 5

for i in range(1, n + 1): # This loop is used to print the upper half of the pattern
    for j in range(i):   # This loop prints stars on the left side
        print("*", end=" ")
    for j in range(2 * (n - i)):   # This loop prints spaces in the middle
        print(" ", end=" ")
    for j in range(i):   # This loop prints stars on the right side
        print("*", end=" ")
    print()   # This moves to the next line

for i in range(n - 1, 0, -1):  # This loop is used to print the lower half of the pattern
    for j in range(i):
        print("*", end=" ")      # This loop prints stars on the left side
    for j in range(2 * (n - i)):   # This loop prints spaces in the middle
        print(" ", end=" ")
    for j in range(i):            # This loop prints stars on the right side
        print("*", end=" ")
    print()   # This moves to the next line