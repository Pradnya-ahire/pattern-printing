n=6
for i in range(1,n+1):  # This loop is used to print the upper half of the diamond
    for k in range(n-i):  # This loop prints spaces before stars
        print(" ",end = " ")
    for j in range(i*2-1):    # This loop prints stars in increasing order
        print("*",end=" ")
    print()          # This moves to the next line


for i in range(n-1,0,-1): # This loop is used to print the lower half of the diamond
    for k in range(n-i):   # This loop prints spaces before stars
        print(" ",end = " ")  
    for j in range(i*2-1):    # This loop prints stars in decreasing order
        print("*",end=" ")
    print()    # This moves to the next line


