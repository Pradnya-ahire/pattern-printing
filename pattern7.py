n=6
for i in range(1,n):       # This loop is used to print 5 rows
    for k in range(1,n-i):      # This loop is used to print spaces before stars
        print(" ",end = " ")
    for j in range(1,i*2):          # This loop is used to print stars in increasing order
        print("*",end=" ")
    print()