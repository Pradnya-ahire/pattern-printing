n=6

for i in range(n-1,0,-1):  # This loop is used to print rows in decreasing order
    for k in range(1,n-i): # This loop is used to print spaces before stars
        print(" ",end = " ")  
    for j in range(1,i*2):    # This loop is used to print stars in decreasing order
        print("*",end=" ")
    print()


