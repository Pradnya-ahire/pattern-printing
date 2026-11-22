n=5
for i in range(1,n+1):  # This loop is used to print 5 rows
    for j in range(1,n-i+1):      # This loop is used to print spaces before stars
        print(" ",end= " ")          
    for k in range(1,i+1) :        # This loop is used to print stars in increasing order
        print("*",end = " ")
    print()