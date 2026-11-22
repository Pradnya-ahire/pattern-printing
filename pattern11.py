for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == i or i == 5:  # This condition checks the first column, diagonal and last row
            print("*", end=" ")
        else:
            print(" ", end=" ")   # If the condition is false, it prints a blank space
    print()