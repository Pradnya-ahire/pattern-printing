n=7
for i in range(n):     # This loop is used to print 7 rows
    for j in range(n):   # This loop is used to print 7 columns
        if i==0 or i==n-1 or j==0 or j==n-1: #this used to print the stars only on border lines
            print("*",end = " ")
        else:
            print(" ",end = " ")       # If the position is not on the border, it prints a space
    print()
